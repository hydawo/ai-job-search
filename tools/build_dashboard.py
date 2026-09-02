#!/usr/bin/env python3
"""Rebuild the dashboard's RECORDS data block from job_search_tracker.csv.

The dashboard (reports/application-dashboard.html) is a data-driven shell: all
design, layout and rendering logic lives in the file's CSS/JS, and every value on
the page comes from a single `const RECORDS = [...]` array. This script rewrites
only that array, so the CSV stays the single source of truth for the data while
the presentation layer is never touched.

Two fields cannot be derived from the CSV and are preserved from the existing
file rather than regenerated:

  events        the per-role stage timeline (dates + notes), hand-curated
  eventsSource  provenance marker for the above

For a row that has no existing record, a single opening event is synthesised
from the CSV's own date/status so a new role still plots on the timeline. Once a
human refines that timeline in the HTML, later runs keep it.

Usage:  python3 tools/build_dashboard.py [--check]
        --check  exit 1 if the dashboard is out of date, write nothing
"""
from __future__ import annotations

import csv
import datetime
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRACKER = os.path.join(ROOT, "job_search_tracker.csv")
DASHBOARD = os.path.join(ROOT, "reports", "application-dashboard.html")

BEGIN = "const RECORDS = ["
END = "];"

# Tracker status -> bucket shown on the dashboard. Anything unmapped falls back
# to a title-cased version of the raw status, which is what the existing file
# does for drafted/shortlisted/skipped/evaluated.
BUCKETS = {
    "applied": "Active",
    "interview": "Interview",
    "offer": "Offer",
    "hired": "Hired",
    "rejected": "Rejected/Closed",
    "no_response": "Rejected/Closed",
    "no response": "Rejected/Closed",
    "offer_declined": "Rejected/Closed",
    "withdrawn": "Rejected/Closed",
}

# Statuses that mean a CV actually went to an employer. Used for the headline
# "applications submitted" stat, which must stay distinct from current stage:
# a role that has moved past applied still counts as submitted.
SUBMITTED = {"applied", "interview", "offer", "hired", "rejected", "offer_declined", "withdrawn"}

INTERVIEWED = {"interview", "offer", "hired"}

FIT_RE = re.compile(r"^\s*(.*?Fit)\s*\((\d+)\s*/\s*100\)\s*$", re.I)
URL_RE = re.compile(r"https?://[^\s,)]+")


def parse_fit(raw: str):
    """'Strong Fit (81/100)' -> ('Strong Fit (81/100)', 'Strong Fit', 81)."""
    raw = (raw or "").strip()
    if not raw:
        return "", "", None
    m = FIT_RE.match(raw)
    if m:
        return raw, m.group(1).strip(), int(m.group(2))
    return raw, raw, None


def doc_ref(tex_path: str):
    """cv/foo.tex -> the compiled PDF's href/abs/name, or None if unset.

    The dashboard links the PDF, never the .tex source, and carries an absolute
    path alongside the relative href so a path can be copied straight out.
    """
    tex_path = (tex_path or "").strip()
    if not tex_path:
        return None, None
    pdf = re.sub(r"\.tex$", ".pdf", tex_path)
    return (
        {
            "href": "../" + pdf,
            "abs": os.path.join(ROOT, pdf),
            "name": os.path.basename(pdf),
        },
        tex_path,
    )


def company_short(name: str) -> str:
    """'Evinova (AstraZeneca)' -> 'Evinova' for the compact row label."""
    return re.sub(r"\s*\(.*?\)\s*$", "", (name or "").strip()) or name


