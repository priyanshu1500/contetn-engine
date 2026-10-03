# ai-agency — Design Philosophy & Creative System

This is the *why* behind the pipeline in `PIPELINE.md`. It exists so any AI
assistant inheriting this project makes the same creative judgment calls we
made — not just the same mechanical steps — including the calls that came
from real mistakes caught mid-project. Read `brand.md` (the locked palette/
type/mascot spec) alongside this file; this document is the reasoning layer
on top of that spec.

---

## 1. Positioning

"I build the automation, then show you exactly how it works." A **portfolio
channel**, not a course or general AI-news feed. Every video is proof-of-
work for one specific, ownable problem. Target viewer: a founder/ops-lead/
agency-owner drowning in a manual process they know is automatable.

Voice: direct, confident, operator-to-operator. Numbers over adjectives
("saved 4 hours a week," not "saved a ton of time"). No hedging ("could,"
"might"). Never hype language, never vague promises, never stock-photo
AI-brain/robot imagery — **Node is our robot; nothing else plays that
role.**

---

## 2. The two-layer visual grammar (the central structural idea)

This is the single most important lesson of this project, discovered by
directly reverse-engineering a high-production-value reference (a photoreal
"desk diorama" carousel animated as a cinemagraph). The reference's trick:
a razor-sharp **static** image, with only one small, forgiving element
animated (falling coins, a glow pulse) — text, mascot, and props stay
**pixel-locked**.

That's backwards from what feels intuitive (add camera movement everywhere
to feel "cinematic"), but it's correct, because it plays to what today's
generative video models are actually good at (ambient/forgiving motion) and
avoids what they're bad at (holding sharp text/props stable across frames).

We adopted this as a **two-layer system**:

- **UI layer** — cards, counters, evidence mockups, drawtext labels. Stays
  **perfectly static, zero shake, zero grain**, always. This is
  Illustrator-flat, software-mockup-crisp. Any camera drift or grain
  applied here is a defect, not a stylistic choice — it was the literal
  cause of a "cheap, shaky screen" complaint that sent us back to fix it.
- **Hero layer** — a small number of **photoreal, Gemini-generated
  cinemagraph shots**, reserved for the emotional bookends (the hook, the
  CTA). These alone carry organic camera drift / grain / ambient particle
  motion, because they're real rendered photography, not flat vector UI.

**Practical rule:** before adding any camera movement or grain to a frame,
name what real-world content justifies it. If the answer is "nothing, it's
flat text," don't add it (this is Fincher's rule, formalized below).

### Why bookends, not a full pivot
We evaluated and explicitly rejected re-doing the *entire* episode in the
heavier photoreal style: it would multiply Gemini round-trips (more
exposure to real, acknowledged web-automation flakiness) for a look that
doesn't suit the "show real software working" demo section — flat, crisp
UI mockups communicate a real automation better than a photoreal diorama
would. Bookend-only gets the production-value lift at the hook/CTA (where
first impressions and conversions matter most) at a fraction of the cost
and risk.

---

## 3. Borrowed cinema-craft rules (from the installed `video`/faceless-channel skills)

These are now permanent audit criteria for every cue, not just the hero
shots. Load `~/.claude/skills/video/references/dramaturgy.md` and
`~/.claude/skills/05-faceless-channel/SKILL.md` directly when doing a full
review pass; the essentials:

- **Camera must have a reason** (Fincher rule). Every camera movement must
  answer "what changed?" If nothing did, the camera is static. This killed
  our uniform Ken-Burns pass.
- **Three-jobs rule.** Every shot must change emotion, advance action, or
  increase pressure — otherwise cut it or shorten the hold. An 8-11s static
  evidence card with only a tiny pop-in is thin by this standard.
- **One-anchor principle.** Commit to one recurring motif/anchor object and
  one final image the viewer carries out. Node is that anchor — he should
  appear at the emotional beat of every scene, and the strongest possible
  ending is on him (the photoreal CTA hero), not a logo pop-in.
