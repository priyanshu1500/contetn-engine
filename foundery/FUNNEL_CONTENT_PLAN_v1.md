# Funnel Content Plan v1 — TOFU / MOFU / BOFU scripts

Written 2026-09-22. Six new episode scripts in the established cue-by-cue format
(see `demos/ep-003-creative-velocity-engine/SCRIPT.md` for the reference shot list
style). All follow `docs/SCRIPT_FORMULA.md` (the 8-beat persuasion skeleton) and
`brand.md` (locked palette, Node, CTA rules). None of these are built yet —
each needs a real automation behind it (or a real client result) before the
numbers go from `[PLACEHOLDER]` to final. **Never publish a placeholder number
as if it were real** — that breaks the brand's core credibility rule.

## Why a funnel, not one format repeated

Right now `_ideas.md` only has one register: proof-of-work demos (MOFU). That
converts warm viewers but does nothing to *create* warm viewers at scale, and
nothing to *close* the ones who are already sold but haven't booked. A funnel
fixes both gaps:

| Stage | Job | Viewer state | Format | Primary CTA |
|---|---|---|---|---|
| **TOFU** | Get seen by the ICP at volume; plant the "I'm bleeding money on this" thought | Doesn't know they have this problem, or doesn't know it's solvable | Pattern-interrupt + pain framing, industry-wide, NO specific automation demo | Low-friction: comment for a free checklist/list |
| **MOFU** | Prove you can actually build it | Knows the problem, is evaluating whether AI automation is real or hype | Full proof-of-work demo (your existing ep-001/002/003 format) | Medium: comment for the workflow breakdown |
| **BOFU** | Convert intent into a booked call | Already believes it works, is deciding whether to act now / with you | Direct offer, ROI math, objection handling | High: book a call / DM to scope their build |

**Sequencing in practice:** TOFU episodes run broad (all three markets, all four
ICP verticals) to maximize reach. MOFU episodes run narrower, one vertical at a
time, and get retargeted to anyone who watched a TOFU video >50%. BOFU episodes
are for commenters/DMs from MOFU episodes and for retargeting — they're not
built to go viral, they're built to close, so don't judge them on view count.

**Cadence suggestion:** 2 TOFU : 2 MOFU : 1 BOFU per week if you're posting
daily. TOFU carries reach, MOFU carries trust, BOFU carries revenue — don't
cut BOFU because it underperforms on views, that's not its job.

---

# TOFU — awareness / pain-recognition

## T1 — "The 40-Hours-a-Week Ghost Employee"

**Target:** broad ICP (any owner paying manual labor for a repeatable process).
**Runtime:** ~20s (TOFU should be short — pattern-interrupt, not a pitch).
**CTA:** `Comment "AUDIT"` → send a free 5-minute process-audit checklist (a real lead magnet, not a fake one — build this once, reuse forever).

### Cue-by-cue
**Cue 1 — THE HOOK (0.0s–4.0s)**
- Header pill: `✦ THE GHOST EMPLOYEE ON YOUR PAYROLL`
- VO: "You have a full-time employee whose entire job is copy-paste. You've never met them. You still pay them $[PLACEHOLDER: avg. fully-loaded admin salary/hr] an hour."
- Visual: dark container stage, a payroll line item redacting to `[REDACTED] — Data Entry` while a clock spins.
- Mascot: `node-thinking`. SFX: cash-register-ish tick, unsettling not fun.

**Cue 2 — THE REVEAL (4.0s–10.0s)**
- Header pill: `✦ IT'S YOU. AND YOUR TEAM.`
- VO: "It's every hour your team spends re-typing a lead into a spreadsheet. Copying a booking from one tab to another. Chasing a follow-up you already promised."
- Visual: three quick evidence-card snapshots — email → spreadsheet, calendar → calendar, "Following up!" text draft — each stamped `MANUAL`.
- Mascot: `node-pointing` at each card in turn.

**Cue 3 — THE ADOPTION GAP (10.0s–15.0s)**
- Header pill: `✦ YOUR COMPETITOR ALREADY FIRED THEIRS`
- VO: "[PLACEHOLDER: verify a real, citable stat — e.g. 'X% of small businesses in your industry' already run this on autopilot]. The rest are still doing it by hand and calling it 'just how it works here.'"
- Visual: two-panel split — dim/manual side vs. bright/automated side, both same industry icon.
- Mascot: `node-working` (dim side) mirrored by a static automated icon (bright side, no Node — Node only represents the manual grind here, deliberately).

