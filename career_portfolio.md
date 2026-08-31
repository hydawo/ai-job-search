# Career Portfolio

**This file is permanent — do not retire, delete, or fold into another mechanism without migrating every entry's full content first, verified, not just linked.** That's the exact mistake that happened to this file's predecessor (see history below): it got retired on the assumption that the underlying source material covered everything, and the resume-specific framing layer was lost because nothing actually checked that assumption at the time. If this file's role ever needs to change, treat that as a real migration with the same verification rigor as any other, not a quick redirect.

Pre-digested career framing for real work done across the workspace — skills tags, draft resume bullets, and verification notes for using each one in an application. This file is `ai_job_search`'s own material, not shared: it's this project's interpretation of facts that live in `../brainiac/writeups/` for its own specific purpose (CV/cover letter/interview material), not a shared fact itself. The underlying findings/narrative are the source of truth in the linked writeup; this file exists so that translation work doesn't have to be redone from scratch every application cycle.

**History:** originally `shared_context/career_portfolio.md`, a shared hub file all five workspace projects read/wrote. Retired 2026-08-13 in favor of `ai_job_search` reading `brainiac/writeups/` directly — that migration silently dropped the resume-bullet framing layer, since writeups aren't written in that register. Restored 2026-08-17 as `ai_job_search/career_achievements.md` (this project's own file, not shared, per the same ownership test the rest of the workspace follows), then renamed to `career_portfolio.md` the same day to keep the original, familiar name and mark it as the permanent, primary source — not a temporary bridge.

**Entries here are source material, not pre-approved copy.** Verify scope/numbers with Hassan before quoting any of this externally, same as any other claim.

---

## 2026-08-12 — Beiwe platform-wide usage/retention dashboard
**Source:** `beiwe_platform_metrics`
**Full story:** [`../brainiac/writeups/beiwe_platform_metrics/dashboard-and-completeness-methodology.md`](../brainiac/writeups/beiwe_platform_metrics/dashboard-and-completeness-methodology.md)
**What:** Built an interactive HTML dashboard plus a Python data pipeline (API pulls, local aggregation, retention-milestone calculation) covering usage, data-completeness, and retention metrics across ~440 Beiwe studies, aggregating tens of millions of rows of per-participant-daily data volume.
**Skills demonstrated:** Data pipeline design at scale, API integration, Python (pandas), dashboard/data-viz development, platform-level analytics for a research-grade digital health system.
**Draft bullet:** *"Designed and built an end-to-end analytics pipeline and interactive dashboard tracking usage, completeness, and retention across ~440 studies on a research digital-phenotyping platform (Beiwe), processing millions of participant-level data-volume records."*
**Needs verification before external use:** exact study count and row counts at time of the specific application; whether platform name ("Beiwe") is appropriate to name given the target employer.
**Last checked:** 2026-08-12

---

## 2026-07-03 to 2026-07-08 — Odin/Asgard: multi-agent AI operations system
**Source:** `bsc_assistant` (desktop shell: `odin-app`)
**Full story:** [`../brainiac/writeups/bsc_assistant/odin-asgard-writeup-draft.md`](../brainiac/writeups/bsc_assistant/odin-asgard-writeup-draft.md) — six agents (Hermes/email, Saga/CRM, Heimdall/RA-tracking, Hephaestus/platform-eng, Fortuna/finance, Odin/briefing synthesis), Electron desktop shell, MCP-connected to live production systems, built cross-agent by design so one real-world event updates every relevant agent once. Built in a single ~400-turn session spanning July 3–8, 2026, refined since.
**Skills demonstrated:** End-to-end AI agent system design (architecture, state, cross-agent coordination — not just prompting), MCP-based tool integration across five+ production systems, Electron desktop app development, product thinking applied to internal tooling, sustained execution on a large multi-day build.
**Draft bullet:** *"Designed and built a six-agent AI operations system for a Harvard research service center — integrating email, CRM, GitHub, Slack, and calendar via MCP connectors behind a custom desktop application — that automates cross-functional workflows and keeps them synchronized without manual reconciliation."*
**Needs verification before external use:** confirm what's safe to name externally (institution, "Beiwe Service Center" / "Odin" / "Asgard" naming), and confirm the six-agent count and MCP-connector framing are still accurate at time of application (this system is actively evolving).
**Last checked:** 2026-08-13

---

