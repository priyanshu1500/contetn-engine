# The Curiosity Ladder — a required pass before any script is greenlit

Added 2026-09-23, synthesized from analysis of a growth-strategy video on Instagram's
interest-based algorithm (curiosity/payoff pacing, own-account Insights data). This is an
addition to `docs/SCRIPT_FORMULA.md`'s 8-beat structure, not a replacement — run both. This
one rule applies to every format we make: Node-mascot TOFU/MOFU/BOFU scripts *and* the
documentary-TOFU episodes (`documentary_tofu/`).

## Why these three metrics
Instagram's own Insights panel ranks what it optimizes for, in order: **watch time, skip
rate, shares.** Follower count and likes are not primary signals — the algorithm judges each
piece of content on its own, so a brand-new account's video can reach as far as an established
one's. Practical consequence: never hold back a script because "the account is too small
yet" — that's not how the feed works anymore. It also means CTA-comment counts (what
`_ideas.md` was tracking) are a *downstream* signal that only tells you about the viewers who
already stayed to the end — they say nothing about whether the first 15% of the video held
anyone. Watch time and shares are the metrics that decide whether a TOFU/MOFU piece gets
distributed at all.

## The mechanic: curiosity vs. payoff
- **Curiosity** is what stops the scroll — a topic framed as a question the viewer wants
  answered, not a fact plainly stated.
- **Payoff** is answering that question — and it's also the moment the viewer has permission
  to leave. Every payoff is a retention risk, not just value delivered.
- High watch time comes from **staggering** payoffs: answer partially, and let that partial
  answer open a *new*, smaller question, so the viewer never has a clean exit point until the
  script is actually done with them.

## The checklist (apply to every draft before it's approved for filming/building)

1. **Outcome-first test.** Read only the first line. Could a viewer already guess what this
   video is "about" (the literal topic/company/number) just from that line? If yes, it's
   stated too plainly — reframe it as the *outcome* the audience wants, or the tension/stakes,
   not the subject itself. ("401(k)s are good for retirement" fails this test. "Your job is
   handing you free money every month and you're leaving it on the table" passes it.)
2. **Premature-payoff flag.** Mark the timestamp/beat where the core answer (the automation
   name, the company, the number, the "aha") is first fully stated. If that lands in the first
   third of the runtime with nothing built up before it, delay it — spend that space on the
   problem, the common mistake, or the stakes instead.
3. **Re-hook-after-reveal rule.** Every payoff beat must be immediately followed by a new,
   smaller curiosity hook — never by a flat statement, a pause, or a CTA with nothing in
   between. ("Don't just invest in any index fund — here are my three, and why the others are
   riskier" is the pattern: the answer to question 1 becomes the setup for question 2.)
4. **Audience-want framing.** For every topic, write down what the audience *wants* from it,
   not what the topic literally is, and open with that. If you can't state the want in one
   sentence, the topic isn't picked yet.

## What this does NOT change
It doesn't replace `SCRIPT_FORMULA.md`'s 8 beats (hook / gap-stat / moat-line / adoption-gap /
listicle / punchline / CTA / sign-off) — the ladder governs *pacing and reveal order* inside
that structure, the 8 beats govern *content*. Both apply together.

## Tooling status (be honest about what's automated vs. manual)
- **Documentary engine** (`documentary_tofu/engine/lint.py`): can check this in code, because
  those episodes have real shot/caption timing. Planned check: flag if the named subject/core
  answer is spoken in the first ~15% of runtime with no reframed hook line before it — a cheap
  proxy for stating the topic too early. Not yet implemented as of 2026-09-23; add alongside
  the existing effects/rhythm checks next time `lint.py` is touched.
- **Node-mascot scripts** (T1/T2/M1/M2/B1/B2 in `FUNNEL_CONTENT_PLAN_v1.md`): plain text, no
  timing data — nothing has been filmed yet, so there is no EDL to lint. This stays a **manual
  review step**, run against the 4-item checklist above before a script goes into production.
  Don't claim this is automated when it isn't.

## Worked example: T1 rewritten (before → after)

**Before** (original `FUNNEL_CONTENT_PLAN_v1.md` draft — fails checks 2 and 3):
- Cue 1 (0-4s): "You have a full-time employee whose entire job is copy-paste. You've never
  met them. You still pay them $[X] an hour."
- Cue 2 (4-10s): immediately explains the metaphor is manual data-entry/follow-up work — the
  "who is this employee" question is answered within 10 seconds of a 20-second video, leaving
  nothing to hold attention through cues 3-4 except a stat and the CTA. Premature payoff, no
  re-hook after it.

**After (T1v2) — applies the full checklist:**

*Cue 1 — hook, outcome-framed, no premature detail (0.0s-4.5s)*
> VO: "You have a full-time employee who has never once complained, never needs training
> twice, and has never called in sick. You've also never met them."
- This passes the outcome-first test: it describes a *quality* (the ideal employee) without
  revealing what/who it is. A viewer cannot guess the topic from this line alone.

*Cue 2 — deepen the mystery, still no reveal (4.5s-9.0s)*
> VO: "They work the exact same hours as everyone else on your team. You just can't see them
> on the org chart."
- This is the delay tactic from the reference: describe consequences and behavior, not the
  answer. Curiosity increases instead of resolving.

*Cue 3 — the reveal, framed as a small twist, not a flat statement (9.0s-13.5s)*
> VO: "It's not a person. It's every manual step your real employees are stuck repeating by
> hand — and it's on payroll whether you notice it or not."
- Payoff #1 lands here — about 55% into the runtime, not the first third.

*Cue 4 — immediate re-hook off the reveal (13.5s-17.0s)*
> VO: "Here's the part almost nobody checks: it's not the biggest task that costs you the
> most. It's the one you do every single day."
- New, smaller curiosity gap opens the instant payoff #1 lands — per the re-hook rule.

*Cue 5 — CTA, arriving as the answer to cue 4's new question, not a cold ask (17.0s-20.0s)*
> VO: "Comment 'AUDIT' and I'll send you the checklist that finds exactly which daily task
> that is in your business."
- The CTA is framed as the payoff to the LAST open question, so it doesn't feel like a bolted-
  on ask — this mirrors "your only reason to keep watching was to get this."

Visual direction (Node poses, header pills, cards) carries over unchanged from the original
T1 spec in `FUNNEL_CONTENT_PLAN_v1.md` — only the VO/pacing changed. Logged as `T1v2` in
`_ideas.md`, marked as the ladder's worked example.