- **Never let the screen rest** (faceless-content law #1). Every second
  needs motion — camera, subject, or both. This doesn't mean "add camera
  shake to everything" (see §2) — it means don't let a beat sit completely
  inert; use pop-ins, sequential build-ins, and proof flashes to keep
  something changing even on an otherwise-static card.
- **9:16 UI-safe zones.** Front-load key visual energy in the top ~60% of
  frame; the bottom ~third and the rightmost ~100px get covered by the
  platform's own caption bar and like/comment/share icon column. This is
  now a hard placement constraint (see `PIPELINE.md` §2D).
- **Never show a flat screenshot as the whole treatment** (SaaS-launch
  skill's #1 rule). A static PNG evidence card with zero depth/parallax/
  sequential reveal is the single most common SaaS-demo-video mistake.
  Prefer a build-in (nodes animating in one at a time) over a single paste.
- **The "Problem Flash" hook** — for a pain/before beat, a rapid montage of
  friction (0.3-0.4s per shot) lands harder than one static "before" card
  held for 5+ seconds. Named pattern from the `02-saas-launch` skill,
  underused in early cuts — apply it to any "the old way" beat.

---

## 4. The mascot system — "Node"

**Two deliberate asset tiers, not a compromise:**

1. **Code-drawn flat poses** (Pillow, `mascot/node.py`) for every small
   pop-in during the flat UI section. Chosen specifically because it
   guarantees pixel-perfect, zero-cost, zero-latency consistency across
   every pose and every episode — it completely sidesteps Gemini's
   real, acknowledged day-to-day instability for an asset that appears
   dozens of times per video.
2. **Photoreal Gemini renders** for the hook/CTA bookends only — see
   `GEMINI_ASSET_AUTOMATION.md`. Worth the generation risk exactly twice
   per episode, not dozens of times.

**Original-design constraint (standing, non-negotiable):** Node must be an
*original* character — same design language as any reference the user
shares (rounded dark body, one glowing eye, thin limbs) but never a
pixel-for-pixel reproduction of someone else's specific character design.
Real business logos (Gmail, HubSpot, n8n) are fine to use verbatim — that's
nominative/identification use, not character IP.

**Pose-readability lesson:** early poses were too subtle (arms same color/
thickness as body, most poses looked near-identical). Fixed by thickening
limbs, using two-segment arms (shoulder→elbow→hand, not a single straight
tilt) for real silhouette change per pose, and adding real props (a laptop
rectangle for `working`, a glowing multi-ray lightbulb for `idea`). A pose
prop is often what makes a pose readable at a glance — the limb angle alone
often isn't enough.

---

## 5. The Proof Layer

A quick evidence-chip flash ("Contact created", "AI enriched", "Follow-up
drafted") during the payoff beat. Cheap — just `drawtext`/`drawbox`, no new
assets — and high-value: it's the direct execution of "proof beats a claim"
from an earlier architecture review. Use it whenever a beat's job is to
*prove* something happened, not just *say* it happened.

---

## 6. Failure modes we hit and explicitly rejected — don't repeat these

- **Off-topic cutaways.** Generic mood-word image/stock searches ("glowing
  data dashboard") returned content with zero topical relevance (a stock
  trading chart for a CRM video), composited *under* still-active card
  text. Both readability and relevance broke at once. Rule now: a cutaway
  asset must be topically exact (not a vague mood match) AND placed in a
  clean gap with no simultaneous card text.
- **Uniform camera shake over flat text.** See §2 — the direct cause of a
  "cheap, shaky screen" complaint.
- **Duplicate on-screen labels.** A `drawtext` caption layer added on top
  of an evidence PNG that already had the same label baked into its own
  HTML mockup. Always check what's already inside a generated evidence
  image before adding a redundant caption.
- **Text/mascot collision on a hero shot.** A headline drawn at the same
  coordinates that worked on a flat beige background silently collided
  with Node's photoreal position once the background became a busy photo.
  Any text placed over a photoreal hero shot needs its own scrim + a
  position audit against what's actually in that specific image — don't
  reuse flat-background text coordinates blindly.
- **Letter-by-letter acronym captions.** A script written as "C-R-M" for
  correct TTS pronunciation leaked straight into the caption burn-in as
  literal "C -R -M". Audio pronunciation and on-screen display are two
  different concerns — fix the display layer, never the pronunciation
  layer, when this happens again with a different acronym.
- **A ~3s dead-air gap in VO** that should have been a natural ~0.5s pause.
  Always run `silencedetect` on every new VO before building anything else,
  and compare gap durations against each other — an outlier is a bug, not
  a stylistic pause.

---

## 7. CTA + voice rules

Every episode ends on exactly one of the locked CTA options (see
`brand.md`) — rotate which one per episode, log it, track which converts.
Voice engine currently `edge-tts` (free) while validating the format;
revisit once episodes are converting.

---

## 8. When to reach for which installed skill

| Situation | Skill to load |
|---|---|
| Writing/auditing any camera move, shot list, or storyboard | `video` (dramaturgy.md, universal-rules.md) |
| Generating or critiquing a still image prompt (hero shots, evidence mockups as images) | `image` (golden-rules.md + model-specific refs) |
| A faceless/narration-driven demo reel structurally | `05-faceless-channel` |
| A pain-state / "the old way" beat | `01-viral-hook`, `02-saas-launch` ("Problem Flash") |
| A before/after or transformation beat | `07-before-after` |
| Any SaaS/software demo cinematography question | `02-saas-launch` |
