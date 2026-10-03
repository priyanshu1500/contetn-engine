"""
make_reddit_cards.py — Generates bespoke 2.5D documentary evidence cards and artifacts for the Reddit origin story.
"""
import os
from PIL import Image, ImageDraw, ImageFont

PUB_IMG = r'D:\agency content\BIN\documentary_tofu\ep-D4-500b-living-room\build\public\img'
PUB_FONTS = r'D:\agency content\BIN\documentary_tofu\ep-D4-500b-living-room\build\public'

os.makedirs(PUB_IMG, exist_ok=True)

def get_fonts():
    f_mono = ImageFont.truetype(os.path.join(PUB_FONTS, 'ibm-plex-mono-600.ttf'), 18)
    f_mono_sm = ImageFont.truetype(os.path.join(PUB_FONTS, 'ibm-plex-mono-400.ttf'), 14)
    f_mono_lg = ImageFont.truetype(os.path.join(PUB_FONTS, 'ibm-plex-mono-600.ttf'), 26)
    f_bebas = ImageFont.truetype(os.path.join(PUB_FONTS, 'bebas-neue-400.ttf'), 48)
    f_bebas_xl = ImageFont.truetype(os.path.join(PUB_FONTS, 'bebas-neue-400.ttf'), 76)
    return f_mono, f_mono_sm, f_mono_lg, f_bebas, f_bebas_xl

f_mono, f_mono_sm, f_mono_lg, f_bebas, f_bebas_xl = get_fonts()

# -------------------------------------------------------------
# 1. FLIP PHONE "MYMOBILEMENU" (THE REJECTED 2005 STARTUP)
# -------------------------------------------------------------
def make_flip_phone():
    img = Image.new('RGB', (1920, 1080), (11, 11, 12))
    draw = ImageDraw.Draw(img)
    
    # Phone frame (Silver Motorola Razr vibe)
    phone_box = [760, 180, 1160, 900]
    draw.rounded_rectangle(phone_box, radius=40, fill=(35, 37, 42), outline=(70, 75, 85), width=4)
    
    # Screen
    screen_box = [800, 240, 1120, 580]
    draw.rounded_rectangle(screen_box, radius=12, fill=(18, 30, 24), outline=(40, 60, 50), width=2)
    
    # Screen UI (2005 LCD green text)
    draw.text((820, 260), "MyMobileMenu v1.0 (2005)", fill=(100, 220, 140), font=f_mono_sm)
    draw.line([(820, 285), (1100, 285)], fill=(60, 140, 90), width=1)
    
    draw.text((820, 305), "ORDER FOOD VIA SMS:", fill=(180, 255, 200), font=f_mono)
    draw.text((820, 340), "1. Boston Pizza Co.", fill=(140, 220, 160), font=f_mono_sm)
    draw.text((820, 370), "2. Cambridge Diner", fill=(140, 220, 160), font=f_mono_sm)
    draw.text((820, 400), "3. Harvard Deli", fill=(140, 220, 160), font=f_mono_sm)
    
    draw.rectangle([820, 440, 1100, 490], fill=(25, 45, 35), outline=(60, 120, 80))
    draw.text((830, 452), "STATUS: PENDING SMS...", fill=(245, 197, 66), font=f_mono_sm)
    draw.text((820, 540), "[OPTIONS]         [EXIT]", fill=(100, 180, 130), font=f_mono_sm)
    
    # Keypad below
    for row in range(3):
        for col in range(3):
            kx = 830 + col * 100
            ky = 610 + row * 80
            draw.rounded_rectangle([kx, ky, kx + 80, ky + 60], radius=10, fill=(24, 26, 30), outline=(50, 55, 65), width=2)
            num = str(row * 3 + col + 1)
            draw.text((kx + 32, ky + 16), num, fill=(180, 185, 195), font=f_mono)
            
    # Red "REJECTED BY Y COMBINATOR" stamp across the phone
    draw.rectangle([680, 480, 1240, 560], fill=(200, 40, 30, 220), outline=(255, 80, 70), width=3)
    draw.text((710, 495), "REJECTED BY Y COMBINATOR", fill=(255, 255, 255), font=f_bebas)
    
    out = os.path.join(PUB_IMG, 'flip_phone_mymobilemenu.png')
    img.save(out)
    print("Saved:", out)

