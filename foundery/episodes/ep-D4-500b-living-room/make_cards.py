"""Generate high-res 2.5D evidence cards for Episode D4."""
from PIL import Image, ImageDraw, ImageFont
import os

HERE = r'D:\agency content\BIN\documentary_tofu\ep-D4-500b-living-room\build\public\img'
os.makedirs(HERE, exist_ok=True)

# 1. YC S05 Cohort Breakdown Card
w, h = 1200, 750
im = Image.new('RGBA', (w, h), (14, 17, 23, 245))
draw = ImageDraw.Draw(im)

# Outer border
draw.rectangle([10, 10, w-10, h-10], outline=(45, 55, 72, 255), width=2)
draw.rectangle([14, 14, w-14, h-14], outline=(30, 41, 59, 255), width=1)

# Header
draw.rectangle([14, 14, w-14, 80], fill=(20, 26, 36, 255))
draw.text((40, 35), "Y COMBINATOR  //  SUMMER 2005 INAUGURAL COHORT", fill=(245, 197, 66, 255))
draw.text((w-280, 35), "CAMBRIDGE, MA  ·  8 STARTUPS", fill=(139, 139, 139, 255))

# 3 Columns for Titans
col_w = 360
# Col 1: Reddit
draw.rectangle([40, 110, 40+col_w, h-120], fill=(20, 24, 33, 255), outline=(40, 50, 68, 255), width=1)
draw.text((65, 140), "REDDIT (INFOSOCKET)", fill=(247, 245, 239, 255))
draw.text((65, 180), "FOUNDERS: STEVE HUFFMAN & ALEXIS OHANIAN", fill=(200, 58, 42, 255))
draw.text((65, 230), "VALUATION: $10.0 BILLION", fill=(245, 197, 66, 255))
draw.text((65, 280), "Publicly traded NYSE: RDDT\nOver 80M daily active users.\nStarted with 2 college grads\nin Paul Graham's kitchen.", fill=(160, 174, 192, 255))

# Col 2: Twitch / Kiko
draw.rectangle([420, 110, 420+col_w, h-120], fill=(20, 24, 33, 255), outline=(40, 50, 68, 255), width=1)
draw.text((445, 140), "KIKO (TWITCH / JUSTIN.TV)", fill=(247, 245, 239, 255))
draw.text((445, 180), "FOUNDERS: JUSTIN KAN & EMMETT SHEAR", fill=(78, 113, 255, 255))
draw.text((445, 230), "ACQUIRED: $970 MILLION (AMAZON)", fill=(245, 197, 66, 255))
draw.text((445, 280), "Pioneered web livestreaming.\nEvolved into Twitch.tv,\nstreaming 2.5M concurrent\nviewers worldwide.", fill=(160, 174, 192, 255))

# Col 3: Loopt / OpenAI
draw.rectangle([800, 110, 800+col_w, h-120], fill=(20, 24, 33, 255), outline=(40, 50, 68, 255), width=1)
draw.text((825, 140), "LOOPT (SAM ALTMAN)", fill=(247, 245, 239, 255))
draw.text((825, 180), "FOUNDER: SAM ALTMAN (AGE 19)", fill=(245, 197, 66, 255))
draw.text((825, 230), "SUBSEQUENT: OPENAI ($157B)", fill=(245, 197, 66, 255))
draw.text((825, 280), "Youngest founder in batch.\nBecame YC President (2014).\nCo-founded OpenAI (2015),\nlaunching the generative AI era.", fill=(160, 174, 192, 255))

# Footer
draw.text((40, h-70), "SOURCE: Y COMBINATOR HISTORICAL ARCHIVE  ·  CAMBRIDGE APARTMENT FOUNDERS", fill=(139, 139, 139, 255))
draw.text((w-360, h-70), "COMBINED ENTERPRISE IMPACT: >$500B", fill=(245, 197, 66, 255))

im.save(os.path.join(HERE, 'yc_s05_cohort_card.png'))
print('Saved yc_s05_cohort_card.png')

