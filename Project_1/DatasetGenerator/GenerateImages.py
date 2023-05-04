from PIL import Image, ImageDraw, ImageFont
import os
# from matplotlib import font_manager
# fonts = font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
fonts = None
with open("fonts.txt") as file:
    fonts = file.read().splitlines()

for i in range(len(fonts)):
    font = ImageFont.truetype(fonts[i],30);
    
    for char in range(ord('A'),ord('Z')+1):
        folder = "./"+chr(char)+"/"
        if not os.path.exists(folder):
            os.mkdir(folder)
        img = Image.new('L', (32, 32), color = 0)
        d = ImageDraw.Draw(img)
        d.text((16,16), chr(char), fill=255, font=font, anchor="mm")
        fontName = fonts[i].split("\\").pop()
        img.save(folder + str(i) + ".jpg")