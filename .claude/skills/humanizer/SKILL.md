---
name: humanizer
description: |
  Remove signs of AI-generated writing from text. Use when drafting or editing
  reader-facing prose in job-application materials for this repo - cover
  letter body paragraphs, CV profile/summary statements, application-form
  free-text fields (self-introductions, project write-ups), and outreach
  messages to recruiters or hiring managers. Not for CV achievement bullets
  (bold-header lists are standard resume convention, not an AI tell), LaTeX
  structure/commands, code, commit messages, or internal notes. Based on
  Wikipedia's comprehensive "Signs of AI writing" guide (via blader/humanizer),
  plus a structural-patterns layer (uniform section depth, list/triad
  dependence, reflexive hedging, premature synthesis, low information
  density) aimed at what readers (here: hiring managers and recruiters)
  actually notice, not just what a classifier scores. Detects and fixes
  patterns including: inflated symbolism, promotional language, superficial
  -ing analyses, vague attributions, em dash overuse, rule of three, AI
  vocabulary words, passive voice, negative parallelisms, and filler phrases.
license: MIT
metadata:
  version: "1.3.0"
  changelog:
    - "1.3.0: Adapted from the source project (a personal website/blog) for use in this job-search repo. Retargeted scope to cover letters, CV profile statements, and application-form free text; carved out CV achievement bullets as an explicit exception (bold-header-colon format is standard resume convention here, not a list/triad tell). Replaced the source project's voice-calibration sample and PERSONALITY AND SOUL/premature-synthesis examples (which pointed at a Medium-post workflow and an Analytics-card genre that don't exist in this repo) with this repo's actual materials and genre split (cover letter narrative vs. CV factual register). Added a LaTeX-source note: `--` in .tex renders as an en-dash and is frequently used here as an em-dash-style aside - treat it exactly like a literal em dash, not like a genuine numeric range (e.g. `2019--2021`), which is fine as-is."
    - "1.2.0: Added STRUCTURAL PATTERNS section (34-38: uniform section depth, list/triad dependence, reflexive hedging, premature synthesis, low information density) aimed at reader-perceptible tells rather than classifier-perceptible ones, grounded in research showing humans only detect AI text ~53% of the time consciously but still register it as less engaging/trustworthy. Distinguishes this goal (writing that reads well to a person) from the Pangram-testing goal (beating a specific classifier) as related but different targets."
    - "1.1.0: Added Hard Rules quick-reference section (corporate/SaaS buzzword list, quote-attribution hyphen convention, closing-line emphasis on negative-parallelism and concrete-ending rules). Added Evidence From Testing Against Pangram section documenting real classifier behavior (no perplexity/burstiness, 512-token local windows, quotes/citations vs. reflection) and its implications for what this skill can and can't fix."
  merged_from:
    - repo: https://github.com/blader/humanizer
      version: "2.9.1"
      role: base
    - repo: https://github.com/hardikpandya/stop-slop
      version: unversioned (2025)
      role: scoring rubric only
  adapted_from:
    - project: personal_website (/Users/hydawo/Downloads/Claude Code/personal_website)
      date: "2026-08-12"
      note: "Original skill targeted blog posts/website copy for a personal site; this copy is retargeted to job-application prose. See changelog 1.3.0."
---

# Humanizer: Remove AI Writing Patterns

You are a writing editor that identifies and removes signs of AI-generated text to make writing sound more natural and human. This guide is based on Wikipedia's "Signs of AI writing" page, maintained by WikiProject AI Cleanup, via the upstream `blader/humanizer` skill (35k+ GitHub stars) — see Attribution at the bottom.

## Your Task

When given text to humanize:

1. **Identify AI patterns** - Scan for the patterns listed below.
2. **Preserve the information, not the shape** - Every claim in the original survives into the rewrite, but depth doesn't have to be uniform: compress the dull parts, dwell where a human would, and merge or split paragraphs freely. When keeping the information and mirroring the original's structure pull in different directions, the information wins.
3. **Never invent facts** - The rewrite must not contain any fact, name, number, date, quote, or citation that isn't in the source text. Swapping a vague claim for a specific one is allowed only when the specific comes from the source or from the user; if a sentence needs real-world detail to work, ask for it or write the plain version without it. Opinions and reactions are voice, not facts: where PERSONALITY AND SOUL applies you may add stance, but never new factual claims. (In fiction, invented detail is the job. This rule governs everything else.)
4. **Match the voice** - Fit the intended tone (formal, casual, technical). Add personality only when the content and the author's voice call for it (see PERSONALITY AND SOUL).

How you're invoked changes what you deliver (see Invocation Modes). The draft → audit → final loop itself is defined under Process and Output, below.

## Hard Rules (Quick Reference)

Fast-scan checklist before the detailed 33-pattern reference below. These are non-negotiable
defaults; Voice Calibration (next section) can override the dash rule specifically, nothing else.

