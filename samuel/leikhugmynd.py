import pygame, sys
from pygame.locals import *
from random import *


pygame.init()
#WINDOW SETUP CONFIG
winTitle = 'Samúel'
winHeight = 600
winWidth = 900
window = winHeight*winWidth
FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
screen = pygame.display.set_mode((winWidth, winHeight), 0, 32)
pygame.display.set_caption(winTitle)

WHITE = (255, 255, 255)
RED = (255,   0,   0)

class Player():
    def __init__(self, startPos, width):
        self.start = startPos
        self.width = width
        self.rect = pygame.Rect(self.start, (width, width))
        self.color = (0, 255, 0)
        self.speed = 6
        self.isFalling = True
        self.isMoving = False

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, dir):
        if player.rect.x <= 0:
            player.rect.x = screen.get_width()
        elif player.rect.x+player.rect.w > screen.get_width()+6:
            player.rect.x = 0
        if dir == "Left":
            player.rect.x -= self.speed
        elif dir == "Right":
            player.rect.x += self.speed

class Object():
    def __init__(self, startPos, width, height):
        self.start = startPos
        self.width = width
        self.height = height
        self.end = (width, height)
        self.rect = pygame.Rect(startPos[0], startPos[1], width, height)
        self.width = 5

    def draw(self):
        pygame.draw.rect(screen, (0,0,0), (self.start, self.end))


gravity = 4
direction = ""
player = Player((screen.get_width()/2, 0), 10)

platforms = [Object((-10,500),screen.get_width()+50, 5), Object((100,400),200, 5)]
walls = [Object((50, 100), 5, 400), Object((800, 100), 5, 400)]
platformColl = []
wallColl = []
for platform in platforms:
    platformColl.append(platform.rect)


print(wallColl, player.rect.collidelist(wallColl))

while True:#Keyrir leikinn
    screen.fill(WHITE)

    if player.isFalling:
        player.rect.y += gravity
    player.draw()

    if player.rect.collidelist(platformColl) >= 0:
        player.isFalling = False
    else:
        player.isFalling = True
    if player.isMoving and direction:
        player.move(direction)

    for platform in platforms:
        platform.draw()


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if (event.key == K_SPACE):
                print("jump")
            elif (event.key == K_LEFT):
                player.isMoving = True
                direction = "Left"
            elif (event.key == K_RIGHT):
                player.isMoving = True
                direction = "Right"
        elif event.type == KEYUP:
            if (event.key == K_LEFT):
                player.isMoving = False
            elif (event.key == K_RIGHT):
                player.isMoving = False
    pygame.display.update()
    fpsClock.tick(FPS)