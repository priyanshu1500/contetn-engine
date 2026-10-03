#!/usr/bin/env python3
"""Ep.002 build v1.1 — "The Fourteen Minutes" (Real Estate Missed-Call Agent).
"""Ep.002 build v1.3 — "The Fourteen Minutes" (Real Estate Missed-Call Agent).
Built against the locked brand system in ai-agency/brand.md and PIPELINE.md §2F.
Applies SCRIPT_FORMULA.md's 8-beat persuasion structure with photoreal hero bookends
(hook + CTA), persistent pinned claim-strip (cues 1-3), sequential evidence build-in,
SMS thread mockup, dashboard cutaway, Proof Layer, and locked Node mascot sign-off.
Overscans hero video inputs (1250x2222) to completely eliminate Gemini/Veo watermark.
Refines Hook and CTA cards into polished floating editorial card panels with proper underline placement.

in: evidence/flow-crop.png, evidence/sms-crop.png, evidence/dashboard-crop.png,
    assets-micro/*.png, mascot/node-*.png, hero/hook-hero.mp4, hero/cta-hero.mp4,
    captions.ass
out: ep002-visual.mp4 (video only; sound design & mux added after by soundbed.py)
"""
import subprocess, pathlib

FF = r"D:\tools\ffmpeg\ffmpeg-8.1.2-essentials_build\bin\ffmpeg.exe"
HERE = pathlib.Path(__file__).parent
CAPTIONS = HERE / "captions.ass"
EVID = HERE / "evidence"
MICRO = HERE / "assets-micro"
MASCOT = HERE / "mascot"
HERO = HERE / "hero"
OUT = HERE / "ep002-visual.mp4"
TOTAL = 46.0
W, H = 1080, 1920

def ff_path(p):
    return str(p).replace("\\", "/").replace(":", "\\:")

ARIAL_BD = ff_path("C:/Windows/Fonts/arialbd.ttf")
ARIAL = ff_path("C:/Windows/Fonts/arial.ttf")

# --- brand palette (locked in ai-agency/brand.md) ---
BEIGE = "0xF5EBDD"
CARD = "0xFFFFFF"
INK = "0x413333"
MUTED = "0x8A7F6E"
BLUE = "0x4E71FF"
ORANGE = "0xF2765E"
GREEN = "0x2ECC71"

# Warm grid on beige base
BG = (f"color=c={BEIGE}:s={W}x{H}:d={TOTAL},"
      f"drawgrid=w=54:h=54:t=1:c=0xE5D9C4@0.8[bg]")

fc = [BG]
cur = "[bg]"
inputs = []


def add_input(path):
    """Register a still-image input looped for TOTAL duration."""
    idx = len(inputs)
    inputs.append(["-loop", "1", "-t", str(TOTAL), "-i", str(path)])
    return idx


def add_video_input(path):
    """Register a real (non-looped) video clip input."""
    idx = len(inputs)
    inputs.append(["-i", str(path)])
    return idx


def hero_bg(path, t0, t1, fade_out=0.4):
    """Full-bleed photoreal Node hero shot bookends. Composited once, full-bleed,
    then fades to the flat base so the UI section picks up cleanly."""
    """Full-bleed photoreal Node hero shot bookends. Overscans by ~1.15x and crops
    with top alignment to push bottom-corner watermarks completely out of frame."""
    global cur
    idx = add_video_input(path)
    fc.append(f"[{idx}:v]scale={W}:{H}:force_original_aspect_ratio=increase,"
              f"crop={W}:{H},setsar=1,format=rgba,"
    fc.append(f"[{idx}:v]scale=1250:2222:force_original_aspect_ratio=increase,"
              f"crop={W}:{H}:(in_w-{W})/2:0,setsar=1,format=rgba,"
              f"fade=t=out:st={t1 - fade_out}:d={fade_out}:alpha=1[hero{idx}]")
    fc.append(f"{cur}[hero{idx}]overlay=0:0:enable='between(t,{t0},{t1})'[herobg{idx}]")
    cur = f"[herobg{idx}]"


def pinned_strip(text, t0, t1, y=80):
    """Persistent pinned claim-strip (cues 1-3) per PIPELINE.md §2F & SCRIPT_FORMULA.md.
    Reinforces the hook promise continuously across multiple beats."""
    global cur
    w = 80 + len(text) * 16
    fc.append(f"{cur}drawbox=x=60:y={y}:w={w}:h=48:color={CARD}@0.95:t=fill:"
              f"enable='between(t,{t0},{t1})'[pstrip_bg]")
    cur = "[pstrip_bg]"
    fc.append(f"{cur}drawtext=fontfile='{ARIAL_BD}':text='{text}':fontsize=20:"
    fc.append(f"{cur}drawtext=fontfile='{ARIAL_BD}':text='{text}':expansion=none:fontsize=20:"
              f"fontcolor={MUTED}:x=78:y={y+14}:enable='between(t,{t0},{t1})'[pstrip_txt]")
    cur = "[pstrip_txt]"


def badge_claim(label, line1, line2, color, t0, t1, y=260):
    """White badge + two-line bold claim on the beige base."""
    f = []
    f.append(f"drawbox=x=60:y={y}:w={min(1000, 60+len(label)*20)}:h=64:"
              f"color={CARD}@0.95:t=fill:enable='between(t,{t0},{t1})'")
    f.append(f"drawtext=fontfile='{ARIAL_BD}':text='{label}':expansion=none:fontsize=26:"
              f"fontcolor={MUTED}:x=84:y={y+19}:enable='between(t,{t0},{t1})'")
    f.append(f"drawtext=fontfile='{ARIAL_BD}':text='{line1}':expansion=none:fontsize=64:"
              f"fontcolor={INK}:x=60:y={y+100}:enable='between(t,{t0},{t1})'")
    f.append(f"drawtext=fontfile='{ARIAL_BD}':text='{line2}':expansion=none:fontsize=64:"
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
    """Pop in the Node mascot in a given pose."""
    idx = add_input(MASCOT / f"node-{pose}.png")
    pop_in(idx, x, y, size, t0, t1, label)


def proof_flash(label_text, t0, dur, color, label, y=1520):
    """Proof Layer: tiny evidence chip that flashes for a fraction of a second."""
    global cur
    w = 90 + len(label_text) * 17
    fc.append(f"{cur}drawbox=x=60:y={y}:w={w}:h=52:color={CARD}@0.96:t=fill:"
              f"enable='between(t,{t0},{t0+dur})'[{label}bg]")
    cur = f"[{label}bg]"
    fc.append(f"{cur}drawtext=fontfile='{ARIAL_BD}':text='✓ {label_text}':fontsize=24:"
    fc.append(f"{cur}drawtext=fontfile='{ARIAL_BD}':text='✓ {label_text}':expansion=none:fontsize=24:"
              f"fontcolor={color}:x=78:y={y+15}:enable='between(t,{t0},{t0+dur})'[{label}]")
    cur = f"[{label}]"


# ==============================================================================
# Filter Graph Assembly
# ==============================================================================

# --- Persistent Pinned Claim-Strip (Cues 1-3: 0.0 - 19.99s) ---
pinned_strip("A REAL PATTERN · EVERY AGENCY SEES IT", t0=0.0, t1=19.99, y=80)

# --- CUE 1 (0.0 - 5.3s): HOOK — Photoreal Hero Bookend ---
hero_bg(HERO / "hook-hero.mp4", t0=0.0, t1=5.3, fade_out=0.4)
# Scrim card over top photo bokeh
fc.append(f"{cur}drawbox=x=0:y=140:w={W}:h=320:color={CARD}@0.88:t=fill:"
          f"enable='between(t,0,5.3)'[t1scrim]")
cur = "[t1scrim]"
for i, flt in enumerate(badge_claim("REAL ESTATE AUTOMATION", "$650K BUYER CALLED.", "NOBODY ANSWERED.",
                                     BLUE, 0.0, 5.3, y=170)):
    lab = f"t1_{i}"
    fc.append(f"{cur}{flt}[{lab}]"); cur = f"[{lab}]"
hand_underline(x=60, y=422, w_final=560, t0=1.1, dur=0.5, color=ORANGE, label="ul1")
# Polished floating Hook card container
fc.append(f"{cur}drawbox=x=60:y=120:w=960:h=420:color={CARD}@0.94:t=fill:"
          f"enable='between(t,0,5.3)'[t1card_bg]")
cur = "[t1card_bg]"
fc.append(f"{cur}drawbox=x=95:y=150:w=360:h=52:color={CARD}:t=fill:"
          f"enable='between(t,0,5.3)'[t1badge_bg]")
cur = "[t1badge_bg]"
fc.append(f"{cur}drawtext=fontfile='{ARIAL_BD}':text='REAL ESTATE AUTOMATION':expansion=none:fontsize=24:"
          f"fontcolor={MUTED}:x=115:y=165:enable='between(t,0,5.3)'[t1badge_txt]")
cur = "[t1badge_txt]"
fc.append(f"{cur}drawtext=fontfile='{ARIAL_BD}':text='$650K BUYER CALLED.':expansion=none:fontsize=64:"
          f"fontcolor={INK}:x=95:y=245:enable='between(t,0,5.3)'[t1_h1]")
cur = "[t1_h1]"
fc.append(f"{cur}drawtext=fontfile='{ARIAL_BD}':text='NOBODY ANSWERED.':expansion=none:fontsize=64:"
          f"fontcolor={BLUE}:x=95:y=330:enable='between(t,0,5.3)'[t1_h2]")
cur = "[t1_h2]"
hand_underline(x=95, y=405, w_final=560, t0=1.1, dur=0.5, color=ORANGE, label="ul1")

# --- CUE 2 (5.55 - 12.73s): THE TURN / GAP STAT ---
for i, flt in enumerate(badge_claim("THE GAP", "78% GO WITH", "THE FIRST REPLY.",
                                     ORANGE, 5.55, 12.73, y=560)):
    lab = f"t2_{i}"
    fc.append(f"{cur}{flt}[{lab}]"); cur = f"[{lab}]"
fc.append(f"{cur}drawtext=fontfile='{ARIAL_BD}':text='MOST AGENCIES\\: VOICEMAIL.':fontsize=28:"
fc.append(f"{cur}drawtext=fontfile='{ARIAL_BD}':text='MOST AGENCIES\\: VOICEMAIL.':expansion=none:fontsize=28:"
          f"fontcolor={MUTED}:x=60:y=850:enable='between(t,5.55,12.73)'[c2sub]")
cur = "[c2sub]"
hand_underline(x=60, y=812, w_final=480, t0=6.2, dur=0.5, color=ORANGE, label="ul2")
idx_bell = add_input(MICRO / "bell.png")
pop_in(idx_bell, x=850, y=590, size=100, t0=5.8, t1=12.4, label="m2")
node("thinking", x=680, y=1090, size=260, t0=5.8, t1=12.4, label="node2")

# --- CUE 3 (12.98 - 19.99s): THE MECHANISM / FLOW EVIDENCE ---
idx_ev_flow = add_input(EVID / "flow-crop.png")
fc.append(f"[{idx_ev_flow}:v]format=rgba,fade=t=in:st=12.98:d=0.35:alpha=1,"
          f"fade=t=out:st=19.5:d=0.35:alpha=1[ev_flow]")
fc.append(f"{cur}[ev_flow]overlay=0:600:enable='between(t,12.98,19.99)'[c3]")
cur = "[c3]"
fc.append(f"{cur}drawbox=x=522:y=778:w=16:h=16:color={BLUE}:t=fill:"
          f"enable='between(t,13.2,19.6)*lt(mod(t,0.6)\\,0.35)'[c3pulse]")
cur = "[c3pulse]"
node("working", x=680, y=1090, size=260, t0=13.2, t1=19.6, label="node3")
hand_box(x=395, y=730, w=290, h=125, t0=14.0, stagger=0.14, color=ORANGE, label="hb", t_off=19.99)

# --- CUE 4 (20.29 - 30.51s): THE PROOF / SMS THREAD & DASHBOARD CUTAWAY ---
idx_ev_sms = add_input(EVID / "sms-crop.png")
fc.append(f"[{idx_ev_sms}:v]format=rgba,fade=t=in:st=20.29:d=0.35:alpha=1,"
          f"fade=t=out:st=28.2:d=0.35:alpha=1[ev_sms]")
fc.append(f"{cur}[ev_sms]overlay=0:480:enable='between(t,20.29,28.5)'[c4_sms]")
cur = "[c4_sms]"
for i, ystart in enumerate([610, 715, 820]):
    idx_chk = add_input(MICRO / "check.png")
    t0_chk = 21.0 + i * 0.4
    pop_in(idx_chk, x=990, y=ystart, size=40, t0=t0_chk, t1=28.2, label=f"chk{i}")
node("pointing", x=680, y=1090, size=260, t0=21.0, t1=28.2, label="node4")

# Proof Layer chips
proof_flash("Replied · 8s", t0=22.5, dur=0.6, color=GREEN, label="pf1")
proof_flash("Budget captured", t0=24.5, dur=0.6, color=BLUE, label="pf2")
proof_flash("Showing booked", t0=26.5, dur=0.6, color=GREEN, label="pf3")

# Dashboard Cutaway (bridges individual transaction to aggregate proof)
idx_ev_dash = add_input(EVID / "dashboard-crop.png")
fc.append(f"[{idx_ev_dash}:v]format=rgba,fade=t=in:st=28.5:d=0.3:alpha=1,"
          f"fade=t=out:st=30.2:d=0.3:alpha=1[ev_dash]")
fc.append(f"{cur}[ev_dash]overlay=0:480:enable='between(t,28.5,30.51)'[c4_dash]")
cur = "[c4_dash]"

# --- CUE 5 (30.81 - 39.21s): THE PUNCH / PAYOFF & COUNTER ---
cue5_filters = [
    (f"drawtext=fontfile='{ARIAL_BD}':text='THE PAYOFF':fontsize=26:"
    (f"drawtext=fontfile='{ARIAL_BD}':text='THE PAYOFF':expansion=none:fontsize=26:"
     f"fontcolor={MUTED}:x=60:y=520:enable='between(t,30.81,39.21)'"),
    (f"drawtext=fontfile='{ARIAL_BD}':"
     f"text='%{{eif\\:min(6\\,floor((t-30.81)/1.1))\\:d}}':fontsize=180:"
     f"fontcolor={BLUE}:x=60:y=570:enable='between(t,30.81,39.21)'"),
    (f"drawtext=fontfile='{ARIAL_BD}':text='SHOWINGS RECOVERED / WK':fontsize=38:"
    (f"drawtext=fontfile='{ARIAL_BD}':text='SHOWINGS RECOVERED / WK':expansion=none:fontsize=38:"
     f"fontcolor={INK}:x=240:y=650:enable='between(t,30.81,39.21)'"),
    (f"drawtext=fontfile='{ARIAL_BD}':text='= 1 FULL-TIME COORDINATOR ROLE':fontsize=28:"
    (f"drawtext=fontfile='{ARIAL_BD}':text='= 1 FULL-TIME COORDINATOR ROLE':expansion=none:fontsize=28:"
     f"fontcolor={MUTED}:x=240:y=710:enable='between(t,30.81,39.21)'"),
    (f"drawbox=x=60:y=800:w=960:h=14:color={CARD}:t=fill:enable='between(t,30.81,39.21)'"),
    (f"drawbox=x=60:y=800:w='960*min(1\\,(t-30.81)/7.5)':h=14:color={ORANGE}:t=fill:"
     f"enable='between(t,30.81,39.21)'"),
    # Visual Punch Stamp ("BEFORE YOUR COFFEE GETS COLD")
    (f"drawbox=x=60:y=850:w=460:h=52:color={CARD}@0.95:t=fill:enable='between(t,33.5,38.8)'"),
    (f"drawtext=fontfile='{ARIAL_BD}':text='BEFORE YOUR COFFEE GETS COLD':fontsize=24:"
    (f"drawtext=fontfile='{ARIAL_BD}':text='BEFORE YOUR COFFEE GETS COLD':expansion=none:fontsize=24:"
     f"fontcolor={ORANGE}:x=78:y=865:enable='between(t,33.5,38.8)'"),
]
for i, flt in enumerate(cue5_filters):
    lab = f"t5_{i}"
    fc.append(f"{cur}{flt}[{lab}]"); cur = f"[{lab}]"
idx_arrow = add_input(MICRO / "arrow-up.png")
pop_in(idx_arrow, x=60, y=570, size=60, t0=31.2, t1=39.0, label="m5_arr")
node("celebrating", x=670, y=1080, size=280, t0=31.2, t1=39.0, label="node5")

# --- CUE 6 (39.51 - 46.0s): CTA / CLOSING HERO BOOKEND ---
hero_bg(HERO / "cta-hero.mp4", t0=39.51, t1=46.0, fade_out=0.2)
fc.append(f"{cur}drawbox=x=0:y=140:w={W}:h=330:color={CARD}@0.88:t=fill:"
          f"enable='between(t,39.51,46.0)'[t6scrim]")
cur = "[t6scrim]"
for i, flt in enumerate(badge_claim("NEXT STEP", "COMMENT", "SYSTEM.",
                                     BLUE, 39.51, 46.0, y=170)):
    lab = f"t6_{i}"
    fc.append(f"{cur}{flt}[{lab}]"); cur = f"[{lab}]"
fc.append(f"{cur}drawtext=fontfile='{ARIAL_BD}':text='SENDING THE EXACT BLUEPRINT.':fontsize=28:"
          f"fontcolor={MUTED}:x=60:y=450:enable='between(t,39.51,46.0)'[c6sub]")
# Refined floating CTA card container
fc.append(f"{cur}drawbox=x=60:y=110:w=960:h=440:color={CARD}@0.94:t=fill:"
          f"enable='between(t,39.51,46.0)'[t6card_bg]")
cur = "[t6card_bg]"
fc.append(f"{cur}drawbox=x=95:y=145:w=220:h=52:color={CARD}:t=fill:"
          f"enable='between(t,39.51,46.0)'[t6badge_bg]")
cur = "[t6badge_bg]"
fc.append(f"{cur}drawtext=fontfile='{ARIAL_BD}':text='NEXT STEP':expansion=none:fontsize=24:"
          f"fontcolor={MUTED}:x=115:y=160:enable='between(t,39.51,46.0)'[t6badge_txt]")
cur = "[t6badge_txt]"
fc.append(f"{cur}drawtext=fontfile='{ARIAL_BD}':text='COMMENT':expansion=none:fontsize=64:"
          f"fontcolor={INK}:x=95:y=245:enable='between(t,39.51,46.0)'[t6_h1]")
cur = "[t6_h1]"
fc.append(f"{cur}drawtext=fontfile='{ARIAL_BD}':text='SYSTEM.':expansion=none:fontsize=64:"
          f"fontcolor={BLUE}:x=95:y=330:enable='between(t,39.51,46.0)'[t6_h2]")
cur = "[t6_h2]"
hand_underline(x=95, y=405, w_final=320, t0=40.5, dur=0.5, color=ORANGE, label="ul3")
fc.append(f"{cur}drawtext=fontfile='{ARIAL_BD}':text='SENDING THE EXACT BLUEPRINT.':expansion=none:fontsize=26:"
          f"fontcolor={MUTED}:x=95:y=465:enable='between(t,39.51,46.0)'[c6sub]")
cur = "[c6sub]"
hand_underline(x=60, y=422, w_final=340, t0=40.5, dur=0.5, color=ORANGE, label="ul3")
node("running", x=680, y=1100, size=270, t0=40.0, t1=46.0, label="node6")

# --- Human-touch pass (Camera drift + grain gated ONLY to photoreal hero segments) ---
# Hero 1 (0.0-5.3s) and Hero 2 (39.51-46.0s). Flat UI section stays pixel-static!
GATE = ("if(lt(t,4.9),1,"
        "if(lt(t,5.3),(5.3-t)/0.4,"
        "if(lt(t,39.51),0,"
        "if(lt(t,39.91),(t-39.51)/0.4,1))))")
fc.append(f"{cur}scale=1112:1978,"
          f"crop=1080:1920:x='16+10*sin(2*PI*t/23)*({GATE})':"
          f"y='29+6*cos(2*PI*t/29)*({GATE})',"
          f"noise=alls=4:allf=t+u:enable='lte(t,5.3)+gte(t,39.51)'[human]")
cur = "[human]"

# --- Subtitle Burn-In ---
fonts_dir = HERE.parent.parent.parent / "assets" / "fonts" / "google"
fc.append(f"{cur}subtitles='{ff_path(CAPTIONS)}':fontsdir='{ff_path(fonts_dir)}'[final]")

flat_inputs = [arg for group in inputs for arg in group]
cmd = [FF, "-y", "-loglevel", "error", *flat_inputs, "-filter_complex", ";".join(fc),
       "-map", "[final]", "-t", str(TOTAL), "-r", "30",
       "-c:v", "libx264", "-crf", "20", "-preset", "medium", "-pix_fmt", "yuv420p",
       str(OUT)]

print(f"Building ep002-visual.mp4 (The Fourteen Minutes — 46.0s render) ...")
r = subprocess.run(cmd, capture_output=True, text=True)
if r.returncode != 0:
    print("FFMPEG ERROR:")
    print(r.stderr[-4000:])
    raise SystemExit("FFMPEG FAILED")
print(f"-> {OUT} ({OUT.stat().st_size // 1024} KB)")