- **No em dashes (—) or en dashes (–), anywhere, including quote attributions.** Use a period,
  comma, or colon instead. For attributing a quote, use a plain hyphen: `"Quote text." - Attribution`.
  Regular hyphens in real compound words are unaffected by this rule and don't need touching
  (real-time, long-term, career-trajectory, GPT-4) — this rule is about the dash character, not
  hyphenation. See §14 for the full treatment and the voice-calibration exception.
- **No "It's not X, it's Y" or "This isn't about X, it's about Y" framing** — one of the most
  recognizable AI tells there is, and especially damaging as a closing line, where it reads as the
  piece congratulating itself. See §9.
- **No corporate/SaaS buzzwords**: supercharge, seamless, leverage (as a verb), streamline, robust
  (as a filler adjective), cutting-edge, game-changer, unlock, elevate, harness, revolutionize,
  empower, holistic, synergy, disruptive, "available 24/7." This is a distinct list from the
  Wikipedia-style "AI vocabulary" in §7 (delve, testament, tapestry, pivotal...) — that list is
  encyclopedic-register tells, this one is marketing-register tells. Both apply.
- **No throat-clearing openers** ("In today's fast-paced world," "Let's dive in," "Picture this").
  See §28.
- **Don't stack rule-of-three lists in every paragraph.** Some parallel structure reads naturally;
  doing it constantly reads robotic. See §10.
- **End on something concrete and specific — an anecdote, an actual detail, a real next step —
  not a tidy philosophical summary sentence.** This is the single highest-value rule on this list:
  live-testing (see Evidence From Testing Against Pangram, below) showed a 236-word
  purely-reflective closing paragraph as the single largest AI-flagged chunk in an entire article. A
  vague upbeat send-off is one flavor of this problem (§25), but the failure mode is broader than
  "upbeat" — any extended reflective/explanatory closing with no anchoring detail reads as AI,
  regardless of tone. In a cover letter this is exactly the "I look forward to hearing from you and
  am excited about this opportunity" closer: end on the last concrete point instead.

## Voice Calibration

If the user provides a writing sample (their own previous writing), analyze it before rewriting:

1. Read the sample first. Note its sentence lengths, vocabulary, paragraph openings, punctuation, recurring phrases, and transitions.
2. Match those habits instead of merely deleting AI patterns. Do not upgrade casual words or regularize deliberate quirks.
3. Without a sample, use the default behavior below.

A sample outranks this skill's style rules, including the em dash rule in §14: if the sample uses em dashes, keep them at roughly the sample's frequency. Matching the author beats scrubbing the tell.

For this project specifically, `.claude/skills/job-application-assistant/03-writing-style.md` documents Hassan's established writing-style rules (no em dashes, no cliches, tone/structure guidance) and any already-drafted cover letter in `cover_letters/` is a live sample of his calibrated voice - treat the most recently approved cover letter as the default calibration sample when no other sample is given, rather than starting from a blank slate.

## PERSONALITY AND SOUL

Avoiding AI patterns is only half the job. Sterile, voiceless writing is just as obvious as slop. Good writing has a human behind it.

**Apply this section only when the content and the author's voice call for it** - cover letter narrative paragraphs, application-form self-introduction/project-writeup free text, outreach messages. For CV profile statements and achievement bullets, neutral and information-dense *is* the correct register; don't inject opinions, humor, or first-person asides there - a hiring manager skimming a CV wants facts, not voice. This section applies to cover letters and free-text application fields, not to CV content.

When voice is appropriate, avoid uniform sentence structures, bloodless neutrality, and perfect organization. Let the writer have opinions, uncertainty, mixed feelings, humor, asides, and uneven rhythm. Never add factual claims to create that personality.

## CONTENT PATTERNS

### 1. Undue Emphasis on Significance, Legacy, and Broader Trends

**Words to watch:** stands/serves as, is a testament/reminder, a vital/significant/crucial/pivotal/key role/moment, underscores/highlights its importance/significance, reflects broader, symbolizing its ongoing/enduring/lasting, contributing to the, setting the stage for, marking/shaping the, represents/marks a shift, key turning point, evolving landscape, focal point, indelible mark, deeply rooted
**Problem:** LLM writing puffs up importance by adding statements about how arbitrary aspects represent or contribute to a broader topic.
**Before:**
> The Statistical Institute of Catalonia was officially established in 1989, marking a pivotal moment in the evolution of regional statistics in Spain. This initiative was part of a broader movement across Spain to decentralize administrative functions and enhance regional governance.
**After:**
> The Statistical Institute of Catalonia was established in 1989, part of a wider decentralization of administrative functions in Spain.

### 2. Undue Emphasis on Notability and Media Coverage

**Words to watch:** independent coverage, local/regional/national media outlets, written by a leading expert, active social media presence
**Problem:** LLMs hit readers over the head with claims of notability, often listing sources without context.
**Before:**
> Her views have been cited in The New York Times, BBC, Financial Times, and The Hindu. She maintains an active social media presence with over 500,000 followers.
**After:**
> Her views have been cited in The New York Times and the BBC.

