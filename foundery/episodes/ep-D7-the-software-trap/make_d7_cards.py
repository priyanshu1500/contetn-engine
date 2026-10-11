"""
make_d7_cards.py — Bespoke Documentary Evidence Cards for Episode D7: "The Software Trap".
Strictly zero generic AI slop. Photoreal financial ledger, tech specs, and stark contrast.
"""
import os
from PIL import Image, ImageDraw, ImageFont

PUB_IMG = r'D:\agency content\BIN\documentary_tofu\ep-D7-the-software-trap\build\public\img'
PUB_FONTS = r'D:\agency content\BIN\documentary_tofu\ep-D7-the-software-trap\build\public'
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

# 1. THE COALITION CARD (Big Tech Silicon Rebellion)
def make_coalition_card():
    img = Image.new('RGB', (1920, 1080), (10, 10, 12))
    draw = ImageDraw.Draw(img)
    
    # Outer container
    draw.rounded_rectangle([240, 120, 1680, 960], radius=24, fill=(16, 17, 21), outline=(45, 48, 58), width=3)
    
    # Header
    draw.text((300, 160), "CONFIDENTIAL // SILICON VALLEY INFRASTRUCTURE AUDIT", fill=(245, 197, 66), font=f_mono)
    draw.text((300, 195), "PROJECT: BIG TECH IN-HOUSE ACCELERATOR REVOLT", fill=(160, 165, 175), font=f_mono_sm)
    draw.line([(300, 230), (1620, 230)], fill=(50, 55, 65), width=2)
    
    # 4 Columns for the 4 Giants
    columns = [
        ("GOOGLE", "TPU v5p", "$2,100,000,000,000", "STILL RUNS ON NVIDIA"),
        ("AMAZON", "TRAINIUM 2", "$2,200,000,000,000", "STILL RUNS ON NVIDIA"),
        ("MICROSOFT", "MAIA 100", "$3,100,000,000,000", "STILL RUNS ON NVIDIA"),
        ("META", "MTIA v2", "$1,600,000,000,000", "STILL RUNS ON NVIDIA")
    ]
    
    col_w = 300
    for i, (corp, chip, cap, status) in enumerate(columns):
        x1 = 300 + i * (col_w + 35)
        x2 = x1 + col_w
        draw.rounded_rectangle([x1, 260, x2, 850], radius=16, fill=(22, 24, 30), outline=(60, 65, 78), width=2)
        draw.text((x1 + 25, 290), f"GIANT 0{i+1}", fill=(140, 145, 160), font=f_mono_sm)
        draw.text((x1 + 25, 325), corp, fill=(247, 245, 239), font=f_bebas)
        
        draw.text((x1 + 25, 420), "CUSTOM SILICON:", fill=(245, 197, 66), font=f_mono_sm)
        draw.text((x1 + 25, 450), chip, fill=(255, 255, 255), font=f_mono_lg)
        
        draw.text((x1 + 25, 520), "MARKET CAP:", fill=(140, 145, 160), font=f_mono_sm)
        draw.text((x1 + 25, 550), cap, fill=(180, 185, 200), font=f_mono_sm)
        
        # Stamp Box
        draw.rectangle([x1 + 20, 680, x2 - 20, 780], fill=(180, 40, 30, 220), outline=(240, 70, 60), width=2)
        draw.text((x1 + 35, 705), "FAILED TO ESCAPE", fill=(255, 255, 255), font=f_bebas)
        draw.text((x1 + 30, 800), "CUDA LOCK-IN", fill=(200, 60, 50), font=f_mono_sm)

    img.save(os.path.join(PUB_IMG, 'coalition_card.png'), quality=95)
    print("Saved coalition_card.png")

