# /save-session - Commit, Push, and Persist Session Learnings

You are wrapping up a working session on this job search framework: commit and push whatever changed in the repo, then persist any durable facts from the conversation into Claude's cross-session memory system.

Invoking this command is itself the user's authorization to commit and push without asking again each time — don't re-confirm those two actions on every run. Still apply ordinary judgment: if something looks wrong (see the secret-scan check below), stop and flag it instead of proceeding.

Follow these steps in order.

---

## Step 1: Check What Changed

Run `git status --short` in the repo root. `.gitignore` already protects personal data (tailored CVs/cover letters, `job_search_tracker.csv`, compiled PDFs, everything under `documents/` except `README.md`), so anything git shows here is expected to be safe to version — but verify that assumption every run, don't just trust it blindly:

- **Secret-scan check:** before staging, scan the changed/untracked file list for anything that looks like a credential or secret (`.env`, `*credentials*`, `*secret*`, `*apikey*`, `*token*`, `*.pem`, `*.key`). If anything matches, stop, do not stage or commit it, and tell the user what you found instead of proceeding.
- If `git status --short` is empty, skip to Step 3 (there's nothing to commit, but memory may still need updating).

## Step 2: Commit and Push

1. Run `git diff --stat` (and `git diff` for smaller diffs) to understand what actually changed, not just which files.
2. Stage everything with `git add -A` (safe here because `.gitignore` is the safety boundary, verified in Step 1).
3. Write a commit message that reflects the actual substance of the session's changes (what changed and why, not a generic "update files"), following this repo's existing commit message style (see `git log --oneline -5` for tone/format). Sign off with:
   ```
   Co-Authored-By: Claude <noreply@anthropic.com>
   ```
4. Commit.
5. Push to `origin` on the current branch. If the push fails (no upstream configured, auth failure, diverged history), report the exact error to the user rather than retrying blindly or force-pushing.

## Step 3: Persist Session Learnings to Memory

Review the session for anything that meets the bar already defined in your standing memory-system instructions — durable facts about the user, feedback on how to do this work, project state that isn't obvious from the repo files themselves, or pointers to external systems. Common sources in this framework specifically:

- New or corrected facts about the candidate's goals, constraints, or preferences
- Corrections or confirmations the user gave about how you should draft CVs/cover letters/evaluations
- New external references discovered this session (a Notion database, a tracking sheet, a portal quirk)
- Material changes to what's tracked in `job_search_tracker.csv` worth a durable note (not the row-by-row data itself, which the CSV already owns)

Before writing anything new:
1. Read the existing `MEMORY.md` index and skim files that look related, so you update rather than duplicate.
2. Only write what isn't already captured durably in the repo's own files (`CLAUDE.md`, the skill files) — memory exists for what a *different* working directory or a session without this repo open still needs to know, not a copy of what's already in version control.
3. Follow the existing type conventions (user / feedback / project / reference) and the frontmatter format already used in this project's memory files.

If nothing from the session clears that bar, say so explicitly rather than writing a low-value memory just to have written one.

---

## Step 4: Report

Summarize what happened:

```
## Session saved

### Committed & pushed
[commit hash] "[commit message subject line]"
[N] files changed
Pushed to [remote]/[branch] — or: "Nothing to commit, working tree matched last push."

### Memory updated
- [New/updated memory file] — [one-line reason]
(or: "Nothing new met the bar for persistent memory this session.")
```