make_flip_phone()

# -------------------------------------------------------------
# 2. JUNE 2005 ORIGINAL REDDIT UI (AUTHENTIC ARCHIVE SNAPSHOT)
# -------------------------------------------------------------
def make_reddit_2005_ui():
    img = Image.new('RGB', (1920, 1080), (14, 15, 18))
    draw = ImageDraw.Draw(img)
    
    # Browser window
    win_box = [300, 120, 1620, 960]
    draw.rounded_rectangle(win_box, radius=16, fill=(255, 255, 255), outline=(80, 85, 95), width=3)
    
    # Browser bar
    draw.rectangle([300, 120, 1620, 180], fill=(235, 238, 242))
    draw.ellipse([320, 142, 336, 158], fill=(235, 95, 85))
    draw.ellipse([346, 142, 362, 158], fill=(245, 185, 60))
    draw.ellipse([372, 142, 388, 158], fill=(95, 195, 85))
    
    # Address bar
    draw.rounded_rectangle([420, 134, 1400, 166], radius=8, fill=(255, 255, 255), outline=(200, 205, 215))
    draw.text((435, 140), "https://reddit.com/ (June 23, 2005) - What's new online", fill=(60, 65, 75), font=f_mono_sm)
    
    # Reddit 2005 Header
    draw.text((340, 205), "reddit.com", fill=(0, 50, 160), font=f_bebas)
    draw.text((540, 222), "what's new online!", fill=(120, 125, 135), font=f_mono)
    draw.line([(340, 265), (1580, 265)], fill=(200, 210, 225), width=2)
    
    # Reddit posts in 2005
    posts = [
        ("1. Downtown Boston Wireless Network Launched", "submitted by spez 2 hours ago | 14 comments", "(boston.com)"),
        ("2. Why Lisp is the Best Language for Web Applications", "submitted by kn0thing 4 hours ago | 28 comments", "(paulgraham.com)"),
        ("3. The Python 2.4 Release Notes & Speed Improvements", "submitted by alexis_o 5 hours ago | 9 comments", "(python.org)"),
        ("4. Cambridge Startup Scene is Heating Up this Summer", "submitted by cambridge_dev 7 hours ago | 31 comments", "(techcrunch.com)"),
        ("5. How to build web applications without servers", "submitted by hacker_01 8 hours ago | 17 comments", "(slashdot.org)"),
    ]
    
    for i, (title, meta, domain) in enumerate(posts):
        y = 290 + i * 110
        # Upvote arrow box
        draw.rounded_rectangle([340, y, 380, y + 55], radius=6, fill=(240, 243, 248), outline=(210, 218, 230))
        draw.polygon([(360, y + 12), (348, y + 28), (372, y + 28)], fill=(255, 69, 0))
        draw.text((352, y + 32), str(42 - i * 7), fill=(60, 65, 75), font=f_mono_sm)
        
        # Post Title
        draw.text((405, y), title, fill=(0, 40, 180), font=f_mono)
        draw.text((405 + len(title) * 11 + 20, y + 2), domain, fill=(140, 145, 155), font=f_mono_sm)
        draw.text((405, y + 28), meta, fill=(100, 105, 115), font=f_mono_sm)
        draw.line([(340, y + 80), (1580, y + 80)], fill=(240, 243, 248), width=1)
        
    # Annotation footer
    draw.rectangle([340, 860, 1580, 930], fill=(255, 245, 220), outline=(245, 197, 66), width=2)
    draw.text((360, 885), "PRIMARY EVIDENCE: ZERO ORGANIC USERS AT LAUNCH (100% SEEDED BY FOUNDERS)", fill=(180, 60, 20), font=f_mono)
    
    out = os.path.join(PUB_IMG, 'reddit_2005_wayback.png')
    img.save(out)
    print("Saved:", out)

make_reddit_2005_ui()

