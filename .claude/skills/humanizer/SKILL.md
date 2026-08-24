---
name: humanizer
description: |
  Remove signs of AI-generated writing from text. Use when drafting or editing
  reader-facing prose in job-application materials for this repo - cover
  letter body paragraphs, CV profile/summary statements, application-form
  free-text fields (self-introductions, project write-ups), and outreach
  messages to recruiters or hiring managers. Not for CV achievement bullets
  (bold-header lists are standard resume convention, not an AI tell), LaTeX
  structure/commands, code, commit messages, or internal notes.
license: MIT
metadata:
  version: "2.0.0"
  note: "This project's copy is a thin pointer, not the full skill. The full skill (all 38 patterns, hard rules, voice calibration, evidence section) is now consolidated in brainiac/skills/humanizer/SKILL.md and shared across all five workspace projects, so this project's genuine divergences (CV-bullet exemption, LaTeX dash handling) are folded in there as inline Project Notes instead of living in a separate drifting copy. See that file's changelog for the 2026-08-23 consolidation."
---

# Humanizer (pointer)

The full skill lives at [`../../../../brainiac/skills/humanizer/SKILL.md`](../../../../brainiac/skills/humanizer/SKILL.md). Read that file and follow it in full, including its Hard Rules, Voice Calibration, PERSONALITY AND SOUL, the 38 numbered patterns, Detection Guidance, Evidence From Testing Against Pangram, Invocation Modes, and Process and Output sections.

For this project specifically:

- Use the **ai_job_search** entry under "Project-Specific Calibration Samples" in the shared file's Voice Calibration section (`.claude/skills/job-application-assistant/03-writing-style.md` and the most recently approved cover letter in `cover_letters/`).
- Apply the **ai_job_search** entry under "Project Notes" in the shared file: CV achievement bullets are exempt from §16 and §35 (bold-header-colon format is standard resume convention, not an AI tell), and this project's `.tex` source gets the LaTeX-specific em-dash handling documented in §14 (`--` treated as a literal em dash for asides, left alone for genuine numeric/date ranges like `2019--2021`).
- Apply the PERSONALITY AND SOUL register split as written in the shared file: cover letter narrative and application free text get voice; CV profile statements and achievement bullets stay neutral and information-dense.
