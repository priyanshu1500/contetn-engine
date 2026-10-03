import os
import math
from PIL import Image, ImageDraw, ImageFont

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
STAGE_DIR = os.path.join(ROOT_DIR, "stage_assets")
os.makedirs(STAGE_DIR, exist_ok=True)

# Container Stage dimensions
STAGE_W = 960
STAGE_H = 900

# Color Tokens
STAGE_BG = (13, 35, 46, 255)       # #0D232E Deep Teal/Navy
STAGE_BG = (13, 35, 46, 255)         # #0D232E Deep Teal/Navy
CONTAINER_BORDER = (28, 64, 82, 255) # #1C4052
WHITE = (255, 255, 255, 255)
INK_DARK = (65, 51, 51, 255)       # #413333
COBALT = (78, 113, 255, 255)       # #4E71FF
CORAL = (242, 118, 94, 255)        # #F2765E
GREEN = (40, 200, 110, 255)        # #28C86E
RED = (255, 75, 75, 255)           # #FF4B4B
GOLD = (255, 193, 37, 255)         # #FFC125
INK_DARK = (65, 51, 51, 255)         # #413333
COBALT = (78, 113, 255, 255)         # #4E71FF
CORAL = (242, 118, 94, 255)          # #F2765E
GREEN = (40, 200, 110, 255)          # #28C86E
RED = (255, 75, 75, 255)             # #FF4B4B
GOLD = (255, 193, 37, 255)           # #FFC125
MUTED_TEXT = (140, 175, 195, 255)

def get_fonts():
    try:
        font_bold = ImageFont.truetype("arialbd.ttf", 34)
        font_large = ImageFont.truetype("arialbd.ttf", 46)
        font_mid = ImageFont.truetype("arialbd.ttf", 26)
        font_small = ImageFont.truetype("arial.ttf", 22)
        font_bold = ImageFont.truetype("arialbd.ttf", 32)
        font_large = ImageFont.truetype("arialbd.ttf", 44)
        font_mid = ImageFont.truetype("arialbd.ttf", 24)
        font_small = ImageFont.truetype("arial.ttf", 20)
    except:
        font_bold = ImageFont.load_default()
        font_large = font_bold
        font_mid = font_bold
        font_small = font_bold
    return font_bold, font_large, font_mid, font_small

