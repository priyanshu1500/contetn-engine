import os
import json
import math
import subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CAPTIONS_FILE = os.path.join(ROOT_DIR, "captions.json")
STAGE_DIR = os.path.join(ROOT_DIR, "stage_assets")
MASCOT_DIR = os.path.join(ROOT_DIR, "mascot")
AUDIO_FILE = os.path.join(ROOT_DIR, "narration", "vo.mp3")
OUTPUT_VIDEO = os.path.join(ROOT_DIR, "delivery", "ep003-v1.0-FINAL.mp4")

WIDTH, HEIGHT = 1080, 1920
FPS = 60

# Palette
BG_COLOR = (245, 235, 221, 255)       # #F5EBDD Warm Cream
HEADER_BG = (255, 255, 255, 255)
HEADER_BORDER = (229, 213, 192, 255)  # #E5D5C0
INK_TEXT = (65, 51, 51, 255)          # #413333
COBALT = (78, 113, 255, 255)          # #4E71FF
CORAL = (242, 118, 94, 255)           # #F2765E
SUBTITLE_COLOR = (200, 106, 75, 255)  # #C86A4B Terracotta
TRACK_BG = (225, 210, 190, 255)
GREEN = (40, 200, 110, 255)
GOLD = (255, 193, 37, 255)
WHITE = (255, 255, 255, 255)

def get_fonts():
    try:
        f_head1 = ImageFont.truetype("arialbd.ttf", 34)
        f_head2 = ImageFont.truetype("arialbd.ttf", 26)
        f_sub = ImageFont.truetype("georgiab.ttf", 52)
        f_sub = ImageFont.truetype("georgiab.ttf", 44)
        f_small = ImageFont.truetype("arialbd.ttf", 20)
    except:
        f_head1 = ImageFont.load_default()
        f_head2 = f_head1
        f_sub = f_head1
        f_small = f_head1
    return f_head1, f_head2, f_sub, f_small

def load_mascot_poses():
    poses = {}
    pose_files = {
        "thinking": "node-thinking.png",
        "working": "node-working.png",
        "idea": "node-idea.png",
        "running": "node-running.png",
        "celebrating": "node-celebrating.png",
        "pointing": "node-pointing.png"
    }
    for name, fname in pose_files.items():
        p = os.path.join(MASCOT_DIR, fname)
        if os.path.exists(p):
            img = Image.open(p).convert("RGBA")
            w, h = img.size
            ratio = 320 / float(h)
            new_size = (int(w * ratio), 320)
            resized = img.resize(new_size, Image.Resampling.LANCZOS)
            
            # Create a glowing rim/outline around Node so he pops against dark stage
            # Create a glowing rim/outline around Node
            glow = Image.new("RGBA", (new_size[0]+24, new_size[1]+24), (0,0,0,0))
            alpha = resized.split()[3]
            # White mask
            white_mask = Image.new("RGBA", new_size, (255, 255, 255, 200))
            white_mask = Image.new("RGBA", new_size, (255, 255, 255, 220))
            white_mask.putalpha(alpha)
            glow.paste(white_mask, (12, 12), white_mask)
            glow = glow.filter(ImageFilter.GaussianBlur(6))
            glow.paste(resized, (12, 12), resized)
            poses[name] = glow
    return poses

def load_stage_images():
    stages = []
    import glob
    for i in range(1, 6):
        matches = glob.glob(os.path.join(STAGE_DIR, f"stage{i}_*.png"))
        if matches:
            stages.append(Image.open(matches[0]).convert("RGBA"))
    return stages

def draw_check_mark(draw, cx, cy, size, color):
    # Vector Checkmark
    p1 = (cx - size * 0.4, cy)
    p2 = (cx - size * 0.1, cy + size * 0.35)
    p3 = (cx + size * 0.45, cy - size * 0.35)
    draw.line([p1, p2], fill=color, width=3)
    draw.line([p2, p3], fill=color, width=3)

