#!/usr/bin/env python3
"""Check the job boards of companies Hassan has applied to, directly.

Two jobs, every run:

  1. LIVENESS  For every tracker row that is still in play (applied, interview,
     drafted, shortlisted, evaluated), confirm the posting still exists on the
     employer's own board. LinkedIn keeps pages up after a req closes and
     recycles IDs under new titles, so it is not evidence of anything.
  2. NEW ROLES Surface relevant postings on those boards that are not yet in
     job_scraper/seen_jobs.json, and optionally record them there.

Boards are configured in job_scraper/employer_boards.json. Adapters: ashby,
greenhouse, workday, rippling, html-list, radancy (Takeda), apple. Add a company when the first
application to it is submitted.

Usage:
  python3 tools/employer_boards.py            # report only
  python3 tools/employer_boards.py --record   # also write new relevant postings into seen_jobs.json
  python3 tools/employer_boards.py --json     # machine-readable output
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import html as htmllib
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "job_scraper" / "employer_boards.json"
SEEN = ROOT / "job_scraper" / "seen_jobs.json"
TRACKER = ROOT / "job_search_tracker.csv"

# Titles worth surfacing. Same spirit as the scraper's quick title filter.
RELEVANT = re.compile(
    r"product|director|head of|partnership|business development|alliance|clinical|"
    r"research|digital health|biomarker|sensing|program manager|strategy",
    re.I,
)
# Titles that match RELEVANT but are never in scope (engineering, design, sales, hardware, finance...).
EXCLUDE = re.compile(
    r"engineer|developer|designer|sales|marketing|accounting|accountant|counsel|legal|security|"
    r"manufactur|hardware|apparel|accessor|recruit|inspector|editor|scientist|researcher|"
    r"data scientist|art director|sustainability|communications|retail|inside sales|"
    r"tax|audit|passout|clearfacts|customer success|account .*executive|business systems analyst",
    re.I,
)
LIVE_STATUSES = {"applied", "interview", "drafted", "shortlisted", "evaluated"}
UA = {"User-Agent": "Mozilla/5.0 (employer-board check; personal job search)", "Accept": "application/json"}


# Some career sites (Takeda's Radancy) return empty results to a UA that announces itself.
BROWSER_UA = {"User-Agent": "Mozilla/5.0", "X-Requested-With": "XMLHttpRequest"}


def get(url: str, data: dict | None = None, timeout: int = 30, headers: dict | None = None) -> bytes:
    req = urllib.request.Request(url, headers=headers or UA)
    if data is not None:
        req.add_header("Content-Type", "application/json")
        req.data = json.dumps(data).encode()
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def norm(s: str) -> str:
    s = s.lower()
    s = s.replace("&", "and")
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


# ---------------------------------------------------------------- adapters
# Each returns a list of {title, url, location, posted} for the whole board.

def ashby(b):
    d = json.loads(get(f"https://api.ashbyhq.com/posting-api/job-board/{b['slug']}"))
    return [{"title": j.get("title", ""), "url": j.get("jobUrl", ""),
             "location": j.get("location", ""), "posted": (j.get("publishedAt") or "")[:10]}
            for j in d.get("jobs", [])]


def greenhouse(b):
    d = json.loads(get(f"https://boards-api.greenhouse.io/v1/boards/{b['slug']}/jobs"))
    return [{"title": j.get("title", ""), "url": j.get("absolute_url", ""),
             "location": (j.get("location") or {}).get("name", ""),
             "posted": (j.get("first_published") or j.get("updated_at") or "")[:10]}
            for j in d.get("jobs", [])]


def rippling(b):
    d = json.loads(get(f"https://api.rippling.com/platform/api/ats/v1/board/{b['slug']}/jobs"))
    return [{"title": j.get("name", ""), "url": j.get("url", ""),
             "location": (j.get("workLocation") or {}).get("label", ""), "posted": ""}
            for j in d]


def workday(b):
    host, site = b["host"], b["site"]
    seen, out = set(), []
    for term in b.get("search_terms", [""]):
        payload = {"appliedFacets": {}, "limit": 20, "offset": 0, "searchText": term}
        d = json.loads(get(f"https://{host}/wday/cxs/{b['slug']}/{site}/jobs", data=payload))
        for j in d.get("jobPostings", []):
            path = j.get("externalPath", "")
            if path in seen:
                continue
            seen.add(path)
            out.append({"title": j.get("title", ""), "url": f"https://{host}/en-US/{site}{path}",
                        "location": j.get("locationsText", ""), "posted": j.get("postedOn", "")})
    return out


def html_list(b):
    out, seen = [], set()
    pat = re.compile(b["link_pattern"])
    for page in range(1, 12):
        try:
            html = get(b["url_template"].format(page=page), timeout=30).decode("utf-8", "ignore")
        except Exception:
            break
        links = pat.findall(html)
        if not links:
            break
        for path in links:
            if path in seen:
                continue
            seen.add(path)
            slug = path.split("/")[2] if path.count("/") >= 2 else path
            out.append({"title": slug.replace("-", " "), "url": b["base"] + path,
                        "location": path.split("/")[1] if path.count("/") >= 1 else "", "posted": ""})
    return out


def radancy(b):
    """Radancy/TalentBrew career sites (Takeda). Results come from /search-jobs/results as HTML."""
    out, seen = [], set()
    li = re.compile(r'<a href="(/job/[^"]+)"[^>]*>\s*<h2 class="title">([^<]+)</h2>\s*(?:<span class="location">([^<]*)</span>)?', re.S)
    for term in b.get("search_terms", [""]):
        for page in range(1, b.get("max_pages", 4) + 1):
            q = urllib.parse.urlencode({
                "ActiveFacetID": 0, "CurrentPage": page, "RecordsPerPage": 50, "Distance": 50,
                "RadiusUnitType": 0, "Keywords": term, "Location": b.get("location", ""), "ShowRadius": "False",
                "IsPagination": "False", "SortCriteria": 0, "SortDirection": 0, "SearchType": 5, "ResultsType": 0,
                "SearchResultsModuleName": "Search Results", "SearchFiltersModuleName": "Search Filters"})
            d = json.loads(get(f"{b['base']}/search-jobs/results?{q}", timeout=30, headers=BROWSER_UA))
            rows = li.findall(d.get("results", ""))
            if not rows:
                break
            for path, title, loc in rows:
                if path in seen:
                    continue
                seen.add(path)
                out.append({"title": htmllib.unescape(title).strip(), "url": b["base"] + path,
                            "location": htmllib.unescape(loc or "").strip(), "posted": ""})
    return out


def apple(b):
    """jobs.apple.com renders results into a hydration blob in the page HTML. The API ignores its query and
    location filters, so page through a location slug (e.g. massachusetts-state969) and filter titles locally."""
    out, seen = [], set()
    for loc in b.get("locations", [""]):
        for page in range(1, b.get("max_pages", 8) + 1):
            q = urllib.parse.urlencode({"location": loc, "sort": "newest", "page": page})
            html = get(f"https://jobs.apple.com/en-us/search?{q}", timeout=30).decode("utf-8", "ignore")
            m = re.search(r'__staticRouterHydrationData\s*=\s*JSON\.parse\((".*?")\);', html, re.S)
            if not m:
                break
            rows = json.loads(json.loads(m.group(1)))["loaderData"]["search"]["searchResults"]
            if not rows:
                break
            for j in rows:
                pid = j.get("positionId")
                if pid in seen:
                    continue
                seen.add(pid)
                locs = ", ".join(f"{l.get('city', '')} {l.get('stateProvince', '')}".strip() or l.get("name", "")
                                 for l in j.get("locations", []))
                out.append({"title": j.get("postingTitle", ""),
                            "url": f"https://jobs.apple.com/en-us/details/{pid}/{j.get('transformedPostingTitle', '')}",
                            "location": locs or "United States", "posted": j.get("postingDate", "")})
    return out


ADAPTERS = {"ashby": ashby, "greenhouse": greenhouse, "rippling": rippling,
            "workday": workday, "html-list": html_list, "radancy": radancy, "apple": apple}


# ---------------------------------------------------------------- matching

def best_match(role: str, jobs: list[dict]) -> tuple[dict | None, str]:
    """Match a tracker role to a board posting by normalised title.
    Returns (job, kind) where kind is 'exact', 'contains', or ''."""
    r = norm(role)
    for j in jobs:
        if norm(j["title"]) == r:
            return j, "exact"
    # tolerate a retitle that keeps the core words (e.g. "Clinical Operations" -> "Clinical Research Operations")
    rw = set(r.split()) - {"senior", "lead", "the", "of", "and", "a"}
    for j in jobs:
        jw = set(norm(j["title"]).split())
        if rw and len(rw & jw) / len(rw) >= 0.75:
            return j, "contains"
    return None, ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--record", action="store_true", help="write new relevant postings into seen_jobs.json")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    cfg = json.loads(CONFIG.read_text())
    seen_doc = json.loads(SEEN.read_text()) if SEEN.exists() else {"seen": {}}
    seen = seen_doc["seen"]
    seen_urls = set(seen) | {v.get("url", "") for v in seen.values()}
    tracker = list(csv.DictReader(open(TRACKER, newline="")))
    known_titles = {((norm(v.get("company", "")).split() or [""])[0], norm(v.get("title", "")))
                    for v in seen.values()}
    known_titles |= {((norm(r["company"]).split() or [""])[0], norm(r["role"])) for r in tracker}
    today = dt.date.today().isoformat()

    report = {"date": today, "boards": [], "liveness": [], "new": []}
    for b in cfg["boards"]:
        entry = {"company": b["company"], "board": b["board"], "ok": True, "openings": 0, "error": ""}
        try:
            jobs = ADAPTERS[b["board"]](b)
        except Exception as e:  # a board being down is a finding, not a crash
            entry.update(ok=False, error=f"{type(e).__name__}: {e}")
            report["boards"].append(entry)
            continue
        entry["openings"] = len(jobs)
        report["boards"].append(entry)

        # 1. liveness for tracked rows at this company
        for row in tracker:
            if norm(row["company"]).split()[0] != norm(b["company"]).split()[0]:
                continue
            if row["status"] not in LIVE_STATUSES:
                continue
            job, kind = best_match(row["role"], jobs)
            if job:  # a retitled tracked role is not a new role
                known_titles.add((norm(b["company"]).split()[0], norm(job["title"])))
            report["liveness"].append({
                "company": row["company"], "role": row["role"], "status": row["status"],
                "live": bool(job), "match": kind,
                "board_title": job["title"] if job else "", "board_url": job["url"] if job else "",
            })

        # 2. new relevant postings not yet seen (by URL, or by company + title under any URL)
        loc_ok = re.compile(b["include_locations"], re.I) if b.get("include_locations") else None
        # big employers (pharma) post hundreds of Director/Clinical reqs; 'title_include' narrows to Hassan's lanes
        title_ok = re.compile(b["title_include"], re.I) if b.get("title_include") else None
        co = norm(b["company"]).split()[0]
        for j in jobs:
            if not RELEVANT.search(j["title"]) or EXCLUDE.search(j["title"]):
                continue
            if loc_ok and not loc_ok.search(j["location"] or ""):
                continue
            if title_ok and not title_ok.search(j["title"]):
                continue
            if j["url"] in seen_urls or (co, norm(j["title"])) in known_titles:
                continue
            report["new"].append({"company": b["company"], **j})

    if args.record and report["new"]:
        for j in report["new"]:
            seen[j["url"]] = {"title": j["title"], "company": j["company"], "url": j["url"],
                              "first_seen": today, "fit": "low", "status": "new",
                              "portal": "employer-board", "note": "Found by tools/employer_boards.py; fit not yet assessed."}
        SEEN.write_text(json.dumps(seen_doc, indent=2, ensure_ascii=False))

    if args.json:
        print(json.dumps(report, indent=2))
        return

    print(f"Employer boards, {today}")
    for e in report["boards"]:
        print(f"  {e['company']:<24} {e['board']:<10} " + (f"{e['openings']} openings" if e["ok"] else f"FAILED: {e['error']}"))
    print("\nLiveness of tracked roles")
    for l in report["liveness"]:
        flag = "LIVE " if l["live"] else "GONE "
        extra = "" if l["match"] in ("exact", "") else f"  (board title now: {l['board_title']})"
        print(f"  {flag} {l['company']:<20} {l['role'][:58]:<58} [{l['status']}]{extra}")
    print(f"\nNew relevant postings not in seen_jobs.json: {len(report['new'])}" + ("  (recorded)" if args.record and report["new"] else ""))
    for j in report["new"]:
        print(f"  {j['company']:<20} {j['title'][:55]:<55} {j['location'][:24]:<24} {j['posted']}  {j['url']}")


if __name__ == "__main__":
    main()