# -------------------------------------------------------------
# 3. GHOST PROFILES ADMIN CARD (THE SECRET HACK)
# -------------------------------------------------------------
def make_ghost_profiles_card():
    img = Image.new('RGB', (1920, 1080), (11, 11, 12))
    draw = ImageDraw.Draw(img)
    
    card_box = [360, 140, 1560, 940]
    draw.rounded_rectangle(card_box, radius=20, fill=(18, 20, 24), outline=(245, 197, 66), width=3)
    
    # Header
    draw.text((410, 180), "REDDIT INTERNAL ADMIN // SUMMER 2005", fill=(245, 197, 66), font=f_mono_lg)
    draw.text((410, 220), "DEPOSITORY OF SYNTHETIC USER PERSONAS (FOUNDER SEED ENGINE)", fill=(160, 165, 175), font=f_mono_sm)
    draw.line([(410, 250), (1510, 250)], fill=(50, 55, 65), width=2)
    
    # 3 Columns of fake accounts
    cols = [
        ("STEVE'S PERSONAS (spez)", ["spez (admin)", "lisp_god_99", "cambridge_guy", "boston_techie", "web_architect"]),
        ("ALEXIS'S PERSONAS (kn0thing)", ["kn0thing (admin)", "uva_wahoo", "reddit_fan_01", "daily_curator", "coffee_coder"]),
        ("AUTOMATED SCRAPER BOTS", ["bot_slashdot", "bot_wired_feed", "bot_del_icio_us", "bot_hackernews_rss", "bot_boston_globe"])
    ]
    
    for c_idx, (col_title, users) in enumerate(cols):
        cx = 410 + c_idx * 380
        draw.text((cx, 280), col_title, fill=(247, 245, 239), font=f_mono)
        draw.line([(cx, 310), (cx + 340, 310)], fill=(78, 113, 255), width=2)
        
        for u_idx, u in enumerate(users):
            uy = 335 + u_idx * 70
            draw.rounded_rectangle([cx, uy, cx + 340, uy + 55], radius=10, fill=(26, 29, 36), outline=(45, 50, 62))
            draw.text((cx + 15, uy + 12), f"> {u}", fill=(245, 197, 66) if 'admin' in u else (210, 215, 225), font=f_mono_sm)
            draw.text((cx + 15, uy + 32), "STATUS: ACTIVE // AUTO-UPVOTE", fill=(100, 180, 120), font=f_mono_sm)
            
    # Bottom callout
    draw.rectangle([410, 780, 1510, 890], fill=(30, 22, 20), outline=(200, 58, 42), width=2)
    draw.text((435, 805), "FOUNDER QUOTE — ALEXIS OHANIAN:", fill=(245, 197, 66), font=f_mono)
    draw.text((435, 840), '"We submitted all the content and had conversations with ourselves so visitors thought it was alive."', fill=(247, 245, 239), font=f_mono_sm)
    
    out = os.path.join(PUB_IMG, 'ghost_profiles_card.png')
    img.save(out)
    print("Saved:", out)

make_ghost_profiles_card()

# -------------------------------------------------------------
# 4. CONDÉ NAST ACQUISITION HEADLINE (OCTOBER 2006)
# -------------------------------------------------------------
def make_conde_nast_headline():
    img = Image.new('RGB', (1920, 1080), (11, 11, 12))
    draw = ImageDraw.Draw(img)
    
    card_box = [340, 160, 1580, 920]
    draw.rounded_rectangle(card_box, radius=20, fill=(248, 246, 240), outline=(200, 200, 200), width=4)
    
    # News Masthead
    draw.text((390, 200), "WIRED NEWS // OCTOBER 31, 2006", fill=(30, 30, 30), font=f_mono)
    draw.line([(390, 235), (1530, 235)], fill=(30, 30, 30), width=3)
    
    # Giant Headline
    draw.text((390, 260), "CONDÉ NAST ACQUIRES REDDIT", fill=(15, 15, 18), font=f_bebas_xl)
    draw.text((390, 345), "Two 23-Year-Old Founders Sell Community Portal in $10 Million Buyout", fill=(60, 60, 65), font=f_mono_lg)
    
    # Article text
    draw.line([(390, 395), (1530, 395)], fill=(180, 180, 180), width=1)
    
    body_lines = [
        "CAMBRIDGE, MA — Just 16 months after launching from a rented Massachusetts apartment,",
        "Steve Huffman and Alexis Ohanian have sold social bookmarking site Reddit to magazine giant",
        "Condé Nast Publications for an estimated $10 to $20 million cash transaction.",
        "",
        "The site, which started with zero visitors in the summer of 2005, now processes over",
        "1 million pageviews daily and has become the primary social discussion layer of the web.",
        "Both founders were 22 years old when Y Combinator funded the company."
    ]
    for idx, l in enumerate(body_lines):
        draw.text((390, 425 + idx * 36), l, fill=(40, 40, 45), font=f_mono_sm)
        
    # Big stat callout badge
    draw.rectangle([390, 720, 1530, 860], fill=(20, 20, 24))
    draw.text((430, 745), "VALUATION METRIC // 16 MONTHS FROM LAUNCH", fill=(245, 197, 66), font=f_mono)
    draw.text((430, 785), "$10,000,000 CASH EXIT  ·  FOUNDERS AGED 23", fill=(255, 255, 255), font=f_bebas)
    
    out = os.path.join(PUB_IMG, 'conde_nast_headline.png')
    img.save(out)
    print("Saved:", out)

