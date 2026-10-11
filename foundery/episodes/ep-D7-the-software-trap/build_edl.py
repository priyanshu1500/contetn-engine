"""
build_edl.py — Master EDL Compiler for Episode D7: "The Software Trap".
Implements Attention Compound standards:
- 17 authentic archival shots & bespoke evidence cards (NO AI SLOP)
- Centered glowing serif-italic thought-unit subtitles
- Optical contrast resets (Stark white slides every 15-20s)
- Analog CRT scanlines & chromatic camera dynamics
"""
import os, json

HERE = os.path.dirname(os.path.abspath(__file__))
PHRASES_PATH = os.path.join(HERE, 'cleaned_phrases.json')
OUT_EDL = os.path.join(HERE, 'build', 'edl.json')

with open(PHRASES_PATH, encoding='utf-8') as f:
    phrases = json.load(f)

# Build Shots Timeline (Total ~98.0s)
shots = [
    # Shot 1: The Inverted Paradox Hook (0.0s - 5.8s)
    {
        "id": "s01",
        "kind": "video",
        "src": "clips/huang.mp4",
        "from": 2.0,
        "t0": 0.0,
        "t1": 5.8,
        "push": 0.08,
        "zoom": 1.02,
        "crt": True,
        "scrim": True,
        "job": "hook_paradox"
    },
    # Shot 2: The Tech Giants Warning (5.8s - 10.2s)
    {
        "id": "s02",
        "kind": "video",
        "src": "clips/jensen_keynote.mp4",
        "from": 1.0,
        "t0": 5.8,
        "t1": 10.2,
        "push": 0.06,
        "zoom": 1.03,
        "crt": True,
        "scrim": True,
        "job": "leather_jacket_stage"
    },
    # Shot 3: Optical Reset — Stark White Slide (10.2s - 15.5s)
    {
        "id": "s03",
        "kind": "stark",
        "t0": 10.2,
        "t1": 15.5,
        "stark": {
            "bg": "white",
            "tag": "CONFIDENTIAL // SILICON VALLEY INITIATIVE",
            "text": "THE $14 TRILLION REVOLT",
            "sub": "EVERY TECH GIANT SET OUT TO KILL NVIDIA",
            "size": 115
        },
        "job": "optical_reset_white"
    },
    # Shot 4: Big Tech Coalition Card (15.5s - 23.5s)
    {
        "id": "s04",
        "kind": "still",
        "src": "img/coalition_card.png",
        "t0": 15.5,
        "t1": 23.5,
        "push": 0.04,
        "zoom": 1.0,
        "scrim": False,
        "job": "coalition_manifest"
    },
    # Shot 5: Semiconductor Cleanroom Fab (23.5s - 30.5s)
    {
        "id": "s05",
        "kind": "video",
        "src": "clips/semiconductor_wafer.mp4",
        "from": 0.0,
        "t0": 23.5,
        "t1": 30.5,
        "push": 0.07,
        "zoom": 1.05,
        "crt": True,
        "scrim": True,
        "job": "chip_fabrication"
    },
    # Shot 6: Corporate Boardroom Revolt (30.5s - 35.2s)
    {
        "id": "s06",
        "kind": "video",
        "src": "clips/succession_boardroom.mp4",
        "from": 3.0,
        "t0": 30.5,
        "t1": 35.2,
        "push": 0.06,
        "zoom": 1.04,
        "crt": True,
        "scrim": True,
        "job": "boardroom_revolt"
    },
    # Shot 7: The Fatal Mistake Card (35.2s - 40.5s)
    {
        "id": "s07",
        "kind": "still",
        "src": "img/fatal_mistake_card.png",
        "t0": 35.2,
        "t1": 40.5,
        "push": 0.04,
        "zoom": 1.0,
        "scrim": False,
        "job": "fatal_mistake_cuda"
    },
    # Shot 8: Data Center Server Corridor (40.5s - 49.5s)
    {
        "id": "s08",
        "kind": "video",
        "src": "clips/datacenter_corridor.mp4",
        "from": 1.0,
        "t0": 40.5,
        "t1": 49.5,
        "push": 0.08,
        "zoom": 1.02,
        "crt": True,
        "scrim": True,
        "job": "datacenter_infinity"
    },
    # Shot 9: CNBC Newsroom Anchor Panel (49.5s - 54.5s)
    {
        "id": "s09",
        "kind": "video",
        "src": "clips/cnbc_ceo.mp4",
        "from": 2.0,
        "t0": 49.5,
        "t1": 54.5,
        "push": 0.05,
        "zoom": 1.03,
        "crt": True,
        "scrim": True,
        "job": "news_anchor_fallout"
    },
    # Shot 10: Silicon Valley Tech Campus (54.5s - 59.0s)
    {
        "id": "s10",
        "kind": "video",
        "src": "clips/tech_campus.mp4",
        "from": 2.0,
        "t0": 54.5,
        "t1": 59.0,
        "push": 0.06,
        "zoom": 1.04,
        "crt": True,
        "scrim": True,
        "job": "google_campus_dependent"
    },
    # Shot 11: Optical Reset — Microsoft Sidelined (59.0s - 63.5s)
    {
        "id": "s11",
        "kind": "stark",
        "t0": 59.0,
        "t1": 63.5,
        "stark": {
            "bg": "white",
            "tag": "REDMOND, WA // INTERNAL MEMO",
            "text": "MICROSOFT: SIDELINED",
            "sub": "MAIA SILICON DELAYED // FORCED BACK TO H100s",
            "size": 120
        },
        "job": "optical_reset_microsoft"
    },
    # Shot 12: Meta Zuck Cluster Procurement Card (63.5s - 69.0s)
    {
        "id": "s12",
        "kind": "still",
        "src": "img/zuck_cluster_card.png",
        "t0": 63.5,
        "t1": 69.0,
        "push": 0.04,
        "zoom": 1.0,
        "scrim": False,
        "job": "zuck_capitulation"
    },
    # Shot 13: Jensen Trophy GPU on Stage (69.0s - 75.5s)
    {
        "id": "s13",
        "kind": "video",
        "src": "clips/jensen_keynote.mp4",
        "from": 7.0,
        "t0": 69.0,
        "t1": 75.5,
        "push": 0.07,
        "zoom": 1.04,
        "crt": True,
        "scrim": True,
        "job": "single_man_leather_jacket"
    },
    # Shot 14: Vintage 1990s PC Gaming Trade Show (75.5s - 80.0s)
    {
        "id": "s14",
        "kind": "video",
        "src": "clips/vintage_office_90s.mp4",
        "from": 0.5,
        "t0": 75.5,
        "t1": 80.0,
        "push": 0.05,
        "zoom": 1.03,
        "crt": True,
        "scrim": True,
        "job": "vintage_graphics_vendor"
    },
    # Shot 15: Market Cap Divergence Card — $3.4T (80.0s - 86.5s)
    {
        "id": "s15",
        "kind": "still",
        "src": "img/valuation_card.png",
        "t0": 80.0,
        "t1": 86.5,
        "push": 0.04,
        "zoom": 1.0,
        "scrim": False,
        "job": "trillion_valuation_divergence"
    },
    # Shot 16: Data Center Red Alert (86.5s - 91.5s)
    {
        "id": "s16",
        "kind": "video",
        "src": "clips/datacenter_corridor.mp4",
        "from": 6.0,
        "t0": 86.5,
        "t1": 91.5,
        "push": 0.06,
        "zoom": 1.04,
        "crt": True,
        "scrim": True,
        "job": "write_him_another_check"
    },
    # Shot 17: Philosophical Conclusion (91.5s - 98.0s)
    {
        "id": "s17",
        "kind": "video",
        "src": "clips/huang.mp4",
        "from": 12.0,
        "t0": 91.5,
        "t1": 98.0,
        "push": 0.05,
        "zoom": 1.02,
        "crt": True,
        "scrim": True,
        "job": "toll_booth_climax"
    }
]