**Cue 4 — THE CTA (15.0s–20.0s)**
- Header pill: `✦ FREE 5-MIN PROCESS AUDIT`
- VO: "Comment 'AUDIT' and I'll send you the checklist we use to find exactly which of your hours are ghost hours."
- Visual: Node celebrating, holding a checklist card.
- SFX: light confetti-pop, restrained (TOFU shouldn't feel like a full sales close).

**Fact-check before publishing:** replace both placeholders with sourced, specific numbers (per Beat 2 of `SCRIPT_FORMULA.md`: precise beats round). Do not publish a guessed percentage.

---

## T2 — "5 Jobs You're Still Paying a Human to Do"

**Target:** broad ICP, listicle format (high rewatch/save rate).
**Runtime:** ~25s.
**CTA:** `Comment "LIST"` → send the full 12-item list as a lead magnet (give more than the 5 shown, standard listicle over-delivery).

### Cue-by-cue
**Cue 1 — HOOK (0.0s–3.5s)**
- Header pill: `✦ 5 JOBS AI ALREADY DOES BETTER`
- VO: "Five jobs businesses are still paying a human to do — that a system already does for less, without complaining about Mondays."
- Mascot: `node-idea`.

**Cue 2 — THE LISTICLE (3.5s–17.5s)** — one verb+object item every ~2.8s, no adjectives (Beat 5 of the formula), each a fresh evidence-card:
1. "Qualify inbound leads before a human ever replies."
2. "Chase no-shows and rebook them automatically."
3. "Turn a missed call into a text conversation in under 10 seconds."
4. "Build the weekly report nobody wants to build."
5. "Screen the first round of resumes overnight."
- Visual: one card per item, consistent icon-left/verb-right layout, UI layer only — perfectly static (per `DESIGN_PHILOSOPHY.md`'s two-layer rule), no camera drift on these, they're flat vector UI.

**Cue 3 — THE MOAT LINE (17.5s–21.5s)**
- Header pill: `✦ NOT LATER. NOW.`
- VO: "This isn't 'the future of work.' It's Tuesday, for the businesses already running it."
- Mascot: `node-pointing`.

**Cue 4 — CTA (21.5s–25.0s)**
- VO: "Comment 'LIST' and I'll send you the other seven."
- Mascot: `node-celebrating`.

---

# MOFU — proof-of-work (full demo)

## M1 — "The Recruiter Who Stopped Reading Resumes"

**Target:** recruiting / staffing agencies and internal talent teams.
**Runtime:** ~40s, full 8-beat structure.
**Automation to actually build before publishing:** inbound resume → AI screens against the job spec → ranks + summarizes top candidates → auto-schedules a screening call with the top N, drops the rest a courteous auto-reply. (If this doesn't exist yet, this script is the brief for it — build first, then film; never demo a fake workflow.)
**CTA:** `Comment "SCREEN"` → workflow breakdown.

### Cue-by-cue
**Cue 1 — HOOK + THE CRASH (0.0s–4.5s)**
- Progress bar: Start.
- Header pill: `✦ 340 RESUMES. ONE OPEN ROLE.`
- VO: "A recruiter opened one job posting and got 340 resumes in four days. She read the first sixty. She never saw the other two-eighty — including, probably, the best one."
- Visual: inbox counter climbing `12 → 88 → 340`, then flatlining with a "not read" badge.
- Mascot: `node-thinking`.

**Cue 2 — THE BOTTLENECK (4.5s–12.0s)**
- Header pill: `✦ THE 6-MINUTE-PER-RESUME WALL`
- VO: "Reading and scoring one resume properly takes six minutes. At 340 resumes, that's 34 hours — more than a full work week — before a single interview is booked."
- Visual: a `34 HOURS` counter building, stacked against a `1 WEEK` calendar strip.
- Mascot: `node-working`.

**Cue 3 — STEP 1: THE SCREENING AGENT (12.0s–22.0s)**
- Progress bar: Level 1.
- Header pill: `✦ STEP 01 / SCREEN & RANK, OVERNIGHT`
- VO: "The system reads every resume against the actual job spec, scores it, and ranks the top candidates by fit — not by who applied first."
- Visual: resume stack feeding into a scanner, ranked list populating `#1, #2, #3...` with match-percentage badges.
- Mascot: `node-idea`. SFX: scanner whir + soft ticks per rank.

**Cue 4 — STEP 2: THE AUTO-SCHEDULE (22.0s–30.0s)**
- Progress bar: Level 2.
- Header pill: `✦ STEP 02 / BOOKS THE CALL ITSELF`
- VO: "Top candidates get a scheduling link automatically. Everyone else gets a real, courteous reply — same day, not three weeks of silence."
- Visual: calendar auto-filling with 3 booked slots; a polite decline message stamped `SENT`.
- Mascot: `node-running`.

**Cue 5 — THE PROOF (30.0s–35.0s)**
- Header pill: `✦ [PLACEHOLDER: REAL BEFORE/AFTER FROM YOUR BUILD]`
- VO: "[PLACEHOLDER: e.g. '34 hours of screening → 20 minutes of reviewing the shortlist.'] Same job spec. Same candidates. One recruiter, not four."
- Visual: `34 HRS → [X] MIN` counter flip.
- Mascot: `node-celebrating`.

**Cue 6 — CTA (35.0s–40.0s)**
- VO: "Comment 'SCREEN' and I'll DM you the full workflow breakdown."
- Mascot: `node-celebrating`, final signature pose.

---

## M2 — "The Report Nobody Builds Anymore" (upgrades idea 003 in `_ideas.md`)

**Target:** marketing/creative agency ops leads, e-commerce operators.
**Runtime:** ~35s.
**Automation:** pulls from ad platform + CRM + analytics, builds the weekly client deck, delivers it to Slack/email at 6am — this is idea **003** already logged as "idea" status; this script makes it filmable.
**CTA:** `Comment "REPORT"` → workflow breakdown + the deck template.

### Cue-by-cue
**Cue 1 — HOOK (0.0s–4.0s)**
- Header pill: `✦ THE MONDAY NOBODY WANTS`
- VO: "Every Monday, someone on your team spends two hours pulling numbers from three different dashboards into one deck nobody double-checks."
- Mascot: `node-thinking` next to three separate dashboard icons.

**Cue 2 — THE COST (4.0s–10.0s)**
- Header pill: `✦ 2 HOURS x 52 WEEKS = [PLACEHOLDER]`
- VO: "That's over 100 hours a year of a strategist's time — spent formatting, not strategizing."
- Visual: `2 HRS → 104 HRS/YR` counter build.
- Mascot: `node-working`.

**Cue 3 — STEP 1: THE PULL (10.0s–18.0s)**
- Progress bar: Level 1.
- Header pill: `✦ STEP 01 / PULLS 3 SOURCES AUTOMATICALLY`
- VO: "The system pulls ad spend, lead volume, and conversion data from every source your clients care about — no logins, no copy-paste."
- Visual: three source icons (ads platform / CRM / analytics) feeding into one glowing container.
- Mascot: `node-idea`.

**Cue 4 — STEP 2: THE DECK BUILDS ITSELF (18.0s–26.0s)**
- Progress bar: Level 2.
- Header pill: `✦ STEP 02 / DECK BUILT & SENT AT 6AM`
- VO: "It builds the deck in your template, writes the summary, and it's in your Slack before your team's first coffee."
- Visual: deck pages assembling in sequence, a Slack notification card popping `📊 Weekly Report — Ready`.
- Mascot: `node-running`.

**Cue 5 — CTA (26.0s–35.0s)**
- Header pill: `✦ [PLACEHOLDER: REAL RESULT] / GET THE TEMPLATE`
- VO: "[PLACEHOLDER: e.g. '2 hours every Monday → zero.'] Comment 'REPORT' and I'll send you the workflow breakdown and the deck template."
- Mascot: `node-celebrating`.

---

# BOFU — direct offer / close

## B1 — "The Math Your Accountant Would Do" (headcount-reduction ROI)

**Target:** any ICP vertical; run this as a retarget to anyone who commented on a MOFU episode.
**Runtime:** ~35s. Full aryamanupmanyu 8-beat formula (this is the format built for direct persuasion).
**CTA:** book a call — the highest-commitment ask, appropriate here because the viewer is already warm.

### Cue-by-cue
**Cue 1 — HOOK (0.0s–4.0s)** *(Beat 1: rhetorical framing + concrete number)*
- Header pill: `✦ $[PLACEHOLDER: AVG. FULLY-LOADED SALARY] A YEAR, OR $[PLACEHOLDER: SYSTEM COST] ONCE?`
- VO: "Do you want to hire someone for $[X] a year to do a job a system does for a fraction of that, forever — or not?"
- Mascot: `node-pointing` at a scale/balance graphic.

**Cue 2 — THE GAP STAT (4.0s–8.0s)** *(Beat 2: precise, not rounded)*
- Header pill: `✦ [PLACEHOLDER: SOURCED, SPECIFIC MARKET STAT]`
- VO: "[PLACEHOLDER: e.g. a precise adoption or market-size figure relevant to the viewer's vertical, sourced before publishing]."

**Cue 3 — THE MOAT LINE (8.0s–12.0s)** *(Beat 3: the quotable structural claim)*
- VO: "A hire needs training, gets sick, and quits. A system doesn't do any of those — it just runs the job."
- Mascot: `node-idea`.

**Cue 4 — THE ADOPTION GAP (12.0s–16.0s)** *(Beat 4: competitor FOMO)*
- VO: "[PLACEHOLDER: e.g. '% of businesses in your space already run this]. The ones that don't are competing on price because they can't compete on speed."

**Cue 5 — THE CAPABILITY LISTICLE (16.0s–24.0s)** *(Beat 5: verb+object, rapid)*
- VO: "Answer every inbound lead in under a minute. Follow up automatically until someone replies. Book the call without a human touching a calendar. Flag the leads actually worth a phone call."
- Visual: four evidence-cards flashing in rhythm with each clause.
- Mascot: `node-working`.

**Cue 6 — THE PUNCHLINE (24.0s–27.0s)** *(Beat 6)*
- Visual: Node stamp `THAT'S THE WHOLE JOB.` over a checkmark burst.
- Mascot: `node-celebrating`. SFX: coin-drop + chime.

**Cue 7 — THE CTA (27.0s–33.0s)** *(Beat 7: stacked, specific)*
- Header pill: `✦ BOOK A 15-MIN CALL`
- VO: "Link in bio. Book 15 minutes — I'll tell you exactly what this replaces in your business, and what it costs to run it instead."

**Cue 8 — SIGN-OFF (33.0s–35.0s)** *(Beat 8: consistent tic)*
- Mascot: Node's fixed final signature pose (same across every episode — define this once if not already, e.g. `node-neutral` with a small wave).

---

## B2 — "We Already Built This For [Vertical]" (case-study close)

**Target:** the specific vertical of your most recent real client win. **Do not build this script for real until you have one real, nameable (or anonymized-with-permission) result** — this is the one format where a fabricated number would do the most damage, since it's explicitly framed as a case study.
**Runtime:** ~30s.
**CTA:** `DM "BUILD"` → scoping call.

### Cue-by-cue
**Cue 1 — HOOK (0.0s–4.0s)**
- Header pill: `✦ REAL CLIENT. REAL NUMBERS.`
- VO: "[PLACEHOLDER: e.g. 'A [vertical] business was losing X leads a week to slow follow-up.'] Here's exactly what we built, and what it did."

**Cue 2 — BEFORE (4.0s–10.0s)**
- Visual: the real "before" evidence card — an actual screenshot/mockup of their manual process (anonymized if needed).
- VO: "[PLACEHOLDER: the real before-state, in one sentence, with a real number.]"

**Cue 3 — THE BUILD (10.0s–20.0s)**
- Progress bar: Level 1 → 2.
- VO: "[PLACEHOLDER: 2-3 sentence real description of what the system does, verb+object style per Beat 5.]"
- Visual: real workflow diagram / evidence cards from the actual build.

**Cue 4 — AFTER (20.0s–25.0s)**
- Header pill: `✦ [PLACEHOLDER: REAL AFTER NUMBER]`
- VO: "[PLACEHOLDER: the real after-state, same units as the before-state, so the comparison is honest.]"
- Mascot: `node-celebrating`.

**Cue 5 — CTA (25.0s–30.0s)**
- VO: "DM 'BUILD' if you want to know what this looks like for your business specifically."

---

## Before any of these go live
1. Replace every `[PLACEHOLDER]` with a real, sourced number — from your own build, a real client (anonymized if needed), or a citable market stat. Log the source the way `GATE3_NOTES.md` does for the Bloodless Coup reel: fact-check claims before publishing, don't guess a percentage because it sounds researched.
2. Add each finished script as a new row in `_ideas.md` with its real before/after and which CTA it used, so you can track which stage + which CTA actually books calls.
3. Build the automation *before* filming the MOFU/BOFU demos of it — never stage a fake workflow on camera; that's the fastest way to lose the "operator-to-operator" credibility the brand voice is built on.
4. Keep the TOFU scripts genuinely light — no sales-close energy, no "book a call." Their only job is to make the ICP think "wait, that's me" and comment for the free resource.
