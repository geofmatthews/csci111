# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 09:07:41 2014

@author: matthews
"""

import os, pygame
from pygame.locals import *
import random, math
from vector import V


def handleInput(screen): # return True if we quit
    #Handle Input Events
    for event in pygame.event.get():
        if event.type == QUIT:
            return True
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                return True
            elif event.key == K_s:
                pygame.event.set_blocked(KEYDOWN|KEYUP)
                fname = input("File name?  ")
                pygame.event.set_blocked(0)
                pygame.image.save(screen,fname)
    return False

def clamp(x,low,hi):
    if x < low:
        return low
    if x > hi:
        return hi
    return x

def getColor(x,y,img):
    """ return color for x,y in [0,1) x [0,1) """
    x = clamp(x,0,1)
    y = clamp(y,0,1)

    w,h = img.get_size()
    return img.get_at((int(x*(w-1)), int(y*(h-1))))
    r = x
    g = y
    b = 1-x
    return (int(255*r), int(255*g), int(255*b))

def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
#Initialize Everything
    pygame.init()
    width,height = 300,400
    image = pygame.image.load('geoffinscotland.png')
    image_surface = pygame.Surface(image.get_size())
    image_surface.blit(image,(0,0))

    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption('Colors!')

#Create The Backgound
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((64, 128, 255))

#Display The Background
    screen.blit(background, (0, 0))
    pygame.display.update()

#Prepare Game Objects
    clock = pygame.time.Clock()

    going = True
    pixelsize = 2**8
    width, height = screen.get_size()
    # game loop
    while going:
        going = not(handleInput(screen))
        # start drawing loop
        while pixelsize > 0:
            print('%d x %d pixels' % (pixelsize,pixelsize))
            clock.tick(1)
            for x in range(0,width,pixelsize):
                pygame.display.update()
                xx = x/float(width)
                if x % (width//10) == 0:
                    print(int(100*(1-xx)), 'percent remaining')
                for y in range(0,height,pixelsize):
                    yy = y/float(height)
                    # draw into background surface
                    color = getColor(xx+pixelsize/width,yy+pixelsize/height,
                                     image_surface)
                    background.fill(color, ((x,y),(pixelsize,pixelsize)))
                    #draw background into screen
                    screen.blit(background, (0,0))
                    if handleInput(screen):
                        return
                            
            pixelsize = pixelsize//2



#this calls the 'main' function when this script is executed
if __name__ == '__main__':
    try:
        main()
    finally:
        pygame.quit()