# 2. THE FATAL MISTAKE (CUDA Architecture Lock-in)
def make_fatal_mistake_card():
    img = Image.new('RGB', (1920, 1080), (6, 6, 7))
    draw = ImageDraw.Draw(img)
    
    # High-impact stark charcoal frame
    draw.rounded_rectangle([320, 140, 1600, 940], radius=24, fill=(14, 15, 18), outline=(60, 65, 75), width=3)
    draw.text((380, 190), "THE ARCHITECTURAL MOAT // 2006 -> 2026", fill=(245, 197, 66), font=f_mono)
    draw.text((380, 240), "THE FATAL MISTAKE", fill=(255, 255, 255), font=f_bebas_xl)
    draw.line([(380, 340), (1540, 340)], fill=(50, 55, 65), width=2)
    
    draw.text((380, 380), "IN 2006, JENSEN HUANG FORCED EVERY CHIP TO RUN CUDA.", fill=(245, 197, 66), font=f_mono_lg)
    draw.text((380, 440), "WALL STREET CALLED IT A DISASTER AND CRUSHED NVIDIA'S STOCK BY 70%.", fill=(180, 185, 195), font=f_mono)
    draw.text((380, 480), "THEY THOUGHT HE WAS BUILDING GRAPHICS HARDWARE.", fill=(180, 185, 195), font=f_mono)
    
    # Massive bottom thesis quote
    draw.rounded_rectangle([380, 560, 1540, 870], radius=16, fill=(20, 22, 28), outline=(245, 197, 66), width=2)
    draw.text((430, 610), '"YOU CAN REPLICATE THE HARDWARE IN 3 YEARS.', fill=(255, 255, 255), font=f_bebas)
    draw.text((430, 680), 'YOU CANNOT REPLICATE 5,000,000 DEVELOPERS."', fill=(245, 197, 66), font=f_bebas)
    draw.text((430, 770), "// WALL STREET DISMISSAL COST: $3.4 TRILLION IN VALUE", fill=(160, 165, 175), font=f_mono)

    img.save(os.path.join(PUB_IMG, 'fatal_mistake_card.png'), quality=95)
    print("Saved fatal_mistake_card.png")

# 3. ZUCK CLUSTER CARD (350,000 GPUs)
def make_zuck_cluster_card():
    img = Image.new('RGB', (1920, 1080), (11, 11, 14))
    draw = ImageDraw.Draw(img)
    
    draw.rounded_rectangle([300, 140, 1620, 940], radius=24, fill=(16, 17, 22), outline=(45, 50, 65), width=3)
    draw.text((360, 190), "META AI INFRASTRUCTURE PROCUREMENT AUDIT", fill=(245, 197, 66), font=f_mono)
    draw.text((360, 240), "350,000 NVIDIA H100s", fill=(255, 255, 255), font=f_bebas_xl)
    draw.line([(360, 340), (1560, 340)], fill=(50, 55, 65), width=2)
    
    # Left Box
    draw.rounded_rectangle([360, 380, 930, 860], radius=16, fill=(22, 25, 32), outline=(60, 65, 78), width=2)
    draw.text((400, 420), "PURCHASE ORDER // 2024", fill=(140, 145, 160), font=f_mono)
    draw.text((400, 460), "$10.5 BILLION", fill=(245, 197, 66), font=f_bebas_xl)
    draw.text((400, 570), "HARDWARE: NVIDIA H100 TENSOR CORE", fill=(255, 255, 255), font=f_mono_sm)
    draw.text((400, 610), "BUYER: MARK ZUCKERBERG / META", fill=(180, 185, 195), font=f_mono_sm)
    draw.text((400, 650), "ELECTRICITY DRAW: 700 MEGAWATTS", fill=(180, 185, 195), font=f_mono_sm)
    draw.text((400, 750), '"WE ARE BUILDING MASSIVE COMPUTE."', fill=(247, 245, 239), font=f_mono)
    
    # Right Box
    draw.rounded_rectangle([990, 380, 1560, 860], radius=16, fill=(22, 25, 32), outline=(60, 65, 78), width=2)
    draw.text((1030, 420), "STRATEGIC OUTCOME", fill=(140, 145, 160), font=f_mono)
    draw.text((1030, 460), "TOTAL CAPITULATION", fill=(240, 70, 60), font=f_bebas_xl)
    draw.text((1030, 570), "IN-HOUSE MTIA CHIPS: SHELVED", fill=(200, 60, 50), font=f_mono_sm)
    draw.text((1030, 610), "REASON: CUDA KERNEL COMPATIBILITY", fill=(180, 185, 195), font=f_mono_sm)
    draw.text((1030, 650), "LLAMA 3 TRAINED 100% ON NVIDIA", fill=(245, 197, 66), font=f_mono_sm)
    draw.text((1030, 750), "SURRENDER TO JENSEN COMPLETE.", fill=(255, 255, 255), font=f_mono)

    img.save(os.path.join(PUB_IMG, 'zuck_cluster_card.png'), quality=95)
    print("Saved zuck_cluster_card.png")