def draw_star(draw, cx, cy, r, color):
    # Vector 5-point star
    pts = []
    for i in range(10):
        angle = i * math.pi / 5 - math.pi / 2
        radius = r if i % 2 == 0 else r * 0.45
        pts.append((cx + radius * math.cos(angle), cy + radius * math.sin(angle)))
    draw.polygon(pts, fill=color)

def wrap_words_into_two_lines(words, max_chars=32):
    if len(words) <= 3:
        return [" ".join(words)]
    
    # Split words into 2 visually balanced lines
    best_diff = float('inf')
    split_idx = len(words) // 2
    for i in range(1, len(words)):
        l1 = " ".join(words[:i])
        l2 = " ".join(words[i:])
        diff = abs(len(l1) - len(l2))
        if diff < best_diff:
            best_diff = diff
            split_idx = i
            
    return [" ".join(words[:split_idx]), " ".join(words[split_idx:])]

def build_video():
    with open(CAPTIONS_FILE, "r", encoding="utf-8") as f:
        meta = json.load(f)
        
    total_duration = meta["total_duration"]
    cues = meta["cues"]
    total_frames = int(total_duration * FPS)
    
    print(f"Rendering {total_frames} frames ({total_duration:.2f}s at {FPS}fps)...")
    
    f_head1, f_head2, f_sub, f_small = get_fonts()
    mascot_poses = load_mascot_poses()
    stage_images = load_stage_images()
    
    os.makedirs(os.path.dirname(OUTPUT_VIDEO), exist_ok=True)
    cmd = [
        "ffmpeg", "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{WIDTH}x{HEIGHT}",
        "-pix_fmt", "rgba",
        "-r", str(FPS),
        "-i", "-",
        "-i", AUDIO_FILE,
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        OUTPUT_VIDEO
    ]
    
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    checkpoints = [140, 320, 520, 720, 940]
    
    for frame_idx in range(total_frames):
        current_time = frame_idx / float(FPS)
        
        active_cue = cues[-1]
        for c in cues:
            if c["start"] <= current_time < c["end"]:
                active_cue = c
                break
            elif current_time < cues[0]["start"]:
                active_cue = cues[0]
                break
                
        cue_idx = active_cue["id"] - 1
        # 1. Solid Cue Resolution: Hold the current cue until the next cue starts
        active_cue = cues[0]
        active_idx = 0
        for i, c in enumerate(cues):
            if i == len(cues) - 1:
                if current_time >= c["start"]:
                    active_cue = c
                    active_idx = i
            else:
                next_c = cues[i + 1]
                if c["start"] <= current_time < next_c["start"]:
                    active_cue = c
                    active_idx = i
                    break
                    
        cue_idx = active_idx
        
        # 1. Base Canvas
        # 2. Base Canvas
        canvas = Image.new("RGBA", (WIDTH, HEIGHT), BG_COLOR)
        draw = ImageDraw.Draw(canvas)
        
        # 2. Top Gamified Level Tracker
        # 3. Top Gamified Level Tracker
        bar_y = 115
        draw.rounded_rectangle([100, bar_y-6, 980, bar_y+6], radius=6, fill=TRACK_BG)
        
        total_progress_pct = min(1.0, current_time / float(total_duration))
        filled_x = int(140 + total_progress_pct * (940 - 140))
        draw.rounded_rectangle([100, bar_y-6, filled_x, bar_y+6], radius=6, fill=CORAL)
        
        for cp_i, cp_x in enumerate(checkpoints):
            if cp_i < 4:
                if filled_x >= cp_x:
                    draw.ellipse([cp_x-18, bar_y-18, cp_x+18, bar_y+18], fill=GREEN, outline=WHITE, width=2)
                    draw_check_mark(draw, cp_x, bar_y, 14, WHITE)
                else:
                    draw.ellipse([cp_x-14, bar_y-14, cp_x+14, bar_y+14], fill=TRACK_BG, outline=WHITE, width=2)
                    draw.text((cp_x-5, bar_y-10), str(cp_i+1), fill=INK_TEXT, font=f_small)
            else:
                if filled_x >= cp_x:
                    draw.ellipse([cp_x-22, bar_y-22, cp_x+22, bar_y+22], fill=GOLD, outline=WHITE, width=3)
                    draw_star(draw, cp_x, bar_y, 12, INK_TEXT)
                else:
                    draw.ellipse([cp_x-18, bar_y-18, cp_x+18, bar_y+18], fill=TRACK_BG, outline=WHITE, width=2)
                    draw_star(draw, cp_x, bar_y, 9, INK_TEXT)
                    
        # 3. Floating Header Pill Badge
        # 4. Floating Header Pill Badge
        badge_x1, badge_y1, badge_x2, badge_y2 = 100, 165, 980, 285
        draw.rounded_rectangle([badge_x1+4, badge_y1+6, badge_x2+4, badge_y2+6], radius=28, fill=(0, 0, 0, 18))
        draw.rounded_rectangle([badge_x1, badge_y1, badge_x2, badge_y2], radius=28, fill=HEADER_BG, outline=HEADER_BORDER, width=3)
        
        # Clean Starburst & Titles
        draw_star(draw, 145, badge_y1 + 42, 12, CORAL)
        draw.text((170, badge_y1 + 22), active_cue["header_1"].replace("✦ ", "").replace("★ ", ""), fill=INK_TEXT, font=f_head1)
        draw.text((170, badge_y1 + 70), active_cue["header_2"], fill=CORAL, font=f_head2)
        
        # 4. Central Stage Container
        # 5. Central Stage Container (with subtle vertical float)
        float_y = int(math.sin(current_time * 2.8) * 8)
        stage_x, stage_y = 60, 330 + float_y
        
        draw.rounded_rectangle([stage_x+6, stage_y+12, stage_x+960+6, stage_y+900+12], radius=36, fill=(0, 0, 0, 32))
        
        # Smooth crossfade on stage entry (200ms ease-out)
        time_into_cue = current_time - active_cue["start"]
        if cue_idx < len(stage_images):
            canvas.paste(stage_images[cue_idx], (stage_x, stage_y), stage_images[cue_idx])
            curr_stage_img = stage_images[cue_idx]
            if 0 <= time_into_cue < 0.25 and cue_idx > 0:
                # Blend with previous stage
                prev_stage_img = stage_images[cue_idx - 1]
                alpha_factor = min(1.0, time_into_cue / 0.25)
                canvas.paste(prev_stage_img, (stage_x, stage_y), prev_stage_img)
                # Blend current stage on top
                blended = curr_stage_img.copy()
                b_alpha = blended.split()[3].point(lambda p: int(p * alpha_factor))
                blended.putalpha(b_alpha)
                canvas.paste(blended, (stage_x, stage_y), blended)
            else:
                canvas.paste(curr_stage_img, (stage_x, stage_y), curr_stage_img)
            
        # 5. Mascot Placement
        # 6. Mascot Placement (Positioned cleanly at x=740 so zero text overlap occurs)
        # 6. Mascot Placement (Positioned cleanly at x=740)
        mascot_key = "thinking"
        if cue_idx == 1:
            mascot_key = "working"
        elif cue_idx == 2:
            mascot_key = "idea"
        elif cue_idx == 3:
            mascot_key = "running"
        elif cue_idx == 4:
            mascot_key = "celebrating"
            
        if mascot_key in mascot_poses:
            m_img = mascot_poses[mascot_key]
            m_hop = int(math.sin(current_time * 4.0) * 6)
            canvas.paste(m_img, (720, stage_y + 600 + m_hop), m_img)
            canvas.paste(m_img, (740, stage_y + 580 + m_hop), m_img)
            
        # 6. Subtitles
        # 7. Subtitles
        sub_y = 1420
        # 7. Subtitles in TWO Balanced Centered Lines
        # 7. Subtitles in ONLY TWO Balanced Centered Lines
        full_text = active_cue["text"]
        words = full_text.split()
        
        cue_progress = (current_time - active_cue["start"]) / max(0.1, active_cue["duration"])
        cue_progress = max(0.0, min(1.0, cue_progress))
        active_word_count = max(1, int(cue_progress * len(words)))
        
        chunk_size = 5
        # 8 words per chunk across 2 lines
        chunk_size = 8
        curr_chunk_idx = (active_word_count - 1) // chunk_size
        chunk_start = curr_chunk_idx * chunk_size
        chunk_words = words[chunk_start:chunk_start + chunk_size]
        display_str = " ".join(chunk_words)
        
        bbox = draw.textbbox((0, 0), display_str, font=f_sub)
        text_w = bbox[2] - bbox[0]
        text_x = (WIDTH - text_w) // 2
        sub_lines = wrap_words_into_two_lines(chunk_words)
        
        draw.rounded_rectangle([text_x - 24, sub_y - 12, text_x + text_w + 24, sub_y + 80], radius=18, fill=(255, 255, 255, 230))
        draw.text((text_x, sub_y), display_str, fill=SUBTITLE_COLOR, font=f_sub)
        # Calculate line widths and heights
        line_metrics = []
        max_line_w = 0
        for line in sub_lines:
            bbox = draw.textbbox((0, 0), line, font=f_sub)
            lw = bbox[2] - bbox[0]
            lh = bbox[3] - bbox[1]
            line_metrics.append((line, lw, lh))
            if lw > max_line_w:
                max_line_w = lw
                
        # Subtitle Pill Box
        sub_box_y = 1380
        box_w = max(400, max_line_w + 64)
        box_h = 75 if len(sub_lines) == 1 else 135
        box_x = (WIDTH - box_w) // 2
        
        # 7. Confetti on CTA
        # Draw Drop Shadow + Pill
        draw.rounded_rectangle([box_x+3, sub_box_y+5, box_x+box_w+3, sub_box_y+box_h+5], radius=22, fill=(0, 0, 0, 16))
        draw.rounded_rectangle([box_x, sub_box_y, box_x+box_w, sub_box_y+box_h], radius=22, fill=(255, 255, 255, 245), outline=HEADER_BORDER, width=2)
        
        # Draw centered text lines
        if len(sub_lines) == 1:
            line_text, lw, lh = line_metrics[0]
            lx = (WIDTH - lw) // 2
            ly = sub_box_y + 14
            draw.text((lx, ly), line_text, fill=SUBTITLE_COLOR, font=f_sub)
        else:
            # Line 1
            l1_text, l1_w, _ = line_metrics[0]
            l1_x = (WIDTH - l1_w) // 2
            l1_y = sub_box_y + 14
            draw.text((l1_x, l1_y), l1_text, fill=SUBTITLE_COLOR, font=f_sub)
            
            # Line 2
            l2_text, l2_w, _ = line_metrics[1]
            l2_x = (WIDTH - l2_w) // 2
            l2_y = sub_box_y + 68
            draw.text((l2_x, l2_y), l2_text, fill=SUBTITLE_COLOR, font=f_sub)
        
        # 8. Confetti on CTA
        if cue_idx == 4:
            np.random.seed(int(frame_idx * 1.5))
            confetti_colors = [COBALT, CORAL, GOLD, GREEN]
            for _ in range(40):
                cx = np.random.randint(60, 1020)
                cy = np.random.randint(80, 1800)
                c_color = confetti_colors[np.random.randint(0, len(confetti_colors))]
                draw.rounded_rectangle([cx, cy, cx+14, cy+8], radius=3, fill=c_color)
                
        raw_bytes = canvas.tobytes()
        process.stdin.write(raw_bytes)
        
        if frame_idx % (FPS * 5) == 0:
            pct = int((frame_idx / float(total_frames)) * 100)
            print(f"Progress: {pct}% ({frame_idx}/{total_frames} frames)")
            
    process.stdin.close()
    process.wait()
    print(f"Done! Master video saved to: {OUTPUT_VIDEO}")

if __name__ == "__main__":
    build_video()
