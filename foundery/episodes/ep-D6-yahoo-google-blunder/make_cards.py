"""
make_cards.py — Generates bespoke 2.5D documentary evidence cards and artifacts for Episode D6:
"The $1M Blunder: Yahoo vs. Google".
Strictly zero generic AI slop. Photoreal document textures, vintage stamps, and stark contrast.
"""
import os
from PIL import Image, ImageDraw, ImageFont

PUB_IMG = r'D:\agency content\BIN\documentary_tofu\ep-D6-yahoo-google-blunder\build\public\img'
PUB_FONTS = r'D:\agency content\BIN\documentary_tofu\ep-D6-yahoo-google-blunder\build\public'
os.makedirs(PUB_IMG, exist_ok=True)

def get_fonts():
    f_mono = ImageFont.truetype(os.path.join(PUB_FONTS, 'ibm-plex-mono-600.ttf'), 20)
    f_mono_sm = ImageFont.truetype(os.path.join(PUB_FONTS, 'ibm-plex-mono-400.ttf'), 15)
    f_mono_lg = ImageFont.truetype(os.path.join(PUB_FONTS, 'ibm-plex-mono-600.ttf'), 28)
    f_bebas = ImageFont.truetype(os.path.join(PUB_FONTS, 'bebas-neue-400.ttf'), 54)
    f_bebas_xl = ImageFont.truetype(os.path.join(PUB_FONTS, 'bebas-neue-400.ttf'), 86)
    f_bebas_giant = ImageFont.truetype(os.path.join(PUB_FONTS, 'bebas-neue-400.ttf'), 140)
    return f_mono, f_mono_sm, f_mono_lg, f_bebas, f_bebas_xl, f_bebas_giant

f_mono, f_mono_sm, f_mono_lg, f_bebas, f_bebas_xl, f_bebas_giant = get_fonts()

# -------------------------------------------------------------
# 1. THE ASYMMETRIC REJECTION CARD (1998 vs 2002)
# -------------------------------------------------------------
def make_rejection_card():
    img = Image.new('RGB', (1920, 1080), (11, 11, 12))
    draw = ImageDraw.Draw(img)
    
    # Outer frame
    card_box = [300, 140, 1620, 940]
    draw.rounded_rectangle(card_box, radius=24, fill=(18, 19, 23), outline=(40, 44, 52), width=3)
    
    # Header
    draw.text((360, 180), "YAHOO! BOARDROOM MINUTES // ACQUISITION ARCHIVE", fill=(245, 197, 66), font=f_mono)
    draw.text((360, 215), "TARGET: PAGERANK ALGORITHM / GOOGLE TECHNOLOGY INC.", fill=(160, 165, 175), font=f_mono_sm)
    draw.line([(360, 245), (1560, 245)], fill=(50, 55, 65), width=2)
    
    # Left Column: 1998
    col1_box = [360, 280, 930, 880]
    draw.rounded_rectangle(col1_box, radius=16, fill=(24, 26, 32), outline=(60, 65, 78), width=2)
    draw.text((400, 320), "OFFER 1 // 1998", fill=(140, 145, 160), font=f_mono)
    draw.text((400, 360), "$1,000,000", fill=(247, 245, 239), font=f_bebas_xl)
    draw.text((400, 470), "ASSET: PAGERANK PATENT", fill=(245, 197, 66), font=f_mono_sm)
    draw.text((400, 505), "SELLER: LARRY PAGE & SERGEY BRIN", fill=(180, 185, 195), font=f_mono_sm)
    draw.text((400, 540), "STATUS: REJECTED", fill=(200, 58, 42), font=f_mono)
    
    # Stamp 1998
    draw.rectangle([400, 620, 890, 720], fill=(180, 40, 30, 220), outline=(240, 70, 60), width=3)
    draw.text((450, 638), "REJECTED BY YAHOO", fill=(255, 255, 255), font=f_bebas)
    draw.text((400, 750), '"Too fast. Users will leave our portal in 3 seconds."', fill=(160, 165, 175), font=f_mono_sm)

    # Right Column: 2002
    col2_box = [990, 280, 1560, 880]
    draw.rounded_rectangle(col2_box, radius=16, fill=(24, 26, 32), outline=(60, 65, 78), width=2)
    draw.text((1030, 320), "OFFER 2 // 2002", fill=(140, 145, 160), font=f_mono)
    draw.text((1030, 360), "$3,000,000,000", fill=(247, 245, 239), font=f_bebas_xl)
    draw.text((1030, 470), "ASSET: ENTIRE COMPANY", fill=(245, 197, 66), font=f_mono_sm)
    draw.text((1030, 505), "BIDDER: TERRY SEMEL (CEO, YAHOO)", fill=(180, 185, 195), font=f_mono_sm)
    draw.text((1030, 540), "STATUS: WALKED AWAY OVER $2B GAP", fill=(200, 58, 42), font=f_mono)
    
    # Stamp 2002
    draw.rectangle([1030, 620, 1520, 720], fill=(180, 40, 30, 220), outline=(240, 70, 60), width=3)
    draw.text((1070, 638), "DEAL COLLAPSED", fill=(255, 255, 255), font=f_bebas)
    draw.text((1030, 750), '"Google wanted $5B. Yahoo refused to pay."', fill=(160, 165, 175), font=f_mono_sm)

    out = os.path.join(PUB_IMG, 'yahoo_google_rejection_card.png')
    img.save(out)
    print("Saved:", out)

