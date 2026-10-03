"""Shared synthesized sound-layer library for DocReel episode mixes — zero downloads, all ffmpeg lavfi.
Import into an episode's mix.py: `from foley import LAYERS, PAPER, TICK` etc.
Each layer is an ffmpeg lavfi filter-graph string suitable for `-f lavfi -i "<layer>"`.
"""

PAPER = "anoisesrc=d=0.6:c=white:a=0.55:r=48000,highpass=f=1800,lowpass=f=8000,tremolo=f=32:d=0.95,afade=t=in:d=0.02,afade=t=out:st=0.35:d=0.25"
TICK = "sine=f=1500:d=0.04:r=48000,afade=t=out:st=0.01:d=0.03"

# --- v2 additions (Big Short / Dirty Money register: archival, investigative texture) ---

# Tape hiss: a steady, filtered noise bed under archival-tagged footage. Loop under a whole shot.
def TAPE_HISS(dur=3.0, level=0.5):
    return f"anoisesrc=d={dur}:c=pink:a={level},highpass=f=3000,lowpass=f=11000,volume=0.5,afade=t=in:d=0.15,afade=t=out:st={max(0,dur-0.2)}:d=0.2"

# Projector hum: a low drone with a subtle mechanical flutter, for "archive footage" establishing beats.
def PROJECTOR_HUM(dur=2.5):
    return (f"sine=f=48:d={dur}:r=48000,volume=0.35,tremolo=f=4.2:d=0.25,afade=t=in:d=0.2,afade=t=out:st={max(0,dur-0.3)}:d=0.3")

# Archive click: a short, dry transient — one per evidence-card entrance (like a shutter/file-stamp click).
ARCHIVE_CLICK = "anoisesrc=d=0.06:c=white:a=0.9,highpass=f=2500,afade=t=out:st=0.01:d=0.05"

# Subtle heartbeat pulse: two low thumps per beat, for escalation/tension energy bands. Loop under a shot.
def HEARTBEAT(dur=4.0, bpm=58):
    period = 60 / bpm
    return (f"sine=f=55:d={dur}:r=48000,volume='0.22*lt(mod(t\\,{period:.3f})\\,0.12)+0.10*between(mod(t\\,{period:.3f})\\,0.20\\,0.30)',afade=t=in:d=0.1,afade=t=out:st={max(0,dur-0.2)}:d=0.2")

# Room tone: a very quiet brown-noise bed for the whole episode (already used in prior episodes; kept here for reuse).
def ROOM_TONE(dur):
    return f"anoisesrc=d={dur}:c=brown:a=0.25:r=48000,lowpass=f=450"

LAYERS = {
    'paper': PAPER, 'tick': TICK, 'tape_hiss': TAPE_HISS, 'projector_hum': PROJECTOR_HUM,
    'archive_click': ARCHIVE_CLICK, 'heartbeat': HEARTBEAT, 'room_tone': ROOM_TONE,
}


def auto_layers_for_shot(s):
    """Suggested foley for a shot, by kind/energy/tags. Returns a list of (lavfi_string, at_seconds, volume)."""
    out = []
    t0 = s['t0']
    if s['kind'] == 'evidence':
        out.append((PAPER, round(t0 - 0.02, 3), 0.45))
        out.append((ARCHIVE_CLICK, round(t0 + 0.05, 3), 0.6))
    if s['kind'] in ('title', 'stat', 'year', 'wordcard', 'cta', 'label'):
        out.append((PAPER, round(t0 - 0.02, 3), 0.4))
    if s.get('archival'):
        out.append((TAPE_HISS(s['t1'] - t0), t0, 0.35))
        out.append((PROJECTOR_HUM(min(2.5, s['t1'] - t0)), t0, 0.3))
    if s.get('energy') == 'escalation':
        out.append((HEARTBEAT(s['t1'] - t0), t0, 0.5))
    return out