def load_existing(html: str) -> dict:
    """Map (company, role) -> existing record, for preserving curated events."""
    try:
        start = html.index(BEGIN)
        body_start = start + len(BEGIN) - 1  # points at the opening '['
        nl = html.index("\n" + END, body_start)  # points at the '\n' before '];'
    except ValueError:
        raise SystemExit("error: could not locate the RECORDS block in the dashboard")
    # Slice must include the closing ']' that sits just after that newline.
    try:
        recs = json.loads(html[body_start : nl + 2])
    except json.JSONDecodeError as exc:
        raise SystemExit(f"error: RECORDS block is not valid JSON ({exc})")
    return {(r.get("company", "").lower(), r.get("role", "").lower()): r for r in recs}


def build_records(rows, existing) -> list:
    out = []
    for row in rows:
        status = (row.get("status") or "").strip().lower()
        company = (row.get("company") or "").strip()
        role = (row.get("role") or "").strip()
        notes = (row.get("notes") or "").strip()

        fit, fit_label, fit_score = parse_fit(row.get("fit_rating", ""))
        cv, cv_tex = doc_ref(row.get("cv_file", ""))
        cl, cl_tex = doc_ref(row.get("cover_letter_file", ""))
        urls = URL_RE.findall(notes)

        prior = existing.get((company.lower(), role.lower()))
        if prior and prior.get("events"):
            events = prior["events"]
            events_source = prior.get("eventsSource", "artifact")
        else:
            # New row: one opening event so it still plots on the timeline.
            events = [{"date": row.get("date", ""), "status": status, "note": ""}]
            events_source = "tracker"

        out.append(
            {
                "date": row.get("date", ""),
                "company": company,
                "role": role,
                "roleType": (row.get("role_type") or "").strip(),
                "sector": (row.get("sector") or "").strip(),
                "channel": (row.get("channel") or "").strip(),
                "statusRaw": status,
                "statusBucket": BUCKETS.get(status, status.title()),
                "isApplication": status in SUBMITTED,
                "contact": (row.get("contact_person") or "").strip(),
                "fit": fit,
                "fitLabel": fit_label,
                "fitScore": fit_score,
                "fitFromNotes": False,
                "notes": notes,
                "posting": urls[-1] if urls else None,
                "source": (row.get("source") or "").strip(),
                "cv": cv,
                "coverLetter": cl,
                "cvTex": cv_tex,
                "clTex": cl_tex,
                "reachedInterview": status in INTERVIEWED
                or any(e.get("status") in INTERVIEWED for e in events),
                "outcome": prior.get("outcome") if prior else None,
                "events": events,
                "eventsSource": events_source,
                "companyShort": company_short(company),
            }
        )
    return out


def render(records) -> str:
    body = json.dumps(records, indent=1, ensure_ascii=False)
    # Match the existing file's formatting: one leading space per top-level entry.
    return BEGIN[:-1] + body + ";"


def main() -> int:
    check = "--check" in sys.argv

    if not os.path.exists(DASHBOARD):
        print(f"error: {DASHBOARD} not found. Run /html-report once to create the shell.", file=sys.stderr)
        return 2

    html = open(DASHBOARD, encoding="utf-8").read()
    with open(TRACKER, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))

    existing = load_existing(html)
    records = build_records(rows, existing)

    start = html.index(BEGIN)
    end = html.index("\n" + END, start) + len("\n" + END)
    updated = html[:start] + render(records) + html[end:]
    updated = re.sub(
        r'const GENERATED = "[^"]*";',
        'const GENERATED = "%s";' % datetime.date.today().isoformat(),
        updated,
        count=1,
    )

    if updated == html:
        print(f"dashboard already up to date ({len(records)} roles)")
        return 0
    if check:
        print(f"dashboard is STALE: tracker has {len(records)} roles, dashboard differs", file=sys.stderr)
        return 1

    open(DASHBOARD, "w", encoding="utf-8").write(updated)
    carried = sum(1 for r in records if r["eventsSource"] != "tracker")
    print(
        f"rebuilt {DASHBOARD} from {os.path.basename(TRACKER)}: "
        f"{len(records)} roles ({carried} with curated timelines preserved, "
        f"{len(records) - carried} new)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
