# Ep.002 — "The Fourteen Minutes" (Real Estate)

Full shot-by-shot creative script. **Rewritten 2026-09-16** to apply the
8-beat persuasion formula in `ai-agency/docs/SCRIPT_FORMULA.md`, reverse-
engineered from `@aryamanupmanyu` (an AI-automation consultant selling
directly to businesses — same buyer type we're targeting). This is a
planning document — for your approval before we move to production build.

**Positioning:** buyer-facing, closed-loop-systems offer (see `brand.md`'s
2026-09-15 positioning update). **Vertical: real estate agencies**, chosen
deliberately over trying to address real estate + hotels + marketing
agencies + recruiting all in one 46s reel — one sharp, vivid persona beats
four diluted ones. The exact same underlying automation (missed call →
qualified → booked) is the natural proof-of-work for a follow-up episode
retargeted at hotels (missed reservation calls) or recruiting (missed
candidate calls) — same system, same script skeleton, swap the persona and
numbers. Log that as ep-003/ep-004 candidates once this one is validated.

**CTA:** `Comment "SYSTEM"` per `brand.md`'s updated CTA list.

---

## Why this is a rewrite, not a polish

**v1** opened on a claim ("We replaced a full-time front-desk hire") and
argued its case with logic and stats. **v2** hit all 8 `SCRIPT_FORMULA.md`
beats but was still a listicle wearing a demo's clothes. **v3 (this one)**
opens on a *scene* — a specific $650,000 buyer, a specific 14 minutes — and
tells the whole pitch as a story with a turn, a mechanism, proof, and a
punch, hitting the same 8 beats without ever feeling like a stat-dump.
Storytelling beats argument: a viewer forgets a percentage, they remember
"the buyer called the office next door." See the chat response this script
shipped in for the full storyteller's reasoning behind each line.

---

## Cue-by-cue shot list

### Cue 1 — HOOK (0.0-4.3s) — Beat 1: a specific scene, not a claim
**VO:** "A six hundred fifty thousand dollar buyer called this agency.
Nobody picked up."
**Visual:** Photoreal Gemini hero bookend (cinemagraph technique, see
`GEMINI_ASSET_AUTOMATION.md`). Visual anchor for this episode: a phone on a
desk next to a "For Sale" sign miniature or a property listing printout —
distinct from ep-001's envelope scene, keeps the recurring-motif idea (a
desk + phone family, matching this episode's actual subject) without
reusing the exact same prop.

**Image prompt:**
> Macro product photography, shallow depth of field, warm cinematic desk
> lighting. A smartphone lying face-up on a wood desk showing a missed-call
> notification with a glowing red banner, next to a small "For Sale" real
> estate sign miniature and a property listing printout, blurred in the
> background. Warm beige and blue color palette, photoreal render,
> product-photography quality, 9:16 vertical, no readable text beyond a
> generic notification shape, no logos.

**Animate prompt:**
> Keep the entire composition and background exactly locked and static.
> Only animate the missed-call notification's red banner gently pulsing
> and the phone screen's glow subtly breathing.

**Text overlay:** Headline "$650K BUYER CALLED." / "NOBODY ANSWERED." (blue)
— the scene rendered in text, not a claim. Persistent pinned claim-strip
(new technique from `SCRIPT_FORMULA.md`'s visual takeaways) below it — small
badge reading "A REAL PATTERN, EVERY AGENCY SEES IT" that stays visible
through cues 1-3. **Do not label this "true story" or name/imply a specific
real agency unless it is one, on the record, with permission** — the scene
is written as a vivid, representative composite to make an honest statistic
concrete, not a documented case study; claiming otherwise would be a false
testimonial. If a real client case becomes available later, swap in their
actual numbers and it's fine to say so explicitly then. Scrim card behind
all of it (per the ep-001 text/mascot-collision fix).
**Mascot:** none this beat (hero shot carries it).

### Cue 2 — THE TURN (4.4-10s) — Beats 2+4: the specific loss becomes universal
**VO:** "Fourteen minutes later, he called the office next door instead.
Seventy-eight percent of buyers go with whoever answers first."
**Visual:** Problem Flash montage (proven technique, applied properly this
time per the ep-001 review) — 4 quick shots, ~0.4s each, continuing the
SAME buyer's story rather than a generic montage:
1. A phone screen timer ticking: 0:00 → 14:00
2. A rival agency's "SHOWING BOOKED" placard sliding onto the SAME property
   photo from cue 1 (the specific buyer, lost to a specific competitor —
   not an abstract stat yet)
3. Voicemail icon, greyed out
4. A calendar with a grayed-out, empty "showing" slot
Hard-cut to the static stat card: "78% GO WITH THE FIRST REPLY." (dark) /
"MOST AGENCIES: VOICEMAIL." (orange) — this is the hinge line where the
one buyer's loss becomes "this happens to agencies like yours," made
explicit on screen, not just spoken.
**Mascot:** `thinking`, safe-zone coordinates from ep-001 (x≈680, y≈1090).

### Cue 3 — THE MECHANISM (10.4-19s) — Beat 3, delivered as one clean image
**VO:** "So instead of hiring someone to sit by the phone all day, we gave
the phone a brain. The second a call is missed, it acts."
**Why this line, not a features list yet:** "We gave the phone a brain" is
the entire mechanism in one image — concrete, ownable, quotable. The actual
capability breakdown comes in cue 4, once the viewer already has the
picture; leading with features here would flatten the story back into a
spec sheet.
**Visual:** Sequential evidence-card build-in (the "add depth" fix from
`PIPELINE.md`) — three nodes animating in one at a time with arrows:
`Missed Call` → `Agent (texts · qualifies · checks budget)` → `Calendar`.
**Annotation:** hand-drawn orange box circling the "Agent" node (`hand_box`,
remember the required `t_off`).
**Mascot:** `working`, same safe-zone coordinates.

### Cue 4 — THE PROOF (19.4-31s) — Beat 5: capability listicle, dramatized
**VO:** "Watch. It texts back in under ten seconds, asks the two questions
that actually matter — budget and timeline — and locks in a showing before
he even thinks about calling anyone else."
**Note:** "before he even thinks about calling anyone else" deliberately
closes the loop back to cue 1-2's specific buyer — the proof beat resolves
the story's tension (will THIS buyer get the callback in time?) rather than
just demonstrating a generic feature.
**Visual:** Real evidence mockup — an SMS thread:
```
[missed call icon]  Missed call from (555) 019-2231

Agent:  Hey! Saw you called about 42 Birchwood Ave — what's your budget
        range and ideal move-in timeline?
Caller: Around $450k, looking to move in the next 2 months
Agent:  Perfect fit. Does Thurs 2pm or Fri 10am work for a showing?
Caller: Fri 10am
Agent:  Booked! See you Friday at 10am. ✅
```
Same phone-thread HTML mockup technique as before, brand colors.
**Proof Layer** (per `DESIGN_PHILOSOPHY.md` §5): 3 quick evidence-chip
flashes — "Replied · 8s", "Budget captured", "Showing booked".
**Mascot:** `pointing`, same safe-zone coordinates.

### Cue 5 — THE PUNCH (31.4-39s) — Beats 5(cont)+6
**VO:** "That's a full-time coordinator's job, done before your coffee gets
cold. Six showings a week that used to just evaporate, booked
automatically."
**Visual:** Animated counter + filling meter (0→6, "SHOWINGS / WEEK
RECOVERED"), plus a small line under it: "= 1 COORDINATOR'S JOB" (muted,
small — the headcount-replacement framing made explicit, staying within
the 3-color/2-weight cap).
**The punch beat** (our visual equivalent of his verbal "This one is just
BOOM"): land the `celebrating` mascot pose exactly on "done before your
coffee gets cold" with a short on-screen stamp — "BEFORE YOUR COFFEE'S
COLD." — the vivid, slightly funny image is what makes this beat land
harder than a bare "saves 3 hours" ever could.
**Mascot:** `celebrating`, same safe-zone coordinates.

### Cue 6 — CTA (39.4-46s) — Beats 7+8: an indicting question + stacked ask
**VO:** "Still paying someone to sit by the phone and hope? Comment
SYSTEM. I'll send you the exact blueprint."
**Why a question, not a statement:** "Still paying someone to sit by the
phone and hope?" makes *not* commenting feel like admitting the answer is
yes — an indicting question converts harder than a flat CTA line because it
forces a private, uncomfortable yes/no before the viewer even reaches the
comment box.
**Visual:** `badge_claim` CTA card — "NEXT STEP" / "COMMENT" / "SYSTEM."
(blue).
**Sign-off (Beat 8):** Node's `running` pose here should become the *fixed,
recurring* closing gesture for every future episode — same pose, same
framing, every single time — so it reads as a signature the way his "Ciao,
I'll see you in the next one" does. Log this as the locked closing beat in
`brand.md` once approved.
**Visual bookend:** photoreal CTA hero shot — same phone/desk family as the
hook, resolved: phone screen shows a calendar confirmation instead of a
missed-call banner, "For Sale" sign now has a small "SHOWING BOOKED" sticky
note beside it.

**CTA hero animate prompt:**
> Keep the entire composition and background exactly locked and static.
> Only animate the phone screen's glow gently pulsing and a small
> calendar-checkmark icon subtly appearing.

---

## Production notes

- **Persistent pinned claim-strip** (cues 1-3): new technique this episode,
  see `SCRIPT_FORMULA.md`. Needs a `build.py` helper distinct from the
  per-cue `badge_claim` — a strip that stays mounted across a longer time
  window while cue cards change underneath it.
- **Karaoke caption style**: consider testing the solid-highlight-box
  variant (`SCRIPT_FORMULA.md`'s second visual takeaway) on this episode
  as an A/B against ep-001's color-only style.
- **Asset generation**: Gemini (`gemini_animate.py`) for the hero shots as
  usual; Google Flow for additional frame variety per the standing
  instruction — its Scenes feature keeps the phone/desk prop consistent
  across the hook/CTA pair.
- **Captions**: proofread the entire `.ass` file line by line before
  burning in — non-negotiable after ep-001 needed three rounds of post-
  delivery transcription fixes. See `QC_CHECKLIST.md` §2.
- **VO edits**: if any line needs a re-take, use the cached
  `narration/lines/cue_0N.wav` clips to re-lay corrected timing — never
  regenerate the whole file for a one-line fix.

---

## Open items needing your input before build

1. Real numbers — replace the $650K/14-minute scene and the 78%/6-showings
   figures with real client data if available, or confirm a credible
   composite is acceptable (see the honesty note on cue 1's text overlay —
   don't let the scene read as a specific documented case unless it is one).
2. Confirm real estate as the lead vertical for this episode (vs. hotels or
   recruiting) — the same script skeleton ports to either with a persona/
   prop swap if you'd rather lead with a different one.
3. Confirm the real tool stack for any logo pop-ins (Twilio + calendar tool
   assumed, placeholder).
4. Confirm "Comment SYSTEM" and the locked Node sign-off pose (`running`)
   as permanent, recurring brand fixtures going forward.