# -------------------------------------------------------------
# 2. VINTAGE 1998 YAHOO PORTAL CLUTTER CARD
# -------------------------------------------------------------
def make_portal_trap_card():
    img = Image.new('RGB', (1920, 1080), (11, 11, 12))
    draw = ImageDraw.Draw(img)
    
    box = [320, 160, 1600, 920]
    draw.rounded_rectangle(box, radius=20, fill=(235, 235, 240), outline=(200, 58, 42), width=4)
    
    # Yahoo header banner (Vintage purple)
    draw.rectangle([320, 160, 1600, 260], fill=(85, 26, 139))
    draw.text((360, 180), "YAHOO! ENTERPRISE PORTAL (1998)", fill=(255, 255, 255), font=f_bebas)
    draw.text((360, 228), "GOAL: MAXIMUM USER DWELL TIME & BANNER AD CLICKS", fill=(245, 197, 66), font=f_mono_sm)
    
    # Cluttered simulated portal grid
    items = [
        ("TODAY'S HOROSCOPES", "Click for Leo, Scorpio & Taurus predictions"),
        ("HOLLYWOOD GOSSIP", "Celebrity breakups and box office figures"),
        ("CHAT ROOMS (32,400 ONLINE)", "Join Room #12: Singles 90s"),
        ("BANNER AD CLICKS", "Earn $0.05 per impression. Keep users clicking!"),
        ("YELLOW PAGES DIRECTORY", "Search 40,000 local businesses manually"),
        ("SPORTS SCORES & ODDS", "NFL, MLB, NBA live ticker updates")
    ]
    
    for idx, (title, sub) in enumerate(items):
        row = idx // 2
        col = idx % 2
        x1 = 360 + col * 610
        y1 = 290 + row * 160
        draw.rectangle([x1, y1, x1 + 580, y1 + 130], fill=(255, 255, 255), outline=(180, 185, 195), width=2)
        draw.text((x1 + 20, y1 + 20), title, fill=(30, 30, 35), font=f_mono)
        draw.text((x1 + 20, y1 + 60), sub, fill=(100, 105, 115), font=f_mono_sm)
        draw.rectangle([x1 + 440, y1 + 15, x1 + 560, y1 + 50], fill=(245, 197, 66), outline=(200, 160, 40))
        draw.text((x1 + 455, y1 + 22), "STAY ON SITE", fill=(10, 10, 10), font=f_mono_sm)

    # Red Stamp Across the entire portal
    draw.rectangle([450, 770, 1470, 870], fill=(200, 40, 30, 240), outline=(255, 80, 70), width=4)
    draw.text((500, 788), 'THE FLAW: USER TRAP ARCHITECTURE', fill=(255, 255, 255), font=f_bebas)

    out = os.path.join(PUB_IMG, 'yahoo_portal_trap_card.png')
    img.save(out)
    print("Saved:", out)

