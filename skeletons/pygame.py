import pygame, sys
from pygame.locals import *
from random import *
import math


pygame.init()
#WINDOW SETUP CONFIG
winTitle = 'Skeleton'
winHeight = 600
winWidth = 900
window = winHeight*winWidth
FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
screen = pygame.display.set_mode((winWidth, winHeight), 0, 32)
pygame.display.set_caption(winTitle)



while True:#Keyrir leikinn
    screen.fill(WHITE)


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)