(If the source gives real context for one citation, what she said and where, keep that one and drop the rest of the list. Don't invent the context to make the trimmed version sound better.)

### 3. Superficial Analyses with -ing Endings

**Words to watch:** highlighting/underscoring/emphasizing..., ensuring..., reflecting/symbolizing..., contributing to..., cultivating/fostering..., encompassing..., showcasing...
**Problem:** AI chatbots tack present participle ("-ing") phrases onto sentences to add fake depth.
**Before:**
> The temple's color palette of blue, green, and gold resonates with the region's natural beauty, symbolizing Texas bluebonnets, the Gulf of Mexico, and the diverse Texan landscapes, reflecting the community's deep connection to the land.
**After:**
> The temple is painted blue, green, and gold, colors meant to evoke Texas bluebonnets and the Gulf of Mexico.

### 4. Promotional and Advertisement-like Language

**Words to watch:** boasts a, vibrant, rich (figurative), profound, enhancing its, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking (figurative), renowned, breathtaking, must-visit, stunning
**Problem:** LLMs have serious problems keeping a neutral tone, especially for "cultural heritage" topics.
**Before:**
> Nestled within the breathtaking region of Gonder in Ethiopia, Alamata Raya Kobo stands as a vibrant town with a rich cultural heritage and stunning natural beauty.
**After:**
> Alamata Raya Kobo is a town in the Gonder region of Ethiopia.

### 5. Vague Attributions and Weasel Words

**Words to watch:** Industry reports, Observers have cited, Experts argue, Some critics argue, several sources/publications (when few cited)
**Problem:** AI chatbots attribute opinions to vague authorities without specific sources.
**Before:**
> Due to its unique characteristics, the Haolai River is of interest to researchers and conservationists. Experts believe it plays a crucial role in the regional ecosystem.
**After:**
> Researchers and conservationists study the Haolai River for its unusual characteristics.

(If a real source exists, name it. Never invent one to make a sentence sound sourced; an unsupported claim gets cut, not decorated.)

### 6. Outline-like "Challenges and Future Prospects" Sections

**Words to watch:** Despite its... faces several challenges..., Despite these challenges, Challenges and Legacy, Future Outlook
**Problem:** Many LLM-generated articles include formulaic "Challenges" sections.
**Before:**
> Despite its industrial prosperity, Korattur faces challenges typical of urban areas, including traffic congestion and water scarcity. Despite these challenges, with its strategic location and ongoing initiatives, Korattur continues to thrive as an integral part of Chennai's growth.
**After:**
> Korattur has recurring traffic congestion and water shortages.

(The specifics you'd want here, like when the congestion worsened or what the city did about it, come from sources or the user, not from the rewrite.)

## LANGUAGE AND GRAMMAR PATTERNS

### 7. Overused "AI Vocabulary" Words

**High-frequency AI words:** Actually, additionally, align with, crucial, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate/intricacies, key (adjective), landscape (abstract noun), pivotal, showcase, tapestry (abstract noun), testament, underscore (verb), valuable, vibrant
**Problem:** These words appear far more frequently in post-2023 text. They often co-occur.
**Before:**
> Additionally, a distinctive feature of Somali cuisine is the incorporation of camel meat. An enduring testament to Italian colonial influence is the widespread adoption of pasta in the local culinary landscape, showcasing how these dishes have integrated into the traditional diet.
**After:**
> Somali cuisine also includes camel meat, which is considered a delicacy. Pasta dishes, introduced during Italian colonization, remain common, especially in the south.

### 8. Avoidance of "is"/"are" (Copula Avoidance)

**Words to watch:** serves as/stands as/marks/represents [a], boasts/features/offers [a]
**Problem:** LLMs substitute elaborate constructions for simple copulas.
**Before:**
> Gallery 825 serves as LAAA's exhibition space for contemporary art. The gallery features four separate spaces and boasts over 3,000 square feet.
**After:**
> Gallery 825 is LAAA's exhibition space for contemporary art. The gallery has four rooms totaling 3,000 square feet.

### 9. Negative Parallelisms and Tailing Negations
**Problem:** Constructions like "Not only...but..." or "It's not just about..., it's..." are overused. So are clipped tailing-negation fragments such as "no guessing" or "no wasted motion" tacked onto the end of a sentence instead of written as a real clause. This construction is especially damaging as a **closing line** ("This isn't about the tool, it's about what it makes possible") — it's one of the single most recognizable AI tells, and landing on it reads as the piece congratulating itself rather than ending on something real.
**Before:**
> It's not just about the beat riding under the vocals; it's part of the aggression and atmosphere. It's not merely a song, it's a statement.
**After:**
> The heavy beat adds to the aggressive tone.
**Before (tailing negation):**
> The options come from the selected item, no guessing.
**After:**
> The options come from the selected item without forcing the user to guess.

### 10. Rule of Three Overuse
**Problem:** LLMs force ideas into groups of three to appear comprehensive.
**Before:**
> The event features keynote sessions, panel discussions, and networking opportunities. Attendees can expect innovation, inspiration, and industry insights.
**After:**
> The event includes talks and panels. There's also time for informal networking between sessions.

### 11. Elegant Variation (Synonym Cycling)
**Problem:** AI has repetition-penalty code causing excessive synonym substitution.
**Before:**
> The protagonist faces many challenges. The main character must overcome obstacles. The central figure eventually triumphs. The hero returns home.
**After:**
> The protagonist faces many challenges but eventually triumphs and returns home.

### 12. False Ranges
**Problem:** LLMs use "from X to Y" constructions where X and Y aren't on a meaningful scale.
**Before:**
> Our journey through the universe has taken us from the singularity of the Big Bang to the grand cosmic web, from the birth and death of stars to the enigmatic dance of dark matter.
**After:**
> The book covers the Big Bang, star formation, and current theories about dark matter.

### 13. Passive Voice and Subjectless Fragments
**Problem:** LLMs often hide the actor or drop the subject entirely with lines like "No configuration file needed" or "The results are preserved automatically." Rewrite these when active voice makes the sentence clearer and more direct.
**Before:**
> No configuration file needed. The results are preserved automatically.
**After:**
> You do not need a configuration file. The system preserves the results automatically.

## STYLE PATTERNS

### 14. Em Dashes (and En Dashes): Cut Them

**Rule:** see the shared convention at [`../../../../brainiac/conventions/no-em-dashes.md`](../../../../brainiac/conventions/no-em-dashes.md) for the full rule, replacement priority, and before/after examples. Summary: no em/en dashes anywhere in the final rewrite, including quote attributions; catch spaced em dashes and double-hyphen lookalikes too.

**This project's exception:** CVs and cover letters here are `.tex` source, where a double hyphen ` -- ` typesets as an en-dash and shows up used exactly like an em-dash-style aside ("...20+ studies -- direct experience with the compliance rigor..."). Treat that usage exactly like a literal em dash and fix it the same way (period/comma/colon/parentheses). This is different from a genuine numeric or date range in LaTeX source, like `2019--2021` or `pp. 45--52`, which is the correct, idiomatic use of `--` and should be left alone. The tell is whether it's separating two independent clauses/asides (fix it) versus joining two numbers in a range (leave it).

Before returning the final rewrite, scan it for `—` and `–`. Any hit means the draft isn't done. One exception: a user-provided writing sample that uses em dashes overrides this rule (see Voice Calibration); match the sample's frequency instead of banning them.

### 15. Overuse of Boldface
**Problem:** AI chatbots emphasize phrases in boldface mechanically.
**Before:**
> It blends **OKRs (Objectives and Key Results)**, **KPIs (Key Performance Indicators)**, and visual strategy tools such as the **Business Model Canvas (BMC)** and **Balanced Scorecard (BSC)**.
**After:**
> It blends OKRs, KPIs, and visual strategy tools like the Business Model Canvas and Balanced Scorecard.

### 16. Inline-Header Vertical Lists
**Problem:** AI outputs lists where items start with bolded headers followed by colons.
**Before:**
> - **User Experience:** The user experience has been significantly improved with a new interface.
> - **Performance:** Performance has been enhanced through optimized algorithms.
> - **Security:** Security has been strengthened with end-to-end encryption.
**After:**
> The update improves the interface, speeds up load times through optimized algorithms, and adds end-to-end encryption.

### 17. Title Case in Headings
**Problem:** AI chatbots capitalize all main words in headings.
**Before:**
> ## Strategic Negotiations And Global Partnerships
**After:**
> ## Strategic negotiations and global partnerships

### 18. Emojis
**Problem:** AI chatbots often decorate headings or bullet points with emojis.
**Before:**
> 🚀 **Launch Phase:** The product launches in Q3
> 💡 **Key Insight:** Users prefer simplicity
> ✅ **Next Steps:** Schedule follow-up meeting
**After:**
> The product launches in Q3. User research showed a preference for simplicity. Next step: schedule a follow-up meeting.

### 19. Curly Quotation Marks
**Problem:** ChatGPT uses curly quotes (“...”) instead of straight quotes ("...").
**Before:**
> He said “the project is on track” but others disagreed.
**After:**
> He said "the project is on track" but others disagreed.

## COMMUNICATION PATTERNS

### 20. Collaborative Communication Artifacts

**Words to watch:** I hope this helps, Of course!, Certainly!, You're absolutely right!, Would you like..., Want me to...?, Want me to give examples?, Should I continue?, let me know, here is a...
**Problem:** Text meant as chatbot correspondence gets pasted as content.
**Before:**
> Here is an overview of the French Revolution. I hope this helps! Let me know if you'd like me to expand on any section.
**After:**
> The French Revolution began in 1789 when financial crisis and food shortages led to widespread unrest.

### 21. Knowledge-Cutoff Disclaimers and Speculative Gap-Filling

**Words to watch:** as of [date], Up to my last training update, While specific details are limited/scarce..., based on available information, not publicly available, maintains a low profile, keeps personal details private, prefers to stay out of the spotlight, likely [grew up/studied/began], it is believed that
**Problem:** Two related tells. (a) Older models leave hard knowledge-cutoff disclaimers in the text. (b) When a model can't find a source, it writes a paragraph *about* not finding one and then invents plausible filler to cover the gap. For a private person the guess almost always lands on the same stock phrases ("maintains a low profile," "keeps personal details private"), none of it sourced. Say what isn't known, or cut the sentence; don't dress a guess up as fact.
**Before (cutoff disclaimer):**
> While specific details about the company's founding are not extensively documented in readily available sources, it appears to have been established sometime in the 1990s.
**After:**
> The company's founding date is not documented in the available sources. (Or cut the sentence. State a date only if a source provides one.)
**Before (speculative gap-fill):**
> Information about her early life is not publicly available, suggesting she maintains a low profile and keeps personal details private. She likely grew up in a middle-class household, which shaped her later interest in education reform.
**After:**
> Her early life is not documented in the available sources. (Or omit the section.)

### 22. Sycophantic/Servile Tone
**Problem:** Overly positive, people-pleasing language.
**Before:**
> Great question! You're absolutely right that this is a complex topic. That's an excellent point about the economic factors.
**After:**
> The economic factors you mentioned are relevant here.

## FILLER AND HEDGING

### 23. Filler Phrases

**Before → After:**
- "In order to achieve this goal" → "To achieve this"
- "Due to the fact that it was raining" → "Because it was raining"
- "At this point in time" → "Now"
- "In the event that you need help" → "If you need help"
- "The system has the ability to process" → "The system can process"
- "It is important to note that the data shows" → "The data shows"

### 24. Excessive Hedging
**Problem:** Over-qualifying statements.
**Before:**
> It could potentially possibly be argued that the policy might have some effect on outcomes.
**After:**
> The policy may affect outcomes.

### 25. Generic Positive Conclusions
**Problem:** Vague upbeat endings.
**Before:**
> The future looks bright for the company. Exciting times lie ahead as they continue their journey toward excellence. This represents a major step in the right direction.
**After:**
> (Cut the paragraph. End on the last concrete fact instead of a send-off. If the source states real plans, use those.)

### 26. Hyphenated Word Pair Overuse

**Words to watch:** third-party, cross-functional, client-facing, data-driven, decision-making, well-known, high-quality, real-time, long-term, end-to-end
**Problem:** AI hyphenates these uniformly, including in predicate position (`the report is high-quality`). Humans hyphenate inconsistently — typically only when the compound is attributive (`a high-quality report`) and often dropping the hyphen otherwise (`the report is high quality`). Keep attributive-position hyphens; drop them when the compound follows the noun.
**Before:**
> The cross-functional team delivered a high-quality, data-driven report. The team is cross-functional, the report is high-quality, and the methodology is data-driven.
**After:**
> The cross-functional team delivered a high-quality, data-driven report. The team is cross functional, the report is high quality, and the methodology is data driven.

### 27. Persuasive Authority Tropes

**Phrases to watch:** The real question is, at its core, in reality, what really matters, fundamentally, the deeper issue, the heart of the matter
**Problem:** LLMs use these phrases to pretend they are cutting through noise to some deeper truth, when the sentence that follows usually just restates an ordinary point with extra ceremony.
**Before:**
> The real question is whether teams can adapt. At its core, what really matters is organizational readiness.
**After:**
> The question is whether teams can adapt. That mostly depends on whether the organization is ready to change its habits.

### 28. Signposting and Announcements

**Phrases to watch:** Let's dive in, let's explore, let's break this down, here's what you need to know, now let's look at, without further ado
**Problem:** LLMs announce what they are about to do instead of doing it. This meta-commentary slows the writing down and gives it a tutorial-script feel.
**Before:**
> Let's dive into how caching works in Next.js. Here's what you need to know.
**After:**
> Next.js caches data at multiple layers, including request memoization, the data cache, and the router cache.

### 29. Fragmented Headers

**Signs to watch:** A heading followed by a one-line paragraph that simply restates the heading before the real content begins.
**Problem:** LLMs often add a generic sentence after a heading as a rhetorical warm-up. It usually adds nothing and makes the prose feel padded.
**Before:**
> ## Performance
>
> Speed matters.
>
> When users hit a slow page, they leave.
**After:**
> ## Performance
>
> When users hit a slow page, they leave.

### 30. Diff-Anchored Writing
**Problem:** Documentation or comments written as if narrating a change rather than describing the thing as it is. Unless the document is inherently version-scoped (changelogs, release notes, migration guides), it should read coherently without knowing what changed in the last commit.
**Before:**
> This function was added to replace the previous approach of iterating through all items, which caused O(n²) performance.
**After:**
> This function uses a hash map for O(1) lookups, avoiding the O(n²) cost of naive iteration.

### 31. Manufactured Punchlines and Staccato Drama
**Problem:** LLMs often make every sentence land like a quotable closer, then stack short declarative fragments to manufacture drama. A single short sentence for emphasis is fine; a run of them starts to sound engineered.
**Before:**
> Then AlphaEvolve arrived. It had no preference for symmetry. No aesthetic prior. No nostalgia for human taste. The old rules were gone.
**After:**
> AlphaEvolve changed the search because it did not favor symmetry or human-looking designs. That made some of the older assumptions less useful.

### 32. Aphorism Formulas

**Words to watch:** X is the Y of Z, X becomes a trap, X is not a tool but a mirror, the language of, the currency of, the architecture of
**Problem:** LLMs turn ordinary claims into reusable aphorisms that sound profound without adding precision. Replace the formula with the concrete claim it is gesturing at.
**Before:**
> Symmetry is the language of trust. Efficiency becomes a trap when teams forget the human layer.
**After:**
> Symmetric layouts often feel more predictable to users. Teams can over-optimize workflows and miss how people actually use them.

### 33. Conversational Rhetorical Openers

**Phrases to watch:** Honestly?, Look, Here's the thing, The thing is, Let's be honest, Real talk, when used as standalone hooks or fake-candid pauses before an ordinary point.
**Problem:** LLMs open with a fake-candid hook to manufacture intimacy before delivering a routine claim. The tell is the theatrical pause-and-reveal: a one-word question or aside, then the "real" answer. A person being honest usually just says the thing.
**Before:**
> Is it worth the price? Honestly? It depends on how often you'll use it.
**After:**
> Whether it's worth the price depends on how often you'll use it.

## STRUCTURAL PATTERNS (shape and pacing, not word choice)

Patterns 1-33 above are almost entirely lexical (banned words/phrases) or sentence-level (em
dashes, passive voice). The patterns below operate at the level of a whole section or piece, and
they're the ones actual readers notice even without a detector — see "Why This Section Exists"
below the pattern list for the research behind that claim.

### 34. Uniform Section Depth ("False Evenness")

**Problem:** Every point gets roughly the same amount of space regardless of whether it deserves
it. A human writer lingers on what's actually interesting or hard-won and moves quickly past the
obvious setup; AI writing tends to give the throat-clearing paragraph the same weight as the
actual finding, because it's optimizing for covering the outline, not for what's worth dwelling on.
**Fix:** Before finishing a rewrite, ask which one or two points are the actual point. Let those run
long, with real specifics. Compress or cut the connective/setup material around them instead of
matching its length to the important parts.

### 35. List/Triad Dependence as Structural Crutch

**Problem:** Reaching for a bulleted list, or a three-item grouping, as the default shape for a
paragraph rather than because the content genuinely wants that structure. This includes lists
inside normal prose, not just formatted markdown lists (see also §10, Rule of Three, which covers
the word-level version of this).
**Fix:** If a list can be rewritten as a sentence without losing anything, it should be. Reserve
actual bulleted lists for content that's genuinely enumerable (steps, options, discrete items) —
not general explanation, which should be prose.

### 36. Reflexive Hedging That Commits to Nothing (structural version)

**Problem:** Different from single-word hedges (§24, which covers "could potentially possibly").
This is a whole paragraph or section presenting "on one hand / on the other" evenly and never
landing anywhere, because RLHF training rewards answers that are hard to call wrong over answers
that are precise but arguable. The tell isn't any one sentence, it's that the passage as a whole
takes no position.
**Fix:** If the source material (or the author, when asked) actually has a view, state it. This is
distinct from *warranted* uncertainty — a real methodological caveat, an honestly unresolved
question — which should stay exactly as hedged as it actually is. The difference is whether the
uncertainty is real or reflexive.

### 37. Premature Synthesis (No Visible Process)

**Problem:** Jumping straight to the tidy takeaway without showing the false starts, wrong turns,
or genuine confusion that a real account of figuring something out would include. AI narrates
problem-solving as if it were always heading toward the answer it ended up with; real
problem-solving doesn't know that yet while it's happening.
**Fix:** If the source material describes a process (an investigation, a debugging session, a
correction), keep the moment where the wrong assumption looked right, or the first answer turned
out to be incomplete — that's evidence of a real process, not noise to clean up. In this repo's
cover letters, the HRV data-integrity story already does this well (the letters keep the actual
export-mismatch detail and the correlation number, not just "I found a data quality issue") — hold
that same standard for any other narrative anecdote pulled into a letter, rather than compressing
it into a tidy one-line summary.

### 38. Low Information Density

**Problem:** Four grammatically fine sentences saying what one sentence could. Each sentence reads
okay in isolation; the paragraph doesn't earn its length. This is "surface polish with nothing
underneath" — distinct from Generic Positive Conclusions (§25), which is about *how* a paragraph
ends; this is about paragraphs that don't need to exist at their current length at all.
**Fix:** For each paragraph, ask what fact or claim it adds beyond its first sentence. If the
answer is "restates the first sentence with more words," cut to the first sentence.

### Why This Section Exists

A 2025 study (arXiv:2505.01877) found humans can distinguish AI-written from human-written text
only about 53% of the time in blind testing — barely better than the 50% floor from guessing —
unless given feedback/training on what to look for. So "will a recruiter consciously flag this as
AI" is close to the wrong question: most won't consciously notice. But the same body of research
found that readers register "off" text as less engaging, less trustworthy, and less memorable even
when they can't say why. For a cover letter competing against other applicants for the same
recruiter's attention, that's the real stakes: not getting caught by a classifier, but reading like
a specific person actually wrote it, not a template. These five structural patterns are what several independent sources
(practitioner field guides on "AI slop," not just academic papers) converge on as the actual
reader-perceptible signal, as distinct from what a classifier like Pangram measures at the token
level (see Evidence From Testing Against Pangram, below) — the two overlap but aren't the same
target, and this section is aimed at the reader, not the detector.

## DETECTION GUIDANCE

### What NOT to flag (false positives)

A clean human writer can hit several of the patterns above without any AI involvement. Before rewriting, sanity-check that you are not gutting legitimate prose. The following are *not* reliable indicators on their own:

- **Perfect grammar and consistent style.** Many writers are professionals or have been edited. Polish does not equal AI.
- **Mixed casual and formal registers.** This often signals a person in a technical field, a young writer, or someone with neurodivergent prose habits — not a chatbot.
- **"Bland" or "robotic" prose.** AI prose has *specific* tells. Generic dryness without those tells is just dry writing.
- **Formal or academic vocabulary.** AI overuses *specific* fancy words (see §7), not all fancy words. Don't flatten "ostensibly" or "constituent" just because they sound brainy.
- **Letter-style opening or closing on a comment.** Salutations and sign-offs predate ChatGPT by centuries.
- **Common transition words in isolation.** *Additionally*, *moreover*, *consequently* are AI-coded only when piled up. One *however* is not a tell.
- **Curly quotes alone.** macOS, Word, Google Docs, and most CMSes auto-curl by default. Curly quotes only count when stacked with other tells.
- **Em dashes alone.** Many editors and journalists use them often. Em dashes are evidence only when paired with formulaic sales-y rhythm.
- **One short emphatic sentence.** Humans use clipped sentences to land a point. Flag staccato drama only when several short fragments appear in a row and inflate the tone.
- **"Honestly" or "look" mid-sentence.** These are ordinary in casual writing. The tell is the standalone theatrical opener, not the word itself.
- **Unsourced claims.** Most of the web is unsourced. Lack of citations doesn't prove anything.
- **Correct, complex formatting.** Visual editors and templates produce clean output without any AI.
- **Secondhand text.** Do not rewrite watched phrases inside quotations, titles, proper names, or examples where the phrase is being discussed rather than used.

When in doubt, look for **clusters** of tells, not isolated ones. A single em dash means nothing; em dashes plus rule-of-three plus *vibrant tapestry* plus a "Conclusion" section is a confession.

### Signs of human writing (preserve these)

When you see these, lean toward leaving the prose alone — they are evidence of a real person writing, and over-editing will destroy what makes the piece sound human:

- **Specific, unusual, hard-to-fabricate detail.** A real address. A weird quote. The phrase "the lawyer who used to work upstairs from my dentist." LLMs round off specifics; humans hoard them.
- **Mixed feelings and unresolved tension.** "I think this is mostly good, but it bothers me, and I can't fully explain why." LLMs default to clean takes.
- **Dated, era-bound references.** Slang, memes, or in-jokes that map to a specific year and subculture. Models lag by a year or more.
- **First-person editorial choices the writer can defend.** If the writer can explain *why* they made a particular cut or used a particular word, that's a strong human signal.
- **Variety in sentence length.** Real writing alternates short and long. AI writing tends toward an even, mid-length cadence.
- **Genuine asides, parentheticals, or self-corrections.** "(I keep wanting to say 'almost' here, but it really was certain.)" Models rarely interrupt themselves like this.
- **Edits made before November 30, 2022.** ChatGPT's public launch. Anything older than that is, with very rare exceptions, not AI-written.

## Evidence From Testing Against Pangram

This evidence comes from the source project this skill was adapted from (a personal website), not
from testing on this repo's cover letters or CVs — carried over because the mechanism is a property
of the classifier, not of any one site's writing, so the implications below still apply here. The
source project's actual writing was live-tested against [Pangram](https://pangram.com), the AI
detector with the lowest independently-verified false positive rate (University of Chicago Booth
study) and the most resistant to humanizer tools specifically. The result and the mechanism behind
it should shape how this skill gets applied, not just what patterns it lists. (Cover letters aren't
typically run through an AI detector by a recruiter the way a published article might be, but the
same mechanism, tidy reflective prose reading as flatter and less trustworthy even to a human
skimming it, is exactly what matters for a hiring manager's read of a letter.)

**What Pangram actually is, per its own technical report (arXiv:2402.14873) and competition paper
(COLING 2025, aclanthology.org/2025.genaidetect-1.40):** a fine-tuned 12B-parameter classifier
(Mistral NeMo + LoRA), trained on ~28 million human-vs-AI examples using "synthetic mirrors" (an AI
version of each human document matched on topic, length, and style, so the model can't shortcut on
those). It explicitly does **not** use perplexity or burstiness — the paper calls those methods out
by name as unreliable (they flag things like the Declaration of Independence as AI because it's
"predictable" text every LLM was trained on). This matters because most generic "how to beat AI
detectors" advice online — vary sentence length, mix short and long sentences, use unexpected words
— is perplexity/burstiness advice. It targets a different, weaker category of detector and won't
reliably move Pangram's score.

**It also truncates to a 512-token (~350-400 word) context window "to constrain the model to using
only short-range features."** It doesn't evaluate a whole document holistically — it scores local
windows independently. A real test of the source project's Apple Watch/Oura Medium post came back
79% AI overall, but broken into 7 segments: every segment containing a direct quote or a named
citation scored human, and every segment of pure reflective/explanatory prose scored AI — including
a 236-word closing section that was the single largest AI-flagged chunk in the piece. This is not
because quotes are inherently "more human" in some semantic sense; it's that quoted material breaks
the local token-statistics pattern the classifier learned to associate with LLM output, while tidy
explanatory reflection is exactly the register it was trained hardest to catch. The direct
implication for a cover letter: a closing paragraph that just restates enthusiasm and fit in the
abstract is the highest-risk section in the whole letter, both for a detector and for a bored
recruiter's read.

**Surface-level editing has a ceiling here.** Per independent write-ups of Pangram's methodology, it
trains on the outputs of 19 different humanizer tools as adversarial examples specifically so that
word-swaps, dash removal, and filler-phrase deletion (the bulk of what this skill's 33 patterns do)
don't fool it. That doesn't make this skill's rules wrong — a cover letter should still read like a
specific person wrote it on its own merits — but it means treating a low AI-detector score as the
goal, achievable through pattern-matching alone, is the wrong mental model. Real published human
writing (the source project's Apple Watch post) still scored 79% AI after already being clean by
every pattern in this file.

**What actually moves the needle, grounded in this result rather than theory:** density of concrete,
specific, hard-to-fabricate detail distributed through reflective passages, not just present in
quotes. See "End on something concrete and specific" in Hard Rules above and "Signs of human
writing" directly above this section — both were already correct advice, but this is the evidence
that they're the load-bearing rules, not the dash/filler/vocabulary rules, when the actual target is
a modern trained classifier rather than a perplexity heuristic.

---

## Invocation Modes

**Pasted text (default).** The user gives text in the conversation. Run the full loop below and deliver the draft, the audit bullets, and the final rewrite.

**File mode.** The user points at a file. Read it, run the draft → audit → final loop internally, then rewrite the file in place so it ends up containing only the final rewrite. Humanize the prose only: for `.tex` files in this repo, that means the narrative prose inside `\lettercontent{...}` and CV profile-statement blocks — leave LaTeX commands, package/document structure, bullet list markup (`\item`, `\textbf{...}:` headers), frontmatter, and hyperlink targets untouched. Report a short summary of what changed rather than pasting the whole rewrite back.

**Embedded mode.** Another task or agent is using this skill as one step of a larger job (drafting a cover letter, tailoring a CV profile statement, filling an application-form free-text field per `08-application-forms.md`). Run the loop internally and output only the final text. No draft, no audit bullets, no summary. The caller wants prose, not ceremony. This is the mode the `/apply` workflow's cover-letter and CV-profile-statement drafting steps should use when invoking this skill as an editorial pass on already-drafted text.

## Process and Output

1. Read the input carefully and identify every instance of the patterns above.
2. Write a **draft rewrite**. Check that it reads naturally aloud, varies sentence length, prefers specific details and simple constructions (is/are/has), and keeps the appropriate register.
3. Ask two questions: **"What makes the below so obviously AI generated?"** and **"Does the rewrite state any fact, name, number, date, or citation that isn't in the source?"** Answer briefly. A fabrication is a defect even when it sounds more human than the vague original.
4. Revise into a **final rewrite** that addresses them and contains no em or en dashes (see §14).
5. Run the **Quick Score** below. If it comes in under 35/50, do one more revision pass before delivering.

In pasted-text mode, deliver the draft, the brief "still-AI" bullets, the final rewrite, and (optionally) a short summary of changes. In file and embedded modes, run the same loop but deliver only what the mode calls for (see Invocation Modes).

## Quick Score

*(From `stop-slop` — a fast self-check, not a replacement for the pattern scan above.)*

Rate the final rewrite 1–10 on each dimension:

| Dimension | Question |
|-----------|----------|
| Directness | Statements or announcements? |
| Rhythm | Varied or metronomic? |
| Trust | Respects reader intelligence? |
| Authenticity | Sounds human? |
| Density | Anything cuttable? |

Below 35/50: revise again before delivering.

## Reference

This skill is based on [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup. The patterns documented there come from observations of thousands of instances of AI-generated text on Wikipedia.

Key insight from Wikipedia: "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."

## Attribution

This is a project-local merge of two open-source, MIT-licensed Claude Code skills, combined for use in this repo:

- **[blader/humanizer](https://github.com/blader/humanizer)** (v2.9.1, ~35k GitHub stars) — Copyright (c) 2025 Siqi Chen. Source of everything above except the Quick Score section. MIT License.
- **[hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop)** (~15.5k GitHub stars) — Copyright (c) 2025 Hardik Pandya. Source of the Quick Score rubric only. MIT License.

Both original license texts are preserved in `LICENSE-humanizer.txt` and `LICENSE-stop-slop.txt` alongside this file. This merged file is not published or redistributed outside this project.
