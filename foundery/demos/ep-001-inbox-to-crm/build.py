#!/usr/bin/env python3
"""Ep.001 build v4.0 — full brand pivot to "Template 01": warm beige base,
blue/orange accents, the "Node" mascot at every beat, real evidence mockups
recolored to match, and a Proof Layer (quick evidence-chip flashes) during
the payoff — the highest-value, lowest-cost idea from the "Greg Isenberg
pipeline" review.

Same 3-beat structure as v2-v3 (title -> evidence -> payoff), same 6-cue
narration timing (unchanged, still synced to the locked VO) — only the visual
language changed. Gemini-generated cutaways from v3.0 are dropped this pass:
they were rendered in the old dark-teal palette and would clash with the new
light brand; regenerate them in the new palette once Gemini's web session is
stable again (see the retro logged 2026-09-13/14).

in: evidence/flow-crop.png, evidence/payoff-crop.png (light theme),
    assets-micro/*.png (blue/orange), mascot/node-*.png, captions.ass
    (regenerated with --key-hex #4E71FF --ink-hex #413333)
out: ep001-visual.mp4  (video only; sound added after by soundbed.py)
"""
import subprocess, pathlib

FF = r"D:\tools\ffmpeg\ffmpeg-8.1.2-essentials_build\bin\ffmpeg.exe"
HERE = pathlib.Path(__file__).parent
CAPTIONS = HERE / "captions.ass"
EVID = HERE / "evidence"
MICRO = HERE / "assets-micro"
MASCOT = HERE / "mascot"
HERO = HERE / "hero"
OUT = HERE / "ep001-visual.mp4"
TOTAL = 43.56
W, H = 1080, 1920

def ff_path(p):
    return str(p).replace("\\", "/").replace(":", "\\:")

ARIAL_BD = ff_path("C:/Windows/Fonts/arialbd.ttf")
ARIAL = ff_path("C:/Windows/Fonts/arial.ttf")

# --- brand v4.0 (locked in ai-agency/brand.md) ---
BEIGE = "0xF5EBDD"
CARD = "0xFFFFFF"
INK = "0x413333"
MUTED = "0x8A7F6E"
BLUE = "0x4E71FF"
ORANGE = "0xF2765E"
GREEN = "0x2ECC71"

# warm grid on beige, matching the reference's notebook-paper texture
BG = (f"color=c={BEIGE}:s={W}x{H}:d={TOTAL},"
      f"drawgrid=w=54:h=54:t=1:c=0xE5D9C4@0.8[bg]")

fc = [BG]
cur = "[bg]"
extra_inputs = []
_next_idx = [2]  # 0,1 reserved for the two evidence PNGs added below


def add_input(path):
    idx = _next_idx[0]; _next_idx[0] += 1
    extra_inputs.extend(["-loop", "1", "-t", str(TOTAL), "-i", str(path)])
    return idx


def add_video_input(path):
    """Register a real (non-looped) video clip input — its own timeline
    starts at t=0 of the whole render, same as every other input."""
    idx = _next_idx[0]; _next_idx[0] += 1
    extra_inputs.extend(["-i", str(path)])
    return idx


def hero_bg(path, t0, t1, fade_out=0.4):
    """Full-bleed photoreal Node hero shot — the 'bookend' cinemagraph
    opening/closing frame from the brand-pivot v4.1 pass. Gemini-generated
    (still + same-thread 'animate this image, keep background locked'), so
    it carries real, camera-quality ambient motion instead of a flat vector
    pop-in. Composited once, full-bleed, then fades to the flat beige base
    so the rest of the episode can stay pixel-static UI without a visual
    seam. Text/badges draw on top of this in the normal cue flow."""
    global cur
    idx = add_video_input(path)
    fc.append(f"[{idx}:v]scale={W}:{H}:force_original_aspect_ratio=increase,"
              f"crop={W}:{H},setsar=1,format=rgba,"
              f"fade=t=out:st={t1 - fade_out}:d={fade_out}:alpha=1[hero{idx}]")
    fc.append(f"{cur}[hero{idx}]overlay=0:0:enable='between(t,{t0},{t1})'[herobg{idx}]")
    cur = f"[herobg{idx}]"


