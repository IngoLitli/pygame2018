import pygame, sys
from pygame.locals import *
from random import *
import math


pygame.init()
#WINDOW SETUP CONFIG
winTitle = 'MazeGen'
winHeight = 600
winWidth = 600
window = winHeight*winWidth
FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
screen = pygame.display.set_mode((winWidth, winHeight), 0, 32)
pygame.display.set_caption(winTitle)

wGap = 20
hGap = 20

vertical = []
horizona = []
for i in range(0, screen.get_width()+wGap, wGap):
    for j in range(0, screen.get_height()+hGap, hGap):
        vertical.append(((i,j),(i,j+hGap)))
        horizona.append(((i,j),(i+wGap,j)))


while True:#Keyrir leikinn
    screen.fill((240,240,240))
    for i in range(0,len(vertical)):
        pygame.draw.line(screen,(0,0,0),vertical[i][0],vertical[i][1])
        pygame.draw.line(screen,(0,0,0),horizona[i][0],horizona[i][1])


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)