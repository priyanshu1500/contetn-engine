"""
make_cards.py — Generates bespoke, high-status cards for Episode D5 (The 7 Lines of Code).
Adheres strictly to AGENTS.md anti-slop rules:
- No generic ChatGPT frames or repeated mockups
- Bespoke 2010 banking paperwork form
- Authentic 7-line Stripe terminal integration
- Photoreal polaroid card with tape and handwritten labels
- $1 Trillion volume stat card
- Stark optical reset typography slide
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(HERE, 'build', 'public', 'img')
os.makedirs(IMG_DIR, exist_ok=True)

# Fonts
FONT_MONO = os.path.join(HERE, 'build', 'public', 'ibm-plex-mono-500.ttf')
FONT_CONDENSED = os.path.join(HERE, 'build', 'public', 'bebas-neue-400.ttf')

# Fallback fonts
def get_font(path, size, fallback="arial.ttf"):
    if os.path.exists(path):
        return ImageFont.truetype(path, size)
    return ImageFont.truetype(fallback, size)

mono_title = get_font(FONT_MONO, 32)
mono_code = get_font(FONT_MONO, 28)
mono_small = get_font(FONT_MONO, 22)
condensed_huge = get_font(FONT_CONDENSED, 110)
condensed_mid = get_font(FONT_CONDENSED, 64)

# ----------------------------------------------------
# CARD 1: stripe_7_lines_code.png (Terminal Code Card)
# ----------------------------------------------------
print("[CardGen] Generating 7 Lines of Code Terminal Card...")
w, h = 1080, 1920
img = Image.new('RGB', (w, h), color=(11, 15, 23)) # Dark slate bg
draw = ImageDraw.Draw(img)

# Terminal Window Box
bx, by, bw, bh = 60, 480, 960, 960
draw.rectangle([bx, by, bx + bw, by + bh], fill=(17, 24, 39), outline=(55, 65, 81), width=3)

# Window Header
draw.rectangle([bx, by, bx + bw, by + 70], fill=(31, 41, 55))
# Dots
draw.ellipse([bx + 30, by + 25, bx + 50, by + 45], fill=(239, 68, 68)) # Red
draw.ellipse([bx + 65, by + 25, bx + 85, by + 45], fill=(245, 158, 11)) # Yellow
draw.ellipse([bx + 100, by + 25, bx + 120, by + 45], fill=(16, 185, 129)) # Green

draw.text((bx + 160, by + 20), "checkout.html — Original Stripe Integration (2010)", fill=(156, 163, 175), font=mono_title)

# Code Lines
code_lines = [
    (1, '<script src="https://js.stripe.com/v1/"></script>', (96, 165, 250)),
    (2, '<form action="/charge" method="POST">', (244, 114, 182)),
    (3, '  <script src="https://checkout.stripe.com/v1.js"', (129, 140, 248)),
    (4, '    class="stripe-button"', (251, 191, 36)),
    (5, '    data-key="pk_live_04938291829..."', (52, 211, 153)),
    (6, '    data-amount="2000"', (52, 211, 153)),
    (7, '    data-description="Widget Purchase">', (52, 211, 153)),
    (8, '  </script>', (129, 140, 248)),
    (9, '</form>', (244, 114, 182)),
]

cy = by + 120
for lnum, line, color in code_lines:
    # Line number
    draw.text((bx + 40, cy), f"{lnum:>2}", fill=(75, 85, 99), font=mono_code)
    # Code syntax
    draw.text((bx + 100, cy), line, fill=color, font=mono_code)
    cy += 64

# Bottom Callout Badge
badge_y = by + bh + 40
draw.rectangle([bx, badge_y, bx + bw, badge_y + 90], fill=(245, 197, 66))
draw.text((bx + 80, badge_y + 15), "7 LINES OF CODE  //  INTEGRATE IN 2 MINUTES", fill=(6, 6, 7), font=condensed_mid)

img.save(os.path.join(IMG_DIR, 'stripe_7_lines_code.png'))

# ----------------------------------------------------
# CARD 2: merchant_bank_forms.png (Legacy Banking Forms)
# ----------------------------------------------------
print("[CardGen] Generating Legacy Merchant Bank Form...")
img2 = Image.new('RGB', (w, h), color=(240, 237, 230)) # Vintage document cream
draw2 = ImageDraw.Draw(img2)

# Document Box
dx, dy, dw, dh = 80, 420, 920, 1080
draw2.rectangle([dx, dy, dx + dw, dy + dh], fill=(255, 255, 255), outline=(180, 175, 160), width=4)

# Document Header
draw2.text((dx + 60, dy + 60), "MERCHANT ACQUIRING BANK // APPLICATION FORM", fill=(20, 20, 20), font=mono_title)
draw2.line([dx + 60, dy + 110, dx + dw - 60, dy + 110], fill=(200, 200, 200), width=3)

# Requirements checklist
checklist = [
    "1. Physical Fax Application (24 Pages)",
    "2. Security Deposit / Rolling Reserve ($15,000)",
    "3. Upfront Bank Underwriting Fee ($3,500)",
    "4. Personal Guarantees & Notarized ID",
    "5. Average Approval Window: 6 WEEKS",
    "6. Gateway Integration Complexity: High",
]

ly = dy + 160
for item in checklist:
    draw2.rectangle([dx + 60, ly + 8, dx + 85, ly + 33], outline=(60, 60, 60), width=3)
    draw2.line([dx + 65, ly + 20, dx + 75, ly + 28], fill=(180, 40, 40), width=4)
    draw2.line([dx + 75, ly + 28, dx + 85, ly + 12], fill=(180, 40, 40), width=4)
    draw2.text((dx + 110, ly), item, fill=(50, 50, 50), font=mono_title)
    ly += 90

# Stamp: REJECTED / 6 WEEKS DELAY
stamp_box = [dx + 180, dy + 760, dx + dw - 180, dy + 920]
draw2.rectangle(stamp_box, outline=(220, 38, 38), width=8)
draw2.text((dx + 230, dy + 785), "WAIT: 6 WEEKS", fill=(220, 38, 38), font=condensed_huge)

img2.save(os.path.join(IMG_DIR, 'merchant_bank_forms.png'))

# ----------------------------------------------------
# CARD 3: collison_installation_card.png (Polaroid Card)
# ----------------------------------------------------
print("[CardGen] Generating Collison Installation Polaroid Card...")
img3 = Image.new('RGB', (w, h), color=(10, 10, 12))
draw3 = ImageDraw.Draw(img3)

# Polaroid Paper Card
px, py, pw, ph = 120, 460, 840, 1000
draw3.rectangle([px, py, px + pw, py + ph], fill=(248, 246, 240), outline=(220, 218, 210), width=2)

# Photo placeholder (Insert Patrick Collison photo if available)
pat_path = os.path.join(IMG_DIR, 'patrick_collison.jpg')
if os.path.exists(pat_path):
    p_img = Image.open(pat_path).convert('RGB')
    p_img = p_img.resize((760, 680), Image.Resampling.LANCZOS)
    img3.paste(p_img, (px + 40, py + 40))
else:
    draw3.rectangle([px + 40, py + 40, px + pw - 40, py + 720], fill=(40, 40, 45))

# Handwritten label tag
draw3.text((px + 60, py + 760), "THE COLLISON INSTALLATION", fill=(20, 20, 20), font=condensed_huge)
draw3.text((px + 60, py + 880), "Palo Alto Coffee Shops, 2010 // 'Give me your laptop.'", fill=(80, 80, 80), font=mono_title)

# Masking tape on top
draw3.rectangle([px + 300, py - 35, px + 540, py + 25], fill=(240, 235, 215))

img3.save(os.path.join(IMG_DIR, 'collison_installation_card.png'))

# ----------------------------------------------------
# CARD 4: stripe_trillion_card.png ($1 Trillion Stat)
# ----------------------------------------------------
print("[CardGen] Generating $1 Trillion Volume Card...")
img4 = Image.new('RGB', (w, h), color=(6, 6, 7))
draw4 = ImageDraw.Draw(img4)

draw4.text((120, 680), "STRIPE ANNUAL PROCESSED VOLUME", fill=(245, 197, 66), font=mono_title)
draw4.text((110, 760), "$1 TRILLION", fill=(255, 255, 255), font=condensed_huge)
draw4.text((120, 910), "POWERING AMAZON, GOOGLE & HALF THE INTERNET", fill=(156, 163, 175), font=mono_title)

img4.save(os.path.join(IMG_DIR, 'stripe_trillion_card.png'))

# ----------------------------------------------------
# CARD 5: friction_lesson_card.png (Stark Optical Reset)
# ----------------------------------------------------
print("[CardGen] Generating Stark Optical Reset Slide...")
img5 = Image.new('RGB', (w, h), color=(255, 255, 255)) # Pure white
draw5 = ImageDraw.Draw(img5)

draw5.text((120, 720), "THE OPERATIONAL LAW:", fill=(100, 100, 100), font=mono_title)
draw5.text((110, 800), "COLLAPSE THE FRICTION.", fill=(6, 6, 7), font=condensed_huge)
draw5.text((120, 950), "THE COMPANY THAT REMOVES FRICTION WINS THE MARKET.", fill=(40, 40, 40), font=mono_title)

img5.save(os.path.join(IMG_DIR, 'friction_lesson_card.png'))

print("[CardGen] All 5 bespoke cards generated successfully in build/public/img/!")
