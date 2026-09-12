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

### Priority 2: Director-Level Healthcare Partnerships / Business Development

Added 2026-08-12 after evaluating WHOOP's "Director, Healthcare Product Partnerships" posting — Hassan's Beiwe Service Center (BSC) work (pricing/DUA/MOU negotiation across ~50 institutions, budgeting/revenue projections, RPAC-committee reporting) already functions at this level. This is a deliberate Director-level carve-out — see [[project-career-strategy-sequencing]] memory — distinct from the still-deferred Director/Head of *Product Strategy* search.

```
site:linkedin.com/jobs "Director" "Healthcare Partnerships" OR "Healthcare Product Partnerships" Boston OR remote
site:linkedin.com/jobs "Director" "Digital Health Partnerships" OR "Business Development" health Boston
"Director, Partnerships" OR "Director, Business Development" "digital health" site:oura.com OR site:whoop.com OR site:verily.com
site:linkedin.com/jobs "Director" "Academic Medical Center" partnerships digital health
```

### Priority 3: Digital Biomarker / Clinical Innovation (Pharma)

These match domain expertise in digital phenotyping, clinical research operations, and IRB/compliance.

```
site:linkedin.com/jobs "Digital Biomarker" OR "Digital Health Innovation" Boston OR remote
site:linkedin.com/jobs "Digital Health Product Owner" OR "Digital Strategy" Sanofi OR Takeda OR Amgen
"Digital Biomarker Operational Lead" OR "Digital Biomarker Innovation" site:sanofi.com OR site:takeda.com OR site:amgen.com
```

### Priority 4: Research Program Manager / Health Tech Adjacent

Adjacent roles Hassan could pivot into, given research operations and platform leadership background.

```
site:linkedin.com/jobs "Research Program Manager" health Boston
site:linkedin.com/jobs "Healthcare Innovation Strategy" OR "Connected Health" Boston OR remote
site:linkedin.com/jobs "Clinical Innovation Manager"
```

### Priority 5: Healthcare Strategy / Advisory (Broader Net)

Wider net for consulting/advisory roles in digital health and life sciences.

```
site:linkedin.com/jobs "Healthcare Advisory" OR "Life Sciences Strategy" Boston OR remote
site:linkedin.com/jobs "Healthcare Data & Analytics" OR "Clinical Transformation" KPMG OR BCG OR McKinsey
"Senior Associate" OR "Vantage Manager" "digital health" site:cvshealth.com OR site:bcg.com
```

### Priority 6: Venture Capital & VC Stepping Stones (Health-Tech)

Added 2026-08-21: health-tech VC is now Hassan's fastest, most-guaranteed route to his comp goal, actively and directly searched — not just flagged opportunistically when it surfaces elsewhere. Full context: `../../../venture_capital_path.md`. These do not need to touch product management to qualify — run this category independent of Priority 1-5 fit, not as a subset of it.

```
site:linkedin.com/jobs "Principal" OR "Venture Partner" OR "Platform" health tech venture capital
site:linkedin.com/jobs "EIR" OR "Entrepreneur in Residence" OR "Scout" healthcare venture
"Venture Partner" OR "Principal" OR "Platform" site:rockhealth.com OR site:406ventures.com OR site:defineventures.com OR site:oakhcft.com
site:linkedin.com/jobs "Corporate Venture" OR "Strategic Venture" health tech OR pharma
"Director" OR "Principal" "Ventures" site:cvshealth.com OR site:sanofi.com OR site:takeda.com OR site:amgen.com
site:linkedin.com/jobs "Strategy" OR "Operations" "Manager" health tech startup Series B OR "Series C" OR "Series D"
```

### Priority 7: Health Data / Real-World Data Platforms (Evidation-shaped)

Added 2026-09-12 when the search widened beyond wearables. Multimodal, individual-level, consented health data with research rigor. Runs in the default top-3 set alongside Priority 1 and 2 (it replaced Priority 3's slot in the default rotation; Priority 3 still runs on `broad`).

```
site:linkedin.com/jobs "Product Manager" "real-world data" OR "real world evidence" OR "health data platform"
site:linkedin.com/jobs "Product Manager" OR "Director" site:verily.com OR site:truveta.com OR site:datavant.com OR site:komodohealth.com OR site:flatiron.com OR site:tempus.com
site:linkedin.com/jobs "Product Manager" "patient-generated" OR "multimodal" health data
```

### Priority 8: Clinical AI with a Trust / Evaluation Problem (Wolters Kluwer-shaped)

Products where "is the model right, and how do we keep knowing" is the product question. health-agent is the credential.

```
site:linkedin.com/jobs "Product Manager" "clinical AI" OR "clinical decision support" OR "ambient" Boston OR remote
site:linkedin.com/jobs "Product Manager" "AI evaluation" OR "responsible AI" OR "human-in-the-loop" health
"Product Manager" OR "Director" site:abridge.com OR site:ambiencehealth.com OR site:nabla.com OR site:hippocraticai.com
```

### Priority 9: Research and Trial Infrastructure (Beacon-shaped)

The Beiwe Service Center work aimed at industry: decentralized-trial platforms, site networks, digital-endpoint vendors.

```
site:linkedin.com/jobs "Director" OR "Head of" "decentralized clinical trials" OR "site network" OR "digital endpoints"
site:linkedin.com/jobs "Product Manager" "clinical trial platform" OR "eCOA" OR "digital biomarker" Boston OR remote
```

### Priority 10: Applied AI Leadership at Boston Life-Sciences Companies (Kymera-shaped)

"First AI leader" and "AI strategy and applications" reqs at clinical-stage biotechs and AMCs. Runs on `broad`.

```
site:linkedin.com/jobs "Director" OR "Head of" "AI Strategy" OR "AI Applications" OR "AI Innovation" biotech OR pharma Boston OR Cambridge
site:linkedin.com/jobs "first" "AI" leader OR "enterprise AI" biotech Cambridge
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
