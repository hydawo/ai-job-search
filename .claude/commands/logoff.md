End-of-session wrap-up: compile, persist durable memory, commit/push, write a handoff file.

**Usage:** `/logoff`

Read [`../shared_context/session_close.md`](../shared_context/session_close.md) first — this file implements that shared four-phase contract with this project's specifics. (Replaces the former `/save-session` — same git/memory behavior, now also compiles a summary and writes a handoff file.)

Invoking this command is itself the user's authorization to commit and push without asking again each time — don't re-confirm those two actions on every run. Still apply ordinary judgment: if something looks wrong (see the secret-scan check below), stop and flag it instead of proceeding.

---

## Phase 1 — Compile the session

Review the full conversation for: which job postings were evaluated, which CVs/cover letters were drafted or revised (and for which company/role), interview prep done, and any decisions Hassan made about targeting or strategy. Keep it to a short plain-language summary — this feeds both the git commit message and the handoff file, not a separate deliverable.

## Phase 2 — Persist durable facts to memory

Common sources in this project specifically:
- New or corrected facts about the candidate's goals, constraints, or preferences
- Corrections or confirmations Hassan gave about how to draft CVs/cover letters/evaluations
- New external references discovered this session (a Notion database, a tracking sheet, a portal quirk)
- Material changes to what's tracked in `job_search_tracker.csv` worth a durable note (not the row-by-row data itself, which the CSV already owns)

Before writing anything new:
1. Read the existing `MEMORY.md` index and skim files that look related, so you update rather than duplicate.
2. Only write what isn't already captured durably in `CLAUDE.md` or the skill files.
3. Follow the existing type conventions (user / feedback / project / reference).

If nothing from the session clears that bar, say so explicitly rather than writing a low-value memory just to have written one.

## Phase 3 — Git commit and push

Run `git status --short`. `.gitignore` already protects personal data (tailored CVs/cover letters, `job_search_tracker.csv`, compiled PDFs, everything under `documents/` except `README.md`), so anything git shows here is expected to be safe to version — but verify that assumption every run, don't just trust it blindly.

- **Secret-scan check:** before staging, scan the changed/untracked file list for anything that looks like a credential or secret (`.env`, `*credentials*`, `*secret*`, `*apikey*`, `*token*`, `*.pem`, `*.key`). If anything matches, stop, do not stage or commit it, and tell the user what you found instead of proceeding.
- If `git status --short` is empty, skip to Phase 4 (there's nothing to commit, but memory and the handoff may still be worth writing).
- `git diff --stat` (and `git diff` for smaller diffs) to understand what actually changed, not just which files.
- Stage everything with `git add -A` (safe here because `.gitignore` is the safety boundary, verified above).
- Write a commit message reflecting the actual substance of the session's changes, following this repo's existing commit style (`git log --oneline -5`). Sign off with `Co-Authored-By: Claude <noreply@anthropic.com>`.
- Commit, then push to `origin` on the current branch. If the push fails (no upstream, auth failure, diverged history), report the exact error rather than retrying blindly or force-pushing.

## Phase 4 — Session handoff file

Write `.claude/session-logs/YYYY-MM-DD-HHMM.md` (create the folder if needed): what was accomplished, decisions made, open threads (e.g. "cover letter for X drafted but not verified"), and concrete next steps for whoever opens the next session here.

---

## Report

```
## Session saved

### Committed & pushed
[commit hash] "[commit message subject line]"
[N] files changed
Pushed to [remote]/[branch] — or: "Nothing to commit, working tree matched last push."

### Memory updated
- [New/updated memory file] — [one-line reason]
(or: "Nothing new met the bar for persistent memory this session.")

### Handoff
Saved to `.claude/session-logs/[file].md`
```
