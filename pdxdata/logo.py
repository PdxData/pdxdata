#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A library for creating a pixelated (i.e. dot matrix) image of a string, like for the "PDXData" logo"""

# import sys

# from colorama import init
# init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
# from termcolor import cprint
# from pyfiglet import figlet_format

# cprint(figlet_format('PDX\nData', font='starwars'),
#        'yellow', 'on_red', attrs=['bold'])


# pip install --upgrade pip
# pip install --upgrade pillow
from PIL import Image, ImageFont, ImageDraw

width = 32 * 4
height = 32
size = (width, height)
background = (255, 255, 255)
foreground = (32, 32, 32)
filename = 'logo.bmp'
pitch = 15
pos1 = (6, 0)
pos2 = (0, 15)
img = Image.new("RGBA", size, background)
font = ImageFont.truetype("arial.ttf", pitch)
pen = ImageDraw.Draw(img)
pen.text((6, 0), "PDX", foreground, font=font)
pen.text((0, 15), "Data", foreground, font=font)
img.save('logo.bmp')
img.show()