# -------------------------------------------------------------
# 3. GOOGLE 3-SECOND ANSWER SPEED CARD
# -------------------------------------------------------------
def make_speed_card():
    img = Image.new('RGB', (1920, 1080), (11, 11, 12))
    draw = ImageDraw.Draw(img)
    
    box = [340, 180, 1580, 900]
    draw.rounded_rectangle(box, radius=24, fill=(18, 20, 24), outline=(78, 113, 255), width=3)
    
    draw.text((400, 230), "GOOGLE 1998 // THE CORE ARCHITECTURAL INVERSION", fill=(78, 113, 255), font=f_mono)
    draw.text((400, 270), "METRIC: TIME TO EXIT (COLLAPSE LATENCY TO ZERO)", fill=(160, 165, 175), font=f_mono_sm)
    draw.line([(400, 300), (1520, 300)], fill=(45, 50, 60), width=2)
    
    # Large speed display
    draw.text((400, 360), "3 SECONDS", fill=(245, 197, 66), font=f_bebas_giant)
    draw.text((400, 530), "Average time from query input to external destination click.", fill=(210, 215, 225), font=f_mono)
    draw.text((400, 580), "Result: Zero ads, pure white screen, instantaneous search resolution.", fill=(160, 165, 175), font=f_mono)
    
    # Comparison footer
    draw.rectangle([400, 660, 1520, 830], fill=(25, 28, 36), outline=(50, 55, 70))
    draw.text((440, 690), "YAHOO MONETIZATION: Keep user trapped -> Click 12 pages -> Maximize ad views", fill=(200, 60, 50), font=f_mono_sm)
    draw.text((440, 740), "GOOGLE MONETIZATION: Deliver answer instantly -> Respect user attention -> Own the internet", fill=(100, 220, 140), font=f_mono_sm)

    out = os.path.join(PUB_IMG, 'google_speed_card.png')
    img.save(out)
    print("Saved:", out)

# -------------------------------------------------------------
# 4. TRILLION-DOLLAR ASYMMETRY CARD
# -------------------------------------------------------------
def make_trillion_card():
    img = Image.new('RGB', (1920, 1080), (11, 11, 12))
    draw = ImageDraw.Draw(img)
    
    box = [300, 160, 1620, 920]
    draw.rounded_rectangle(box, radius=24, fill=(18, 20, 24), outline=(245, 197, 66), width=3)
    
    draw.text((360, 210), "HISTORICAL OUTCOME // 2026 VALUATION DIVERGENCE", fill=(245, 197, 66), font=f_mono)
    draw.line([(360, 250), (1560, 250)], fill=(45, 50, 60), width=2)
    
    # Google side
    draw.text((360, 290), "GOOGLE (ALPHABET)", fill=(247, 245, 239), font=f_bebas)
    draw.text((360, 350), "$2,100,000,000,000+", fill=(245, 197, 66), font=f_bebas_xl)
    draw.text((360, 460), "Built on instant search speed and algorithmic relevance.", fill=(180, 185, 195), font=f_mono_sm)
    
    draw.line([(360, 520), (1560, 520)], fill=(45, 50, 60), width=1)
    
    # Yahoo side
    draw.text((360, 560), "YAHOO (SOLD TO VERIZON)", fill=(160, 165, 175), font=f_bebas)
    draw.text((360, 620), "$4,480,000,000", fill=(200, 60, 50), font=f_bebas_xl)
    draw.text((360, 730), "Sold for salvage value in 2017 after rejecting Google, eBay, and Facebook.", fill=(160, 165, 175), font=f_mono_sm)

    out = os.path.join(PUB_IMG, 'trillion_divergence_card.png')
    img.save(out)
    print("Saved:", out)

# -------------------------------------------------------------
# 5. THE AGENCY B2B LESSON CARD
# -------------------------------------------------------------
def make_lesson_card():
    img = Image.new('RGB', (1920, 1080), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Stark pure white slide with high-status black typography
    draw.text((200, 240), "THE LESSON FOR BUSINESS OWNERS TODAY:", fill=(100, 100, 100), font=f_mono)
    draw.text((200, 320), "THE MARKET DOES NOT CARE", fill=(10, 10, 10), font=f_bebas_giant)
    draw.text((200, 470), "ABOUT YOUR BILLABLE HOURS.", fill=(200, 40, 30), font=f_bebas_giant)
    
    draw.text((200, 670), "Legacy companies reject autonomous AI swarms to protect human hourly billing.", fill=(40, 40, 40), font=f_mono_lg)
    draw.text((200, 720), "Just like Yahoo protected banner ads over search speed.", fill=(80, 80, 80), font=f_mono)
    draw.text((200, 780), "THE FASTER MACHINE WINS EVERY SINGLE TIME.", fill=(10, 10, 10), font=f_mono_lg)

    out = os.path.join(PUB_IMG, 'faster_machine_lesson.png')
    img.save(out)
    print("Saved:", out)

if __name__ == '__main__':
    make_rejection_card()
    make_portal_trap_card()
    make_speed_card()
    make_trillion_card()
    make_lesson_card()

