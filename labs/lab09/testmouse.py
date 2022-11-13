
import os, pygame
from pygame.locals import *
import random, math

pygame.init()
screen = pygame.display.set_mode((400,400))
running = True
while running:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            print('pos:', event.pos)
            print('button:', event.button)
        elif event.type == QUIT:
            running = False
            break

pygame.quit()