# Convert phrases into Remotion `text` cues with Attention Compound centered layout
text_cues = []
for p in phrases:
    # Build word item for each token
    tokens = p['text'].split()
    token_dur = (p['end'] - p['start']) / max(1, len(tokens))
    
    words_arr = []
    for idx, t in enumerate(tokens):
        t_start = round(p['start'] + idx * token_dur, 3)
        words_arr.append({
            "w": t,
            "t": t_start,
            "fontKind": p['fontKind'],
            "color": "#FFFFFF",
            "box": p['box']
        })
        
    text_cues.append({
        "t0": p['start'],
        "t1": p['end'],
        "layout": "center",  # Chest-level Attention Compound placement
        "words": words_arr
    })

edl_data = {
    "title": "Episode D7: The Software Trap (Nvidia CUDA & Big Tech)",
    "duration": 98.0,
    "fps": 24,
    "width": 1080,
    "height": 1920,
    "specks": True,
    "shots": shots,
    "text": text_cues,
    "fadeOut": [96.5, 98.0]
}

os.makedirs(os.path.dirname(OUT_EDL), exist_ok=True)
with open(OUT_EDL, 'w', encoding='utf-8') as f:
    json.dump(edl_data, f, indent=2)

print(f"EDL compiled successfully: {OUT_EDL}")
print(f"Total shots: {len(shots)} | Total text cues: {len(text_cues)} | Duration: {edl_data['duration']}s")