def badge_claim(label, line1, line2, color, t0, t1, y=260):
    """White badge + two-line bold claim on the beige base."""
    f = []
    f.append(f"drawbox=x=60:y={y}:w={min(1000, 60+len(label)*20)}:h=64:"
              f"color={CARD}@0.95:t=fill:enable='between(t,{t0},{t1})'")
    f.append(f"drawtext=fontfile='{ARIAL_BD}':text='{label}':fontsize=26:"
              f"fontcolor={MUTED}:x=84:y={y+19}:enable='between(t,{t0},{t1})'")
    f.append(f"drawtext=fontfile='{ARIAL_BD}':text='{line1}':fontsize=64:"
              f"fontcolor={INK}:x=60:y={y+100}:enable='between(t,{t0},{t1})'")
    f.append(f"drawtext=fontfile='{ARIAL_BD}':text='{line2}':fontsize=64:"
              f"fontcolor={color}:x=60:y={y+180}:enable='between(t,{t0},{t1})'")
    return f


def hand_underline(x, y, w_final, t0, dur, color, label):
    global cur
    fc.append(f"{cur}drawbox=x={x}:y={y}:"
              f"w='{w_final}*if(lt(t-{t0},{dur}*0.6),1.15*(t-{t0})/{dur},"
              f"min(1,0.69+0.31*((t-{t0})-{dur}*0.6)/({dur}*0.4)))':"
              f"h=6:color={color}:t=fill:enable='between(t,{t0},{t0}+6)'[{label}]")
    cur = f"[{label}]"


def hand_box(x, y, w, h, t0, stagger, color, label, t_off):
    global cur
    strokes = [
        (x, y, w, 4, t0), (x + w - 4, y, 4, h, t0 + stagger),
        (x, y + h - 4, w, 4, t0 + stagger * 2), (x, y, 4, h, t0 + stagger * 3),
    ]
    for i, (bx, by, bw, bh, bt) in enumerate(strokes):
        fc.append(f"{cur}drawbox=x={bx}:y={by}:w={bw}:h={bh}:color={color}:t=fill:"
                  f"enable='between(t,{bt},{t_off})'[{label}{i}]")
        cur = f"[{label}{i}]"


def pop_in(idx, x, y, size, t0, t1, label):
    global cur
    fc.append(f"[{idx}:v]scale={size}:{size},format=rgba,"
              f"fade=t=in:st={t0}:d=0.18:alpha=1,fade=t=out:st={t1-0.15}:d=0.15:alpha=1[{label}a]")
    fc.append(f"{cur}[{label}a]overlay=x={x}:y='if(lt(t,{t0}+0.22),{y}-24*(1-(t-{t0})/0.22),{y})':"
              f"enable='between(t,{t0},{t1})'[{label}]")
    cur = f"[{label}]"


def node(pose, x, y, size, t0, t1, label):
    """Pop in the Node mascot in a given pose — appears at every scene's
    emotional beat, the recurring host the whole brand system is built on."""
    idx = add_input(MASCOT / f"node-{pose}.png")
    pop_in(idx, x, y, size, t0, t1, label)


def proof_flash(label_text, t0, dur, color, label, y=1520):
    """A tiny evidence chip that flashes for a fraction of a second — the
    Proof Layer. Cheap (just drawtext/drawbox), no new assets, and it's the
    highest-value idea from the pipeline review: proof beats a claim."""
    global cur
    w = 90 + len(label_text) * 17
    fc.append(f"{cur}drawbox=x=60:y={y}:w={w}:h=52:color={CARD}@0.96:t=fill:"
              f"enable='between(t,{t0},{t0+dur})'[{label}bg]")
    cur = f"[{label}bg]"
    fc.append(f"{cur}drawtext=fontfile='{ARIAL_BD}':text='✓ {label_text}':fontsize=24:"
              f"fontcolor={color}:x=78:y={y+15}:enable='between(t,{t0},{t0+dur})'[{label}]")
    cur = f"[{label}]"


# --- cue1 (0.0-4.3): TITLE CARD — bookend hero shot ---
# Photoreal Node (Gemini still + same-thread "animate, keep background
# locked") fills the whole opening frame instead of a flat vector pop-in;
# it fades to the flat beige base right at the cue boundary so cue2 picks
# up on the plain UI system with no visual seam.
hero_bg(HERO / "hook-hero.mp4", t0=0.0, t1=4.3, fade_out=0.4)
# The hero photo has Node sitting mid-frame (~y580-1250) — the headline used
# to sit right on top of him at y=560, unreadable and visually colliding
# with the mascot. Pulled the whole text block up into the clear top band
# (cup/pen bokeh, nothing sharp there) and added a scrim card behind it so
# blue/black text never sits directly on uncontrolled photo detail again.
fc.append(f"{cur}drawbox=x=0:y=130:w={W}:h=330:color={CARD}@0.88:t=fill:"
          f"enable='between(t,0,4.3)'[t1scrim]")