# 4. VALUATION ASYMMETRY CARD ($3.4 Trillion)
def make_valuation_card():
    img = Image.new('RGB', (1920, 1080), (8, 8, 9))
    draw = ImageDraw.Draw(img)
    
    draw.rounded_rectangle([280, 120, 1640, 960], radius=24, fill=(15, 16, 20), outline=(50, 55, 68), width=3)
    draw.text((340, 160), "MARKET CAPITALIZATION DIVERGENCE // 1999 -> 2024", fill=(245, 197, 66), font=f_mono)
    draw.text((340, 200), "$3,400,000,000,000", fill=(255, 255, 255), font=f_bebas_giant)
    draw.line([(340, 360), (1580, 360)], fill=(50, 55, 65), width=2)
    
    # 2 Comparison Columns
    # Left: 1999 IPO
    draw.rounded_rectangle([340, 400, 920, 890], radius=16, fill=(20, 22, 28), outline=(55, 60, 72), width=2)
    draw.text((380, 440), "NVIDIA IPO // JAN 1999", fill=(140, 145, 160), font=f_mono)
    draw.text((380, 480), "$230 MILLION", fill=(180, 185, 200), font=f_bebas_xl)
    draw.text((380, 590), "PRODUCT: RIVA 128 / GEFORCE 256", fill=(160, 165, 175), font=f_mono_sm)
    draw.text((380, 630), "PERCEPTION: 'NICHE PC GAMING TOY'", fill=(200, 60, 50), font=f_mono_sm)
    draw.text((380, 720), "OFFICE: DENNY'S RESTAURANT BOOTH", fill=(245, 197, 66), font=f_mono)
    
    # Right: Today
    draw.rounded_rectangle([980, 400, 1580, 890], radius=16, fill=(20, 22, 28), outline=(245, 197, 66), width=2)
    draw.text((1020, 440), "NVIDIA TODAY // 2024", fill=(245, 197, 66), font=f_mono)
    draw.text((1020, 480), "$3.4 TRILLION", fill=(255, 255, 255), font=f_bebas_xl)
    draw.text((1020, 590), "EXCEEDS ENTIRE GERMAN STOCK MARKET (DAX 40)", fill=(245, 197, 66), font=f_mono_sm)
    draw.text((1020, 630), "MORE VALUABLE THAN ALL OF SILICON VALLEY COMBINED IN 2010", fill=(180, 185, 200), font=f_mono_sm)
    draw.text((1020, 720), "THE TOLL BOOTH OF CIVILIZATION.", fill=(255, 255, 255), font=f_mono)

    img.save(os.path.join(PUB_IMG, 'valuation_card.png'), quality=95)
    print("Saved valuation_card.png")

make_coalition_card()
make_fatal_mistake_card()
make_zuck_cluster_card()
make_valuation_card()
print("All D7 evidence cards rendered successfully!")