make_conde_nast_headline()

# -------------------------------------------------------------
# 5. 2024 REDDIT IPO & AI LICENSING DEAL CARD
# -------------------------------------------------------------
def make_reddit_ipo_deal_card():
    img = Image.new('RGB', (1920, 1080), (11, 11, 12))
    draw = ImageDraw.Draw(img)
    
    card_box = [340, 140, 1580, 940]
    draw.rounded_rectangle(card_box, radius=20, fill=(18, 20, 26), outline=(78, 113, 255), width=3)
    
    # Header
    draw.text((390, 180), "NEW YORK STOCK EXCHANGE // TICKER: RDDT (2024 - 2026)", fill=(78, 113, 255), font=f_mono_lg)
    draw.text((390, 220), "THE $15B+ DATA LAYER FOR ARTIFICIAL INTELLIGENCE", fill=(180, 185, 195), font=f_mono_sm)
    draw.line([(390, 250), (1530, 250)], fill=(50, 55, 70), width=2)
    
    # Stat boxes
    draw.rounded_rectangle([390, 290, 930, 520], radius=16, fill=(24, 28, 38), outline=(60, 70, 95))
    draw.text((420, 315), "MARKET CAPITALIZATION", fill=(245, 197, 66), font=f_mono)
    draw.text((420, 360), "$15.4 BILLION", fill=(255, 255, 255), font=f_bebas_xl)
    draw.text((420, 460), "NYSE PUBLIC TRADING VALUATION", fill=(140, 145, 160), font=f_mono_sm)
    
    draw.rounded_rectangle([980, 290, 1530, 520], radius=16, fill=(24, 28, 38), outline=(60, 70, 95))
    draw.text((1010, 315), "AI LICENSING CONTRACTS", fill=(78, 113, 255), font=f_mono)
    draw.text((1010, 360), "$60,000,000/YR", fill=(255, 255, 255), font=f_bebas_xl)
    draw.text((1010, 460), "GOOGLE & OPENAI MODEL TRAINING DATA", fill=(140, 145, 160), font=f_mono_sm)
    
    # Bottom Takeaway Box
    draw.rectangle([390, 570, 1530, 880], fill=(26, 22, 18), outline=(245, 197, 66), width=2)
    draw.text((425, 605), "THE ARCHIVAL INVERSION:", fill=(245, 197, 66), font=f_mono)
    draw.text((425, 650), "WHAT STARTED AS FAKE ACCOUNTS SEEDED IN A LIVING ROOM", fill=(255, 255, 255), font=f_bebas)
    draw.text((425, 715), "IS NOW THE FOUNDATIONAL CORPUS TRAINING HUMANITY'S AI MODELS.", fill=(245, 197, 66), font=f_mono_lg)
    draw.text((425, 780), "From 0 users in 2005 -> 1.2 Billion Monthly Active Discussions.", fill=(180, 185, 195), font=f_mono_sm)
    
    out = os.path.join(PUB_IMG, 'reddit_ipo_deal_card.png')
    img.save(out)
    print("Saved:", out)

make_reddit_ipo_deal_card()

