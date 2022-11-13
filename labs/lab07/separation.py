import sys,math
from PIL import Image
from pixel import *

def red(img):
    newimage = Image.new('RGB', img.size)
    for x in range(img.width):
        for y in range(img.height):
            r,g,b = getpixel(img, x, y)
            putpixel(newimage, x,y, (r,0,0))
    return newimage

def green(img):
    newimage = Image.new('RGB', img.size)
    for x in range(img.width):
        for y in range(img.height):
            r,g,b = getpixel(img, x, y)
            putpixel(newimage, x,y, (0,g,0))
    return newimage

def blue(img):
    newimage = Image.new('RGB', img.size)
    for x in range(img.width):
        for y in range(img.height):
            r,g,b = getpixel(img, x, y)
            putpixel(newimage, x,y, (0,0,b))
    return newimage
