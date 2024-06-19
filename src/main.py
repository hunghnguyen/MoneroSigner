# first show we are alive!
from xmrsigner.hardware.ST7789 import ST7789
from PIL import Image, ImageDraw, ImageFont
dispaly = ST7789()
display.reset()
# here we need to generate brief some image 240x240px, or smaller and ajust x/y
image: Image = Image.new('RGB', (240, 240), 'white')
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()  # You may need to specify a specific font
text = 'Loading...'
text_width, text_height = draw.textsize(text, font)
x = (240 - text_width) // 2
y = (240 - text_height) // 2
draw.text((x, y), text, fill='red', font=font)
display.ShowImage(image, 0, 0)
del image, draw, font, text, text_width, text_height, x, y, display
# and destroy all variables and objects to not interfere

from xmrsigner.controller import Controller
# Get the one and only Controller instance and start our main loop
Controller.get_instance().start()
