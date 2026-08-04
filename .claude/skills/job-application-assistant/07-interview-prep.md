---
framework_version: 1.0.0
---

# Interview Preparation Guide

<!-- SETUP: STAR examples are personalized by running /setup based on your actual experience -->

## STAR Format

Structure answers as: **Situation** (context), **Task** (your responsibility), **Action** (what you did), **Result** (outcome).

Keep answers to 1-2 minutes. Be specific. End with what you learned or would do differently.

## Ready-Made STAR Examples

<!-- Populated by /setup from the master career profile document. S/T/A/R details need to be filled in with specifics (numbers, timelines) before relying on these in an interview. -->

### 1. Heartbeat Feature (Cross-functional product requirements definition)
**Source:** Harvard Chan / Beiwe Platform
**What happened:** Need for better visibility into whether participant data was being successfully collected and transmitted; worked with developers and data scientists to define requirements for a device/data-upload health-tracking system.
**S/T/A/R stub:**
- Situation: Researchers lacked visibility into device activity, data uploads, and platform health across 20+ active studies.
- Task: Define a system to track this reliably without adding burden to research teams.
- Action: Coordinated with developers and data scientists to translate the research need into product requirements; drove the feature from problem identification through implementation.
- Result: [Fill in — adoption across studies, reduction in data-loss incidents, etc.]
**Use for:** "Tell me about a time you identified a gap and built a solution", "product requirements definition", "cross-functional coordination"

### 2. SOGP GPS Imputation Coordination (Technical tradeoff decision-making)
**Source:** Harvard Chan / Beiwe Platform
**What happened:** Coordinated a parameter-change decision affecting processing time vs. measurement accuracy tradeoffs (including seed-setting for reproducibility) for a machine-learning GPS imputation model, without personally writing or deploying the code.
**S/T/A/R stub:**
- Situation: Biostatisticians maintained a Sparse Online Gaussian Process (SOGP) model for GPS imputation; a parameter change would trade off processing time against accuracy.
- Task: Make the tradeoff call as the product/platform lead between biostatisticians and engineering.
- Action: Evaluated the tradeoff with the team, including reproducibility considerations (seed-setting), and made the go/no-go decision.
- Result: [Fill in — what was decided, and what it enabled downstream]
**Use for:** "Tell me about a technical decision you made without being the engineer", "how do you work with data science teams", "technically fluent PM" questions

### 3. Beiwe Service Center Financial Operations (Cross-functional financial/operational management)
**Source:** Harvard Chan / Beiwe Service Center
**What happened:** Directs BSC operations, working with Financial Associates, the Associate Director of Finance, and central finance administrators biannually to adjust and report on the costing model.
**S/T/A/R stub:**
- Situation: BSC needed a sustainable costing model to serve external investigators as a SaaS-style offering within an academic institution.
- Task: Own the business-operations side of a scientific platform.
- Action: Worked biannually with finance stakeholders to adjust the costing model, produce financial reports, and identify funds for expansions.
- Result: [Fill in — growth in supported studies/collaborators, financial sustainability outcome]
**Use for:** "Tell me about a time you managed budget/financial operations", "business operations within a research/academic setting"

### 4. Co-Founding Phebe Health (Founder-level product ownership)
**Source:** Phebe Health (Feb 2020 - Dec 2023)
**What happened:** Co-founded a digital phenotyping startup; led product strategy/roadmap, built a phased funding waterfall and investor pitch deck with the CEO, and managed technical implementation of the Phebe Beiwe instance.
**S/T/A/R stub:**
- Situation: Early-stage startup needed to translate a research concept (digital phenotyping for behavioral health) into a fundable, buildable product.
- Task: Own product strategy end-to-end as co-founder and Head of Product.
- Action: Built the funding waterfall and pitch deck, partnered with a development firm (BrickAbove) to define a phased technical plan, ran beta testing, and built Tableau dashboards for participant/study metrics.
- Result: [Fill in — funding raised, studies onboarded, or reason for eventual close]
**Use for:** "Tell me about founder/0-to-1 experience", "how do you handle ambiguity", "startup product leadership"