cur = "[t1scrim]"
for i, flt in enumerate(badge_claim("AUTOMATION LOG", "MY INBOX", "RAN ITSELF.",
                                     BLUE, 0.0, 4.3, y=170)):
    lab = f"t1_{i}"
    fc.append(f"{cur}{flt}[{lab}]"); cur = f"[{lab}]"
hand_underline(x=60, y=422, w_final=380, t0=1.1, dur=0.5, color=ORANGE, label="ul1")

# --- cue2 (4.4-10): BEFORE CARD (pain state -> orange) ---
for i, flt in enumerate(badge_claim("THE OLD WAY", "45 MIN/DAY", "COPY-PASTE.",
                                     ORANGE, 4.4, 10.0, y=560)):
    lab = f"t2_{i}"
    fc.append(f"{cur}{flt}[{lab}]"); cur = f"[{lab}]"
idx_bell = add_input(MICRO / "bell.png")
pop_in(idx_bell, x=850, y=590, size=100, t0=4.9, t1=9.6, label="m2")
node("thinking", x=680, y=1090, size=260, t0=5.2, t1=9.6, label="node2")
idx_fly = add_input(MICRO / "gmail-badge.png")
fc.append(f"[{idx_fly}:v]scale=90:90,format=rgba,"
          f"fade=t=in:st=9.6:d=0.1:alpha=1,fade=t=out:st=10.5:d=0.2:alpha=1[flya]")
fc.append(f"{cur}[flya]overlay=x='(-140+(1080)*min(1,(t-9.6)/0.7))':y=700:"
          f"enable='between(t,9.6,10.7)'[m3]")
cur = "[m3]"

# --- cue3 (10.4-19): EVIDENCE — the build ---
# (no extra drawtext label here — flow-crop.png already carries
# "THE BUILD · LIVE AGENT" baked into the mockup; a second label stacked
# on top violates the one-idea-per-beat rule)
p1 = EVID / "flow-crop.png"
inputs_evidence = ["-loop", "1", "-t", str(TOTAL), "-i", str(p1)]
fc.append(f"[0:v]format=rgba,fade=t=in:st=10.4:d=0.4:alpha=1,fade=t=out:st=18.6:d=0.4:alpha=1[ev1]")
fc.append(f"{cur}[ev1]overlay=0:600:enable='between(t,10.4,19.0)'[c3]")
cur = "[c3]"
fc.append(f"{cur}drawbox=x=522:y=778:w=16:h=16:color={BLUE}:t=fill:"
          f"enable='between(t,10.8,19.0)*lt(mod(t,0.6)\\,0.35)'[c3pulse]")
cur = "[c3pulse]"
node("working", x=680, y=1090, size=260, t0=11.0, t1=18.6, label="node3")
hand_box(x=395, y=730, w=290, h=125, t0=12.0, stagger=0.14, color=ORANGE, label="hb", t_off=19.0)

# --- cue4 (19.4-31): EVIDENCE — the payoff ---
# (same fix — payoff-crop.png already carries "THE PAYOFF · CRM ROW,
# AUTO-CREATED" baked in)
p2 = EVID / "payoff-crop.png"
inputs_evidence += ["-loop", "1", "-t", str(TOTAL), "-i", str(p2)]
fc.append(f"[1:v]format=rgba,fade=t=in:st=19.4:d=0.4:alpha=1,fade=t=out:st=30.6:d=0.4:alpha=1[ev2]")
fc.append(f"{cur}[ev2]overlay=0:540:enable='between(t,19.4,31.0)'[c4]")
cur = "[c4]"
for i, ystart in enumerate([665, 730, 795]):
    idx_chk = add_input(MICRO / "check.png")
    t0 = 20.6 + i * 0.3
    pop_in(idx_chk, x=990, y=ystart, size=40, t0=t0, t1=30.6, label=f"chk{i}")
node("pointing", x=680, y=1090, size=260, t0=21.5, t1=30.6, label="node4")
# Proof Layer — quick evidence-chip flashes, the highest-ROI idea from the
# pipeline review: a fraction-of-a-second flash of real proof beats a claim.
proof_flash("Contact created", t0=24.0, dur=0.5, color=GREEN, label="pf1")
proof_flash("AI enriched", t0=24.7, dur=0.5, color=BLUE, label="pf2")
proof_flash("Follow-up drafted", t0=25.4, dur=0.5, color=GREEN, label="pf3")