def create_base_stage():
    img = Image.new("RGBA", (STAGE_W, STAGE_H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([0, 0, STAGE_W, STAGE_H], radius=36, fill=STAGE_BG, outline=CONTAINER_BORDER, width=4)
    return img, draw

def render_stage_1():
    img, draw = create_base_stage()
    f_bold, f_large, f_mid, f_small = get_fonts()
    
    draw.text((60, 50), "META ADS PERFORMANCE AUDIT", fill=MUTED_TEXT, font=f_small)
    draw.text((60, 85), "FATIGUE DEATH SPIRAL", fill=RED, font=f_large)
    draw.text((60, 45), "META ADS PERFORMANCE AUDIT", fill=MUTED_TEXT, font=f_small)
    draw.text((60, 75), "FATIGUE DEATH SPIRAL", fill=RED, font=f_large)
    
    # Live ROAS Metric Box
    draw.rounded_rectangle([60, 180, 440, 360], radius=20, fill=(20, 50, 65, 255), outline=RED, width=3)
    draw.text((85, 205), "ROAS (DAY 1 -> DAY 6)", fill=MUTED_TEXT, font=f_small)
    draw.text((85, 245), "4.2x -> 0.8x", fill=RED, font=f_large)
    draw.text((85, 315), "[-] 81% CRASH (FATIGUED)", fill=RED, font=f_small)
    # Metrics
    draw.rounded_rectangle([60, 150, 440, 310], radius=18, fill=(20, 50, 65, 255), outline=RED, width=3)
    draw.text((80, 170), "ROAS (DAY 1 -> DAY 6)", fill=MUTED_TEXT, font=f_small)
    draw.text((80, 205), "4.2x -> 0.8x", fill=RED, font=f_large)
    draw.text((80, 265), "[-] 81% CRASH (FATIGUED)", fill=RED, font=f_small)
    
    # Ad CPA Metric Box
    draw.rounded_rectangle([480, 180, 880, 360], radius=20, fill=(20, 50, 65, 255), outline=RED, width=3)
    draw.text((505, 205), "CUSTOMER ACQUISITION COST", fill=MUTED_TEXT, font=f_small)
    draw.text((505, 245), "$38 -> $142.50", fill=RED, font=f_large)
    draw.text((505, 315), "[+] 275% SPIKE", fill=RED, font=f_small)
    draw.rounded_rectangle([480, 150, 880, 310], radius=18, fill=(20, 50, 65, 255), outline=RED, width=3)
    draw.text((500, 170), "CUSTOMER ACQUISITION COST", fill=MUTED_TEXT, font=f_small)
    draw.text((500, 205), "$38 -> $142.50", fill=RED, font=f_large)
    draw.text((500, 265), "[+] 275% SPIKE", fill=RED, font=f_small)
    
    # Chart Area (Graph line dropping)
    draw.rounded_rectangle([60, 390, 880, 670], radius=20, fill=(18, 44, 58, 255))
    for y in [450, 520, 590]:
    # Chart Area
    draw.rounded_rectangle([60, 340, 880, 600], radius=18, fill=(18, 44, 58, 255))
    for y in [400, 470, 540]:
        draw.line([(80, y), (860, y)], fill=(30, 70, 90, 255), width=2)
    
    points = [(100, 440), (220, 450), (360, 490), (500, 580), (680, 640), (840, 650)]
    points = [(100, 380), (220, 390), (360, 430), (500, 510), (680, 570), (840, 580)]
    for i in range(len(points)-1):
        draw.line([points[i], points[i+1]], fill=RED, width=6)
        draw.ellipse([points[i][0]-8, points[i][1]-8, points[i][0]+8, points[i][1]+8], fill=RED)
    draw.ellipse([points[-1][0]-10, points[-1][1]-10, points[-1][0]+10, points[-1][1]+10], fill=RED)
        draw.ellipse([points[i][0]-7, points[i][1]-7, points[i][0]+7, points[i][1]+7], fill=RED)
    draw.ellipse([points[-1][0]-9, points[-1][1]-9, points[-1][0]+9, points[-1][1]+9], fill=RED)
    
    # Frustrated Client Slack Alert
    draw.rounded_rectangle([80, 705, 860, 845], radius=20, fill=(255, 255, 255, 245))
    draw.text((110, 725), "Client CEO in #general:", fill=INK_DARK, font=f_small)
    draw.text((110, 760), "\"ROAS is dying again... why haven't we launched new ads?\"", fill=RED, font=f_mid)
    draw.text((110, 805), "Received: Today at 8:42 AM", fill=(130, 130, 130, 255), font=f_small)
    # Slack Alert (Leaves right side for Node)
    draw.rounded_rectangle([60, 630, 700, 840], radius=18, fill=(255, 255, 255, 245))
    draw.text((85, 650), "Client CEO in #general:", fill=INK_DARK, font=f_small)
    draw.text((85, 685), "\"ROAS is dying again... why haven't\nwe launched new creatives yet?\"", fill=RED, font=f_mid)
    draw.text((85, 785), "Received: Today at 8:42 AM", fill=(130, 130, 130, 255), font=f_small)
    
    img.save(os.path.join(STAGE_DIR, "stage1_roas_crash.png"))

def render_stage_2():
    img, draw = create_base_stage()
    f_bold, f_large, f_mid, f_small = get_fonts()
    
    draw.text((60, 50), "CREATIVE PRODUCTION BOTTLENECK", fill=MUTED_TEXT, font=f_small)
    draw.text((60, 85), "THE 4-DAY CREATIVE SLOWDOWN", fill=CORAL, font=f_large)
    draw.text((60, 45), "CREATIVE PRODUCTION BOTTLENECK", fill=MUTED_TEXT, font=f_small)
    draw.text((60, 75), "THE 4-DAY CREATIVE SLOWDOWN", fill=CORAL, font=f_large)
    
    # Left Card
    draw.rounded_rectangle([60, 180, 440, 520], radius=20, fill=(20, 50, 65, 255), outline=CORAL, width=3)
    draw.text((85, 205), "CREATIVE STRATEGIST", fill=MUTED_TEXT, font=f_small)
    draw.text((85, 245), "4 Days / 3 Briefs", fill=CORAL, font=f_bold)
    draw.text((85, 310), "- Competitor audits\n- Brainstorming hooks\n- Writing Figma docs\n- Re-writing copy", fill=WHITE, font=f_mid)
    draw.text((85, 460), "STATUS: OVERWHELMED", fill=RED, font=f_small)
    draw.rounded_rectangle([60, 150, 430, 460], radius=18, fill=(20, 50, 65, 255), outline=CORAL, width=3)
    draw.text((80, 170), "CREATIVE STRATEGIST", fill=MUTED_TEXT, font=f_small)
    draw.text((80, 205), "4 Days / 3 Briefs", fill=CORAL, font=f_bold)
    draw.text((80, 260), "- Competitor audits\n- Brainstorming hooks\n- Writing Figma docs\n- Re-writing copy", fill=WHITE, font=f_mid)
    draw.text((80, 410), "STATUS: OVERWHELMED", fill=RED, font=f_small)
    
    # Right Card
    draw.rounded_rectangle([480, 180, 880, 520], radius=20, fill=(20, 50, 65, 255), outline=CORAL, width=3)
    draw.text((505, 205), "VIDEO EDITING QUEUE", fill=MUTED_TEXT, font=f_small)
    draw.text((505, 245), "24 Briefs Backlog", fill=RED, font=f_bold)
    draw.text((505, 310), "- Timeline render: 14%\n- Sourcing raw B-roll\n- Cropping 9:16 aspect\n- Caption styling delays", fill=WHITE, font=f_mid)
    draw.text((505, 460), "STATUS: 7-DAY DELAY", fill=RED, font=f_small)
    draw.rounded_rectangle([460, 150, 830, 460], radius=18, fill=(20, 50, 65, 255), outline=CORAL, width=3)
    draw.text((480, 170), "VIDEO EDITING QUEUE", fill=MUTED_TEXT, font=f_small)
    draw.text((480, 205), "24 Briefs Backlog", fill=RED, font=f_bold)
    draw.text((480, 260), "- Timeline render: 14%\n- Sourcing raw B-roll\n- Cropping 9:16 aspect\n- Caption styling delays", fill=WHITE, font=f_mid)
    draw.text((480, 410), "STATUS: 7-DAY DELAY", fill=RED, font=f_small)
    
    # Bottom Alert Card
    draw.rounded_rectangle([60, 560, 880, 830], radius=20, fill=(20, 50, 65, 255))
    draw.text((85, 585), "WHY 7-FIGURE BRANDS WIN PAID MEDIA", fill=MUTED_TEXT, font=f_small)
    draw.text((85, 625), "Standard Agency:  3 new ads / month (Fatigue & High CPA)", fill=(255, 120, 120, 255), font=f_mid)
    draw.text((85, 685), "Winning DTC Brand: 30 new hooks / week (Scalable ROAS)", fill=GREEN, font=f_mid)
    draw.text((85, 760), "* Autonomous Creative Engine solves this in 60 seconds", fill=GOLD, font=f_small)
    # Bottom Alert Card (Left portion)
    draw.rounded_rectangle([60, 490, 700, 840], radius=18, fill=(20, 50, 65, 255))
    draw.text((85, 515), "WHY 7-FIGURE BRANDS WIN PAID MEDIA", fill=MUTED_TEXT, font=f_small)
    draw.text((85, 560), "Standard Agency:  3 new ads / month (Fatigue)", fill=(255, 120, 120, 255), font=f_mid)
    draw.text((85, 620), "Winning DTC Brand: 30 new hooks / week", fill=GREEN, font=f_mid)
    draw.text((85, 680), "Result: Scalable ROAS & Stable CPAs", fill=WHITE, font=f_mid)
    draw.text((85, 760), "* Autonomous Creative Engine solves this in 60s", fill=GOLD, font=f_small)
    
    img.save(os.path.join(STAGE_DIR, "stage2_bottleneck.png"))

def render_stage_3():
    img, draw = create_base_stage()
    f_bold, f_large, f_mid, f_small = get_fonts()
    
    draw.text((60, 50), "AUTONOMOUS HOOK MULTIPLIER", fill=MUTED_TEXT, font=f_small)
    draw.text((60, 85), "30 PSYCHOLOGICAL HOOK ANGLES", fill=COBALT, font=f_large)
    draw.text((60, 45), "AUTONOMOUS HOOK MULTIPLIER", fill=MUTED_TEXT, font=f_small)
    draw.text((60, 75), "30 PSYCHOLOGICAL HOOK ANGLES", fill=COBALT, font=f_large)
    
    cards = [
        ("01. CURIOSITY GAP HOOK", "Scrapes top 50 viral competitor ads & extracts pattern interrupts", COBALT),
        ("02. CONTRARIAN TRUTH HOOK", "Claude writes 30 angles targeting buyer skepticism & pain", GREEN),
        ("03. PROBLEM FLASH HOOK", "Formats 0.3s rapid visual friction script into instant storyboard", CORAL)
        ("01. CURIOSITY GAP HOOK", "Scrapes top 50 viral competitor ads & patterns", COBALT),
        ("02. CONTRARIAN TRUTH HOOK", "Claude writes 30 angles targeting buyer skepticism", GREEN),
        ("03. PROBLEM FLASH HOOK", "Formats 0.3s rapid friction storyboard", CORAL)
    ]
    
    y_start = 180
    y_start = 160
    # Keep width to 700 so Node at 720+ has 100% clear space!
    for title, desc, color in cards:
        draw.rounded_rectangle([60, y_start, 880, y_start + 180], radius=20, fill=(20, 50, 65, 255), outline=color, width=3)
        draw.text((95, y_start + 25), title, fill=color, font=f_large)
        draw.text((95, y_start + 90), desc, fill=WHITE, font=f_mid)
        draw.text((95, y_start + 135), "* Generated in 1.8 seconds | Ready to assemble", fill=MUTED_TEXT, font=f_small)
        y_start += 215
        draw.rounded_rectangle([60, y_start, 700, y_start + 190], radius=18, fill=(20, 50, 65, 255), outline=color, width=3)
        draw.text((85, y_start + 20), title, fill=color, font=f_large)
        draw.text((85, y_start + 75), desc, fill=WHITE, font=f_mid)
        draw.text((85, y_start + 130), "* Generated in 1.8 seconds | Ready to assemble", fill=MUTED_TEXT, font=f_small)
        y_start += 225
        
    img.save(os.path.join(STAGE_DIR, "stage3_hook_multiplier.png"))

def render_stage_4():
    img, draw = create_base_stage()
    f_bold, f_large, f_mid, f_small = get_fonts()
    
    draw.text((60, 50), "1-CLICK BATCH VIDEO ASSEMBLY", fill=MUTED_TEXT, font=f_small)
    draw.text((60, 85), "ROAS REBOUNDS TO 4.8X", fill=GREEN, font=f_large)
    draw.text((60, 45), "1-CLICK BATCH VIDEO ASSEMBLY", fill=MUTED_TEXT, font=f_small)
    draw.text((60, 75), "ROAS REBOUNDS TO 4.8X", fill=GREEN, font=f_large)
    
    grid_x, grid_y = 60, 180
    col_w, row_h = 250, 280
    grid_x, grid_y = 60, 160
    col_w, row_h = 240, 270
    for row in range(2):
        for col in range(3):
            x = grid_x + col * (col_w + 35)
            y = grid_y + row * (row_h + 25)
            x = grid_x + col * (col_w + 30)
            y = grid_y + row * (row_h + 20)
            draw.rounded_rectangle([x, y, x + col_w, y + row_h], radius=16, fill=(24, 60, 78, 255), outline=GREEN, width=2)
            draw.text((x + 20, y + 20), f"HOOK #{row*3 + col + 1}", fill=GOLD, font=f_small)
            draw.rounded_rectangle([x + 20, y + 60, x + col_w - 20, y + 200], radius=10, fill=(15, 40, 52, 255))
            draw.text((x + 35, y + 115), "[>] 9:16 LIVE", fill=WHITE, font=f_small)
            draw.text((x + 20, y + 225), "STATUS: [OK] SCALING", fill=GREEN, font=f_small)
            draw.text((x + 18, y + 18), f"HOOK #{row*3 + col + 1}", fill=GOLD, font=f_small)
            draw.rounded_rectangle([x + 18, y + 55, x + col_w - 18, y + 190], radius=10, fill=(15, 40, 52, 255))
            draw.text((x + 30, y + 110), "[>] 9:16 LIVE", fill=WHITE, font=f_small)
            draw.text((x + 18, y + 215), "STATUS: [OK] SCALING", fill=GREEN, font=f_small)
            
    draw.rounded_rectangle([60, 760, 880, 850], radius=20, fill=GREEN)
    draw.text((90, 780), "+$38,000 CLIENT REVENUE PROTECTED | ROAS: 4.8X", fill=(10, 40, 20, 255), font=f_bold)
    draw.rounded_rectangle([60, 750, 700, 840], radius=18, fill=GREEN)
    draw.text((85, 775), "+$38,000 CLIENT REVENUE PROTECTED | ROAS: 4.8X", fill=(10, 40, 20, 255), font=f_bold)
    
    img.save(os.path.join(STAGE_DIR, "stage4_roas_rebound.png"))

def render_stage_5():
    img, draw = create_base_stage()
    f_bold, f_large, f_mid, f_small = get_fonts()
    
    draw.text((60, 50), "COMPLETE AGENCY AUTOMATION OS", fill=MUTED_TEXT, font=f_small)
    draw.text((60, 85), "THE 30-HOOK CREATIVE ENGINE", fill=GOLD, font=f_large)
    draw.text((60, 45), "COMPLETE AGENCY AUTOMATION OS", fill=MUTED_TEXT, font=f_small)
    draw.text((60, 75), "THE 30-HOOK CREATIVE ENGINE", fill=GOLD, font=f_large)
    
    draw.rounded_rectangle([60, 180, 880, 600], radius=24, fill=(20, 50, 65, 255), outline=GOLD, width=3)
    draw.text((95, 215), "INCLUDED IN THE MASTER BLUEPRINT:", fill=MUTED_TEXT, font=f_small)
    draw.text((95, 265), "1. Competitor Ad Library Scraper (n8n Webhook)", fill=WHITE, font=f_bold)
    draw.text((95, 335), "2. Claude 30-Hook Angle Generator & Prompts", fill=WHITE, font=f_bold)
    draw.text((95, 405), "3. CapCut & Premiere Batch Template Pipelines", fill=WHITE, font=f_bold)
    draw.text((95, 475), "4. Autonomous Ad Fatigue & ROAS Monitor", fill=WHITE, font=f_bold)
    draw.text((95, 545), "* 100% Plug-and-Play for Performance Agencies", fill=GREEN, font=f_mid)
    # Blueprint box (x=60..700 to leave right side for celebrating Node)
    draw.rounded_rectangle([60, 150, 700, 580], radius=20, fill=(20, 50, 65, 255), outline=GOLD, width=3)
    draw.text((85, 175), "INCLUDED IN THE MASTER BLUEPRINT:", fill=MUTED_TEXT, font=f_small)
    draw.text((85, 220), "1. Competitor Ad Library Scraper", fill=WHITE, font=f_bold)
    draw.text((85, 280), "2. Claude 30-Hook Angle Generator", fill=WHITE, font=f_bold)
    draw.text((85, 340), "3. CapCut & Premiere Batch Pipelines", fill=WHITE, font=f_bold)
    draw.text((85, 400), "4. Autonomous Ad Fatigue Monitor", fill=WHITE, font=f_bold)
    draw.text((85, 490), "* 100% Plug-and-Play for Agencies", fill=GREEN, font=f_mid)
    
    draw.rounded_rectangle([60, 640, 880, 840], radius=28, fill=WHITE)
    draw.text((110, 675), "COMMENT \"CREATIVE\"", fill=INK_DARK, font=f_large)
    draw.text((110, 745), "I'LL DM YOU THE FULL AUTOMATION BLUEPRINT & TEMPLATES", fill=CORAL, font=f_mid)
    # CTA button
    draw.rounded_rectangle([60, 620, 700, 840], radius=24, fill=WHITE)
    draw.text((90, 655), "COMMENT \"CREATIVE\"", fill=INK_DARK, font=f_large)
    draw.text((90, 735), "I'LL DM YOU THE FULL AUTOMATION BLUEPRINT", fill=CORAL, font=f_mid)
    draw.text((90, 785), "& PRODUCTION-READY SCRIPT TEMPLATES", fill=INK_DARK, font=f_small)
    
    img.save(os.path.join(STAGE_DIR, "stage5_cta_studio.png"))

if __name__ == "__main__":
    print("Re-rendering stage assets with clean ASCII and proper bounds...")
    print("Re-rendering all 5 stage assets with guaranteed non-overlapping layout...")
    render_stage_1()
    render_stage_2()
    render_stage_3()
    render_stage_4()
    render_stage_5()
    print("Stage assets re-generated successfully!")
    print("Stage assets updated cleanly!")