### 5. Apple Watch HRV Discovery (Measurement validity / device skepticism / origin story)
**Source:** Personal self-directed digital health research, 2018-2021. [Full write-up](https://medium.com/@systemsnotsilos/i-exported-my-apple-watch-data-twice-it-didnt-match-dc4c8fb17cb3)
**What happened:** Exported the same historical 640-day HRV window from a personal Apple Watch twice, a year apart (Sept 2020, Apr 2021). Both exports were 97% complete, but the correlation between them was only 0.67 — proof Apple's algorithm had silently reprocessed historical values after the fact. Shared the finding with JP Onnela (Harvard biostatistician, developer of the Beiwe platform); it was covered by The Verge and 4 other outlets. Less than a year later, became Head of Platform for Beiwe — the same platform JP built.
**S/T/A/R stub:**
- Situation: Tracking personal Apple Watch HRV data purely out of curiosity, not for any formal study.
- Task: Noticed a re-export of the same historical window didn't match the original and needed to determine whether this was noise or a real data-integrity issue.
- Action: Compared the two exports systematically (97% completeness both times, r=0.67 correlation), documented the finding, and brought it to a credible outside expert (JP Onnela) rather than just posting about it.
- Result: Became a widely covered story (The Verge +4 outlets) demonstrating that proprietary wearable algorithms can silently rewrite historical data; directly led to the professional relationship and job that followed. This is the clearest available "why this field, why now" origin story — genuine curiosity that predates any job, not a resume-driven narrative.
**Use for:** "Tell me about a time you questioned an assumption", "measurement validity", "why wearables/digital health", "tell me about yourself" (strong opening anecdote), "why are you passionate about this industry"

<!-- Add more STAR examples as needed. Aim for 4-6 covering different competencies. -->

## Common Tough Questions

### "Why did you leave [previous company]?"
> [PREPARE YOUR ANSWER - be honest, forward-looking, no negativity about former employer]

### "You don't have [specific skill/experience]."
> [PREPARE YOUR ANSWER - acknowledge the gap, bridge to adjacent experience, show willingness to learn]

### "Where do you see yourself in 5 years?"
> [PREPARE YOUR ANSWER - show ambition aligned with the role's growth path]

### "What's your biggest weakness?"
> [PREPARE YOUR ANSWER - genuine weakness with concrete mitigation strategy]

### "Why this company specifically?"
> Customize per company. Must reference: specific projects, company values, market position, or team structure. Never give a generic answer.

## Questions You Should Ask Interviewers

### About the Role
- "What does a typical week look like in this role?"
- "What would success look like in the first 6 months?"
- "What's the biggest challenge the team is facing right now?"

### About the Team
- "How big is the team, and how do you divide work?"
- "What does the development/project lifecycle look like, from idea to production?"
- "How do you onboard new team members?"

### About Tech & Growth
- "What's your current tech stack for [relevant area]?"
- "Is there room to grow into more architectural or strategic decisions?"
- "How does the team stay current with new tools and methods?"

### About Culture (use these to prevent disappointment)
- "How would you describe the team culture?"
- "What does professional development look like here?"
- "Is there flexibility for remote/hybrid work?"
- "What's the balance between development/new projects and maintenance work?"
- "How would you describe the leadership style in this team?"
- "What do people who thrive here have in common?"

## Phone/Video Interview Tips
- Have STAR examples written out (use this file)
- Keep a glass of water nearby
- Smile when speaking (it changes your tone)
- Ask for clarification if a question is vague
- It's OK to take 5 seconds to think before answering
- End with: "Is there anything else you'd like to know about my background?"

## After the Application (Best Practice)

### Follow-Up Etiquette
- **Don't call to "stand out"** or to learn more about the role post-submission - this risks a negative impression
- If the employer specified a timeline, respect it and wait
- If no timeline was given and significant time has passed (2+ weeks), a brief call to ask about status is acceptable
- If you have genuinely new, relevant information to share, a short follow-up is fine

### Thank-You Notes
- When you receive any update (interview invitation, rejection, or status update), send a brief thank-you message
- Express appreciation for their time and the process
- Keep it short (2-3 sentences)

## Roleplay Guidelines
When the user asks for interview practice:
1. Ask which role/company to simulate
2. Start with easy warm-up questions ("Tell me about yourself")
3. Progress to role-specific technical questions
4. Include 1-2 behavioral questions using the competencies from the job posting
5. End with a tough question or curveball
6. After each answer, give brief feedback: what worked, what to sharpen
7. Suggest which STAR example would work best for each question
