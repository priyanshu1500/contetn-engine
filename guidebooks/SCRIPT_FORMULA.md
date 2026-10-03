# Script Formula — Persuasion Structure for Buyer-Facing Episodes

Reverse-engineered from `@aryamanupmanyu` (75.8K followers, "We consult &
Automate D2C & B2C, working with $300M+" — an AI-automation consultant
selling directly to businesses, the same buyer we're targeting). His format
is **talking-head** (direct-to-camera, personal delivery) — we don't copy
that, our brand is deliberately faceless (Node, the mascot). What transfers
completely is the **persuasion structure underneath the delivery**. Every
one of his reels checked (`Db3akM-yf-O`, `Db8ocVByeA8`, `DbvsLMFSdPD`) uses
the identical 8-beat skeleton below.

Use this as the required structure for every buyer-facing episode from here
on — slot the cue-by-cue production techniques from `DESIGN_PHILOSOPHY.md`
and `PIPELINE.md` (hero bookends, Proof Layer, mascot beats) onto this
skeleton, don't replace it.

---

## The 8 beats

1. **Hook — rhetorical framing + a concrete number in the same sentence.**
   Never a bare claim ("AI can help your business"). Always a specific
   number or a yes/or-not framing that forces a mental answer.
   > "Do you want to close 30% more leads without hiring another agent, or not?"

2. **The gap/opportunity stat — precise, not rounded.** A specific-looking
   number reads as researched; a round one reads as made up. "$10.87
   billion in 2026, climbing to $68.75 billion by 2031" lands harder than
   "a multi-billion dollar market."

3. **The moat/insight line — one quotable sentence explaining *why*, not
   just *that*.** This is the line a viewer would screenshot. Not "AI is
   powerful" — a structural claim about the buyer's specific business:
   > "Speed isn't a nice-to-have in real estate. It's the entire sale."
   > "Solve accuracy and compliance together and clients don't leave. Ever."

4. **The adoption-gap line — competitor FOMO, with a number.** Frame the
   buyer's current position against where competitors already are:
   > "60% of large enterprises have already automated this. Barely a third
   > of small and mid-sized companies have caught up."
   This is the single highest-leverage line for our actual ICP (real
   estate, marketing agencies, hotels, recruiting) — these are competitive,
   status-conscious industries; "your competitor already has this" outperforms
   "this would save you time."

5. **The capability listicle — 4-5 items, each one verb + object, zero
   adjectives.** "Categorize transactions automatically. Reconcile bank
   statements in real time. Process receipts and invoices. Flag anomalies
   before they become audit problems." Rapid, concrete, scannable — this
   is also where our evidence-card sequential build-in (from `PIPELINE.md`)
   does double duty, visualizing each listicle item as it's said.

6. **The punchline — one short, confident reaction breaking the info
   rhythm.** His version is verbal personality ("This one is just BOOM.").
   Ours has to be visual since we're faceless: a Node pose + a short on-
   screen stamp (`celebrating` pose + "THAT'S IT." or similar), landing at
   the exact beat his vocal punchline would.

7. **The CTA — a stacked, specific lead magnet, never vague.** Not "I'll
   DM you." Always two named deliverables: "the full breakdown **and** a
   step-by-step implementation roadmap." Matches our own CTA rule in
   `brand.md` (sales-conversation ask, not a follow-ask) — just make the
   promised deliverable concrete and doubled, not singular and vague.

8. **A consistent sign-off tic.** He closes every video identically
   ("Ciao, I'll see you in the next one") — a personal-brand consistency
   device. Our equivalent: Node's final pose/gesture should be the *same*
   across every episode's last beat, so it reads as a recurring signature,
   not a one-off animation.

---

## Two visual takeaways (not just copy)

- **A persistent pinned headline**, not swapped per-cue. His bold caption
  ("TURN YOUR CLAUDE INTO A $500 PRODUCTIVITY MACHINE") stays on screen for
  the *entire* video, reinforcing the hook's promise continuously. Our
  cue-by-cue `badge_claim` cards replace their text every beat — consider
  keeping one persistent small claim-strip pinned throughout, in addition
  to the per-cue cards, for the episodes where the hook is the whole pitch.
- **Solid-color highlight boxes on karaoke captions**, not just color-
  changing text. His active-word styling is a filled rounded-rect behind
  the phrase, not a text-color swap — reads punchier at a glance. Worth
  testing as a `karaoke.py` style variant (`--key-style box` alongside the
  existing color-only mode) for buyer-facing episodes.

## What does NOT transfer

- The talking-head/personal-brand delivery itself — we stay faceless by
  design (Node is the host).
- His audience is aspiring agency *builders* ("start this business") —
  ours is the *buyer* of a finished system. Beat 5's capability listicle
  and beat 4's adoption-gap line port directly; beats 1-3 need reframing
  from "here's an opportunity to start" to "here's what replacing your
  process/hire actually looks like" — see the rewritten ep-002 script for
  the applied version.
