import os
from PIL import Image, ImageDraw, ImageFont

PUB_IMG = r'D:\agency content\BIN\documentary_tofu\ep-D4-500b-living-room\build\public\img'
PUB_FONTS = r'D:\agency content\BIN\documentary_tofu\ep-D4-500b-living-room\build\public'

f_mono_sm = ImageFont.truetype(os.path.join(PUB_FONTS, 'ibm-plex-mono-400.ttf'), 16)
f_mono = ImageFont.truetype(os.path.join(PUB_FONTS, 'ibm-plex-mono-600.ttf'), 22)
f_bebas_xl = ImageFont.truetype(os.path.join(PUB_FONTS, 'bebas-neue-400.ttf'), 84)

img = Image.new('RGB', (1920, 1080), (11, 11, 12))
draw = ImageDraw.Draw(img)

card_box = [340, 150, 1580, 930]
draw.rounded_rectangle(card_box, radius=20, fill=(18, 20, 24), outline=(245, 197, 66), width=3)

# Header
draw.text((390, 190), 'Y COMBINATOR SUMMER 2005 // THE PIVOT DIRECTIVE', fill=(245, 197, 66), font=f_mono)
draw.text((390, 230), 'PAUL GRAHAM (CO-FOUNDER, Y COMBINATOR) -> STEVE HUFFMAN & ALEXIS OHANIAN', fill=(160, 165, 175), font=f_mono_sm)
draw.line([(390, 260), (1530, 260)], fill=(50, 55, 65), width=2)

# Quote Box
draw.rectangle([390, 290, 1530, 680], fill=(24, 26, 32), outline=(60, 65, 80))
draw.text((430, 330), '"YOUR IDEA IS DEAD.', fill=(255, 69, 0), font=f_bebas_xl)
draw.text((430, 425), 'BUT WE LIKE YOU.', fill=(247, 245, 239), font=f_bebas_xl)
draw.text((430, 520), 'BUILD THE FRONT PAGE OF THE INTERNET."', fill=(245, 197, 66), font=f_bebas_xl)

# Footer context
draw.rectangle([390, 720, 1530, 870], fill=(20, 20, 24))
draw.text((430, 745), 'HISTORICAL CONTEXT // JUNE 2005', fill=(78, 113, 255), font=f_mono)
draw.text((430, 785), 'Called founders at Boston train station 1 hour after rejecting their mobile menu app.', fill=(210, 215, 225), font=f_mono_sm)
draw.text((430, 815), 'Result: Huffman coded the Reddit prototype in Cambridge over the next 20 days.', fill=(160, 165, 175), font=f_mono_sm)

out = os.path.join(PUB_IMG, 'paul_graham_card.png')
img.save(out)
print('Saved:', out)

