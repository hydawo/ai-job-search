# Search Queries for Job Scraper

<!-- SETUP: Customize these queries based on your skills, target roles, and location -->

## Installed portal CLIs (primary for `/scrape`)

`/scrape` discovers every portal skill under `.agents/skills/*/SKILL.md` and runs its CLI first. Installed CLIs: `linkedin-search` and `freehire-search` (country-agnostic). Danish portal demos (jobbank/jobdanmark/jobindex/jobnet-search) are also present in this fork but not relevant to a Boston-based search — ignore their results, or remove them with `/add-portal` cleanup if desired. You do **not** need a matching `site:` line below for `linkedin-search`/`freehire-search` to run.

The `site:` query templates in this file are the **WebSearch fallback** — for portals without a CLI, company career pages, or when a CLI fails.

## Search Sites

Primary:
- **linkedin.com/jobs** - LinkedIn job listings (filter: United States / Boston, MA); also covered by `linkedin-search` CLI
- **freehire-search CLI** - country-agnostic job board coverage

Secondary (company career pages via Google):
- Direct Google searches with `site:` filters for target companies (Oura, WHOOP, Verily, Apple, Sanofi, Takeda, Amgen, Boston Children's Hospital, Abridge)

## Query Categories

Queries are grouped by priority. Each query should be combined with location terms (Boston, MA / remote) where the site supports it.

### Priority 1: Senior/Staff Product Manager, Digital Health & Wearables

These match the strongest and most desired career direction.

```
site:linkedin.com/jobs "Senior Product Manager" "digital health" Boston
site:linkedin.com/jobs "Staff Product Manager" wearables
site:linkedin.com/jobs "Product Manager" "digital phenotyping" OR "digital biomarker"
"Senior Product Manager" OR "Staff Product Manager" site:oura.com OR site:whoop.com OR site:verily.com
```

### Priority 2: Digital Biomarker / Clinical Innovation (Pharma)

These match domain expertise in digital phenotyping, clinical research operations, and IRB/compliance.

```
site:linkedin.com/jobs "Digital Biomarker" OR "Digital Health Innovation" Boston OR remote
site:linkedin.com/jobs "Digital Health Product Owner" OR "Digital Strategy" Sanofi OR Takeda OR Amgen
"Digital Biomarker Operational Lead" OR "Digital Biomarker Innovation" site:sanofi.com OR site:takeda.com OR site:amgen.com
```

### Priority 3: Research Program Manager / Health Tech Adjacent

Adjacent roles Hassan could pivot into, given research operations and platform leadership background.

```
site:linkedin.com/jobs "Research Program Manager" health Boston
site:linkedin.com/jobs "Healthcare Innovation Strategy" OR "Connected Health" Boston OR remote
site:linkedin.com/jobs "Clinical Innovation Manager"
```

### Priority 4: Healthcare Strategy / Advisory (Broader Net)

Wider net for consulting/advisory roles in digital health and life sciences.

```
site:linkedin.com/jobs "Healthcare Advisory" OR "Life Sciences Strategy" Boston OR remote
site:linkedin.com/jobs "Healthcare Data & Analytics" OR "Clinical Transformation" KPMG OR BCG OR McKinsey
"Senior Associate" OR "Vantage Manager" "digital health" site:cvshealth.com OR site:bcg.com
```

## Location Filter

When evaluating results, verify the job location matches these constraints. **Hard constraint: no relocation.**
- Boston, MA and surrounding areas (Cambridge, Brookline, Somerville) - ideal, hybrid or on-site OK
- Fully remote (US-based) with <20% travel - acceptable
- Fully remote (US-based) with >=20% travel - borderline, flag for discussion with the candidate before applying
- Any role requiring relocation, or on-site outside the Boston area with no remote/hybrid option - too far / FAIL (deal-breaker)

## Date Filter

Only include jobs posted within the last 14 days, or with an application deadline that has not yet passed. If a posting date cannot be determined, include it but flag as "date unknown".

## Adapting Queries

If the user specifies a focus area, select queries from the matching category and also generate 2-3 custom queries for that focus. For example:
- "/scrape [focus_area]" -> relevant category queries + custom focus-specific queries
