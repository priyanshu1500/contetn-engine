"""
build_edl.py — Edit Decision List (EDL) Compiler for Episode D6:
"The $1M Blunder: Yahoo vs. Google".
Full MetroMedia investigative architecture:
- 100% Primary Proof Assets & Real Video Clips (Vintage 90s Tech Office, Yahoo Portal, Google Speed Card, Larry Page, Sergey Brin)
- Multi-Font Kinetic Typography Switching (Sans, Serif Italic, Condensed Display, Mono)
- Stark High-Key Optical Contrast Reset Slides (#FFFFFF / #0B0B0C)
- Polaroid Pinboard Frame with Authentic Handwritten Script
- Spring-Damped Physical Pop Dynamics
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ENGINE_DIR = os.path.normpath(os.path.join(HERE, '..', 'engine'))
sys.path.append(ENGINE_DIR)
from editorial_edl import format_caption_chunks

words = json.load(open(os.path.join(HERE, 'words_timing.json'), encoding='utf-8'))

voice_dur = words[-1]['end'] + 0.6
DUR = round(voice_dur, 1)

def find_word_time(target, after=0.0):
    t_low = target.lower().rstrip('.,!?\"')
    for w in words:
        if w['start'] >= after and t_low in w['word'].lower():
            return w['start']
    return None

def find_word_end(target, after=0.0):
    t_low = target.lower().rstrip('.,!?\"')
    for w in words:
        if w['start'] >= after and t_low in w['word'].lower():
            return w['end']
    return None

# Narrative beat timestamps
t_google = find_word_end('Google', 0.0) or 2.30
t_offer1 = find_word_end('$1,000,000', t_google) or 6.03
t_offer2 = find_word_end('$3,000,000,000', t_offer1) or 9.25
t_times = find_word_end('times', t_offer2) or 11.71
t_world = find_word_end('world', t_times) or 15.50
t_bucks = find_word_end('bucks', t_world) or 23.50
t_boardroom = find_word_end('boardroom', t_bucks) or 27.50
t_seconds = find_word_end('SECONDS', t_boardroom) or 34.20
t_horoscopes = find_word_end('horoscopes', t_seconds) or 42.50
t_empire = find_word_end('$1 Trillion', t_horoscopes) or 48.50
t_way = find_word_end('way', t_empire) or 52.80
t_won = find_word_end('won', t_way) or 57.50
t_reason = find_word_end('reason', t_won) or 64.50
t_hours = find_word_end('hours', t_reason) or 68.00

shots = [
    # Shot 1: The Asymmetric Hook (Vintage 90s Tech Office)
    {
        "id": "s1", "kind": "video", "src": "clips/vintage_office_90s.mp4",
        "t0": 0.0, "t1": t_google, "from": 1.0, "scale": 1.06, "grade": "contrast(1.15) brightness(0.95)", "scrim": True,
        "job": "hook:asymmetric_decision"
    },
    # Shot 2: Stark Rejection Comparison Card ($1M vs $3B)
    {
        "id": "s2", "kind": "still", "src": "img/yahoo_google_rejection_card.png",
        "t0": t_google, "t1": t_times, "fx": 0.5, "fy": 0.5, "scale": 1.04,
        "job": "proof:boardroom_rejections"
    },
    # Shot 3: Pure White Optical Reset
    {
        "id": "s3", "kind": "stark", "t0": t_times, "t1": t_world,
        "stark": {
            "bg": "white", "text": "THE FIRST REJECTION", "tag": "STANFORD UNIVERSITY // 1998",
            "sub": "Larry Page & Sergey Brin walk into Yahoo HQ."
        },
        "job": "optical_reset:white"
    },
    # Shot 4: Larry Page Archival Polaroid Card
    {
        "id": "s4", "kind": "polaroid", "t0": t_world, "t1": t_bucks,
        "polaroid": {
            "src": "img/larry_page.jpg", "label": "Larry Page (Stanford CS, 1998)",
            "rot": -2.0, "scale": 1.0
        },
        "job": "photo:founder_larry"
    },
    # Shot 5: Boardroom Laughter (Cinematic Dark Boardroom)
    {
        "id": "s5", "kind": "video", "src": "clips/succession_boardroom.mp4",
        "t0": t_bucks, "t1": t_boardroom, "from": 0.0, "scale": 1.08, "scrim": True,
        "job": "broll:boardroom_rejection"
    },
    # Shot 6: Google 3-Second Speed Inversion Card
    {
        "id": "s6", "kind": "still", "src": "img/google_speed_card.png",
        "t0": t_boardroom, "t1": t_seconds, "fx": 0.5, "fy": 0.5, "scale": 1.05,
        "job": "proof:speed_metric"
    },
    # Shot 7: Yahoo Cluttered Portal Trap
    {
        "id": "s7", "kind": "still", "src": "img/yahoo_portal_trap_card.png",
        "t0": t_seconds, "t1": t_horoscopes, "fx": 0.5, "fy": 0.5, "scale": 1.04,
        "job": "proof:portal_trap"
    },
    # Shot 8: Trillion Dollar Divergence Card
    {
        "id": "s8", "kind": "still", "src": "img/trillion_divergence_card.png",
        "t0": t_horoscopes, "t1": t_way, "fx": 0.5, "fy": 0.5, "scale": 1.04,
        "job": "stat:divergence"
    },
    # Shot 9: Stark Black Optical Reset
    {
        "id": "s9", "kind": "stark", "t0": t_way, "t1": t_won,
        "stark": {
            "bg": "#0B0B0C", "text": "THEY REJECTED THE IDEA THAT WON.", "tag": "HISTORICAL POST-MORTEM",
            "sub": "Yahoo didn't miss Google by accident."
        },
        "job": "optical_reset:black"
    },
    # Shot 10: Modern Autonomous Agency Velocity (Cursor IDE)
    {
        "id": "s10", "kind": "video", "src": "clips/cursor_ide.mp4",
        "t0": t_won, "t1": t_reason, "from": 0.0, "scale": 1.05, "scrim": True,
        "job": "tech:autonomous_velocity"
    },
    # Shot 11: Stark White Moral Slide ("THE FASTER MACHINE ALWAYS WINS")
    {
        "id": "s11", "kind": "still", "src": "img/faster_machine_lesson.png",
        "t0": t_reason, "t1": DUR, "fx": 0.5, "fy": 0.5, "scale": 1.04,
        "job": "moral:agency_lesson"
    }
]

# Generate multi-font kinetic typography chunks
text_chunks = format_caption_chunks(words, max_words=3)

edl = {
    "duration": DUR,
    "shots": shots,
    "text": text_chunks
}

out_path = os.path.join(HERE, 'build', 'edl.json')
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(edl, f, indent=2)

print(f"[EDLBuilder] Successfully compiled {len(shots)} shots and {len(text_chunks)} kinetic caption bursts into {out_path} (Duration: {DUR}s).")