# --- cue5 (31.4-36.56): PAYOFF CARD — animated counter + filling meter ---
cue5_filters = [
    (f"drawtext=fontfile='{ARIAL_BD}':text='THE RESULT':fontsize=26:"
     f"fontcolor={MUTED}:x=60:y=560:enable='between(t,31.4,36.56)'"),
    (f"drawtext=fontfile='{ARIAL_BD}':"
     f"text='%{{eif\\:min(4\\,floor((t-31.4)/1.1))\\:d}}':fontsize=180:"
     f"fontcolor={BLUE}:x=60:y=610:enable='between(t,31.4,36.56)'"),
    (f"drawtext=fontfile='{ARIAL_BD}':text='HOURS / WEEK BACK':fontsize=42:"
     f"fontcolor={INK}:x=60:y=830:enable='between(t,31.4,36.56)'"),
    (f"drawbox=x=60:y=910:w=960:h=14:color={CARD}:t=fill:enable='between(t,31.4,36.56)'"),
    (f"drawbox=x=60:y=910:w='960*min(1\\,(t-31.4)/5.16)':h=14:color={ORANGE}:t=fill:"
     f"enable='between(t,31.4,36.56)'"),
]
for i, flt in enumerate(cue5_filters):
    lab = f"t5_{i}"
    fc.append(f"{cur}{flt}[{lab}]"); cur = f"[{lab}]"
idx_arrow = add_input(MICRO / "arrow-up.png")
pop_in(idx_arrow, x=370, y=650, size=70, t0=31.8, t1=36.56, label="m4")
node("celebrating", x=670, y=1080, size=280, t0=32.0, t1=36.56, label="node5")

# --- cue6 (36.96-43.56): CTA CARD ---
# timings shifted -2.44s from the original 39.4/46.0 to match the VO's
# tightened silence gap (was ~3.0s dead air after "four hours a week back",
# trimmed to a natural ~0.55s pause — see narration/vo-v1-backup.mp3).
for i, flt in enumerate(badge_claim("NEXT STEP", "COMMENT", "AUTOMATE.",
                                     BLUE, 36.96, 43.56, y=560)):
    lab = f"t6_{i}"
    fc.append(f"{cur}{flt}[{lab}]"); cur = f"[{lab}]"
idx_n8n = add_input(MICRO / "n8n.png")
idx_hub = add_input(MICRO / "hubspot.png")
pop_in(idx_n8n, x=60, y=900, size=70, t0=37.76, t1=43.56, label="m5")
pop_in(idx_hub, x=160, y=900, size=70, t0=37.96, t1=43.56, label="m6")
node("running", x=680, y=1100, size=270, t0=38.16, t1=43.56, label="node6")
hand_underline(x=60, y=812, w_final=340, t0=38.56, dur=0.5, color=ORANGE, label="ul2")

# human touch — camera drift + grain, now scoped ONLY to the photoreal hero
# window (0-4.3s), not the flat UI cues. Per dramaturgy's camera rule ("every
# movement must answer 'what changed?' — if nothing, the camera is static"),
# panning/graining flat drawtext cards was exactly the "shaky screen" defect
# flagged in review. GATE ramps the drift amplitude to zero over the same
# 3.9-4.3s window the hero clip itself fades out on, so framing settles to
# dead-center with no snap, and stays static/grain-free for the rest of the
# flat-card section.
GATE = "if(lt(t,3.9),1,if(lt(t,4.3),(4.3-t)/0.4,0))"
fc.append(f"{cur}scale=1112:1978,"
          f"crop=1080:1920:x='16+10*sin(2*PI*t/23)*({GATE})':"
          f"y='29+6*cos(2*PI*t/29)*({GATE})',"
          f"noise=alls=4:allf=t+u:enable='lte(t,4.3)'[human]")
cur = "[human]"

fonts_dir = HERE.parent.parent.parent / "assets" / "fonts" / "google"
fc.append(f"{cur}subtitles='{ff_path(CAPTIONS)}':fontsdir='{ff_path(fonts_dir)}'[final]")

cmd = [FF, "-y", "-loglevel", "error", *inputs_evidence, *extra_inputs, "-filter_complex", ";".join(fc),
       "-map", "[final]", "-t", str(TOTAL), "-r", "30",
       "-c:v", "libx264", "-crf", "20", "-preset", "medium", "-pix_fmt", "yuv420p",
       str(OUT)]
print("building ep001-visual.mp4 (v4.0 — full brand pivot + Node mascot + Proof Layer) ...")
r = subprocess.run(cmd, capture_output=True, text=True)
if r.returncode != 0:
    print(r.stderr[-4000:])
    raise SystemExit("FFMPEG FAILED")
print(f"-> {OUT}  ({OUT.stat().st_size // 1024} KB)")
