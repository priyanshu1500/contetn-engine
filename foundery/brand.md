# Brand — AI Agency / Automation Showcase (LOCKED — Template 01)

Locked identity, replacing the earlier dark-teal draft. Sourced from the
"AI Automations Reel Template" reference: warm editorial-paper base, confident
blue/orange accents, a recurring mascot character. This is now the standard
every `ai-agency` episode builds against.

**Positioning (updated 2026-09-15):** "I build the complete closed-loop system,
end to end, that runs the workflow so you don't have to hire someone to."
Not a course, not a general AI-news channel, and not just a single-automation
demo reel — an **outbound lead-gen channel for a systems-sales offer**. Every
video proves a full closed-loop system (trigger → agent action → resolution,
start to finish, zero manual steps in between), and the explicit value prop
is **headcount reduction / cost avoidance**, not just "saved time." Say the
number a business would otherwise spend on a hire or a contractor wherever
the math supports it — this is the single strongest lever for this buyer.

**Target viewer:** a business owner or operator in the **US, France, or wider
Europe** paying for manual labor (front desk, admin, lead follow-up, customer
support) to do a mundane, repeatable workflow — and who would rather pay for
a system than another salary. Higher-budget, higher-intent than a general
"cool AI automation" viewer; speak to them as a buyer, not a hobbyist audience.
English-language copy works across all three markets; keep numbers in USD
unless a specific episode is built for a named non-US client, then match
their currency.

**Every episode should make three things unmistakable:** (1) this replaces a
role/manual process, not just a task, (2) it runs start-to-finish with no
human step in the loop, (3) the CTA is a sales conversation, not a follower
ask — "comment X and I'll show you exactly how this works for your business,"
never a generic "follow for more."

## Palette (locked)

| Token | Hex | Use |
|---|---|---|
| `bg` | `#F5EBDD` | beige editorial-paper background — every card sits on this |
| `panel` | `#FFFFFF` / `#EDE3D3` | lighter card panels over the beige base |
| `ink` | `#413333` | primary text — dark warm brown-black, not pure black |
| `primary` | `#4E71FF` | headlines, UI accents, primary brand blue |
| `accent` | `#F2765E` | orange — CTAs, arrows, hand-drawn annotations, "before" pain state |
| `success` | keep `#2ECC71`-family green | checkmarks / "automated" confirmations only, used sparingly |

This is a full pivot from the earlier dark-teal draft — warm/paper base instead
of near-black, blue+orange instead of teal+coral. Textures from the Material
Library (Phase 1, `assets/materials/paper/`) are the natural background layer
under this palette — they were generated for exactly this kind of warm base.

## Type (locked rules)

- **Headlines:** bold, confident, all-caps for the hook line only (e.g.
  "STOP DOING THIS.") — one weight, not mixed.
- **Body:** clean, minimal, sentence case.
- **Notes/annotations:** a handwritten-style face for the hand-drawn
  arrows/circles/asides (`Caveat`, already in `assets/fonts/google/`).
- **Labels/UI chrome:** a mono/technical face for anything meant to look like
  real software (`JetBrains Mono` if available, else system mono).
- **Hard cap: 2 font weights, 1 family per role, max 3 colors on screen at
  once** (ink + one accent + background). This is a discipline rule, not a
  suggestion — audit every scene against it.

## The mascot — "Node" (original design, our own version)

A simple rounded-block character: dark rounded-square body, one glowing dot
"eye" (accent blue or white glow), thin bent-line limbs for arms/legs — plain
geometric shapes, not photorealistic, not a copy of any existing character.
Built as **code** (`ai-agency/mascot/node.py`, Pillow), not AI-generated —
this guarantees pixel-perfect consistency across every episode and every pose,
with zero generation cost or API flakiness.

**Locked poses** (extend this list as new scenes need them):
`neutral`, `pointing`, `thinking`, `celebrating`, `working` (at a laptop),
`idea` (light-bulb moment), `running`.

Node appears in every episode, at the emotional beat of each scene, exactly
the way this format uses it — not decoration, a recurring host.

## Voice

Direct, confident, operator-to-operator. Short declarative sentences. Numbers
over adjectives ("saved 6 hours a week," not "saved a ton of time"). No
hedging language ("could," "might") — state what the automation does.

**Never do:** hype language ("insane," "game-changer"), vague promises ("AI
will change everything"), stock-photo AI-brain/robot imagery — Node is our
robot; nothing else plays that role.

## CTA (locked per episode, rotate the specific ask — updated for systems-sales positioning)

Every episode ends on exactly one **sales-conversation** ask, never a bare
follow/like ask — this channel sells systems, engagement is a byproduct:
- "Comment `SYSTEM` and I'll show you exactly how this works for your business."
- "Comment `AUTOMATE` and I'll send you the workflow breakdown."
- "DM me `BUILD` if you want this running in your business."
- "Link in bio — book a 15-min call, I'll tell you if this replaces a hire
  for you specifically."

Pick one per episode, log which one in `_ideas.md`, track which converts.
Retired: "Follow for more AI systems that save you time" — too passive for a
buyer-facing offer; only use a follow-ask as a secondary line after the sales
CTA, never instead of it.

## Reference shot-list rhythm (from Template 01, use as the pacing model)

~2 seconds per beat, one clear idea per card, never two claims stacked:
hook → agent explanation → real example (form/input) → enrichment/processing →
result (a real before→after number) → "you can build this too" → compounding
payoff → CTA. Our existing 6-cue narration structure maps onto this; the
lesson is **pacing discipline** (short, punchy, one idea per beat), not
necessarily matching their exact scene count.

## Voice engine

Not locked yet — start on `edge-tts` (free) while validating the format; once
episodes are converting, consider a distinct voice from LexIntent's
`en-IN-PrabhatNeural` so the two channels don't sound identical to a shared
viewer.