## 2026-08-12 — Personal health-data analytics practice (multi-year, wearables + passive-sensing)
**Source:** `health_data_analytics`
**Full story:** three of the six existing writeups carry the strongest distinct skill signal — [`apple-health-vs-oura-comparison.md`](../brainiac/writeups/health_data_analytics/apple-health-vs-oura-comparison.md) (device-agreement validation: Pearson r, Lin's CCC, Bland-Altman, mixed-effects models, ~20 rounds of methodological correction), [`communication-vs-physiological-stress.md`](../brainiac/writeups/health_data_analytics/communication-vs-physiological-stress.md) (catching a real data-coverage bug and a shared-drift confound before they became false findings, then tracing a mechanism — late-night texting delaying bedtime — across two independent devices), and [`sleep-inference-from-communication-silence.md`](../brainiac/writeups/health_data_analytics/sleep-inference-from-communication-silence.md) (a negative-result validation of a passive-sensing sleep-proxy technique, explicitly relevant to digital-phenotyping/Beiwe-style research, not just personal curiosity). The other three writeups (`ramadan-health-effects.md`, `ramadan-sociability.md`, `wear-time-coverage-apple-vs-oura.md`) mostly reinforce the same methodology rather than adding new skill signal, so they're not separately logged here.
**Skills demonstrated:** Rigorous statistical validation methodology applied independently (concordance correlation, Bland-Altman, mixed-effects modeling), catching and correcting real data-quality bugs and statistical confounds before they became false conclusions rather than after, causal-mechanism tracing rather than stopping at correlation, and — via the sleep-inference piece specifically — applied passive-sensing/digital-phenotyping methodology validation that connects directly to the professional Beiwe-platform domain.
**Draft bullet:** *"Independently conducted multi-year statistical analysis of wearable and passive-sensing data (1,000+ paired daily observations across two devices), applying rigorous validation methodology and catching multiple data-quality confounds before they produced false findings, including a negative-result study on communication-based sleep inference directly relevant to digital-phenotyping research methods."*
**Resolved 2026-08-26:** Hassan confirmed this belongs in cover letters (Oura New Experiences letter first) — brief mention only, at most one value (no correlation coefficients or other stats notation, consistent with [[feedback-application-narrative]]'s existing "no stats notation" rule), deeper findings (e.g. the RHR measurement-window correction) saved for interview conversation rather than written out. Standard phrasing landed: "...and more recently ran a two-year, 1,000-plus-day statistical comparison of my own Apple Watch and Oura data." Reuse this pattern for future WHOOP/Oura letters rather than re-deriving depth/framing each time.
**Last checked:** 2026-08-26

---

## 2026-08-18 — HeartBeat feature and Beiwe tenure-long platform metrics
**Source:** `beiwe_platform_metrics` (`heartbeat_feature_career_qa.md`, `platform_improvement_highlights.md` — not yet in `brainiac/writeups/`, session-produced Q&A files)
**What:** Directed the build of HeartBeat, a device check-in/re-engagement feature (implemented by an engineer, Eli, under Hassan's direction) that restores background data collection after a device drops out. Rigorous participant-level analysis (Welch's t-test) isolated the feature's effect from an unrelated 2023 Android regression.
**Verified numbers (see project memory `project_beiwe_heartbeat_feature.md` / `project_beiwe_tenure_metrics.md` for full detail and sourcing):**
- HeartBeat specifically: **+7-8 percentage points** platform-wide data-completion (participant-level +7.3pt, 95% CI [5.3,9.3], p≪0.001), isolated from the dip.
- Simple tenure-long framing (Mar 2022 arrival → Jun 2026): **+10.3 percentage points** (83.24% → 93.57%), no trend-fitting.
- Scale framing: **82.7% of all data the platform has ever collected** (30.05 TB of 36.36 TB, 2014-2026) happened during this ~4.5-year tenure.
**Skills demonstrated:** Product decision-making with measurable outcome, cross-functional direction of an engineer's build (not hands-on implementation), rigorous before/after statistical framing, honest handling of a confounding factor (the Android regression) rather than taking credit for the naive trough-to-peak number.
**Draft bullet:** *"Directed the build of HeartBeat, a device re-engagement feature that lifted platform-wide data-collection completion by 7-8 percentage points (statistically tested, p<0.001), contributing to a tenure-long rise of 10.3 points and an all-time platform record."*
**Priority ranking (Hassan's call, 2026-08-18):** the 82.7%-of-all-data stat and the HeartBeat +7-8pt stat are the two strongest, default-use points (quantified *and* attributable to a specific decision). The all-time-record stat and raw scale/footprint numbers (63 studies, 3,918 participants, 29.65 TB) are supporting detail only — include only when a specific posting's requirements make them directly relevant, never as filler.
**Needs verification before external use:** say "directed the build of," never "built" (Eli did the implementation). Say "percentage points," never "%" (a 20-point-style claim would misstate this). Source files aren't yet migrated into `brainiac/writeups/` — check there first for an updated/canonical version before reusing.
**Last checked:** 2026-08-18

---

*(Add new entries above this line, newest first, whenever a vault writeup gets translated into career framing. Update `Last checked` when re-verifying an existing entry.)*
