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
        self.isJumping = False
        self.jumpTimer = 0
        self.jumpHeight = 20

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

    def jump(self):
        self.isJumping = True
        if self.isJumping:
            self.isFalling = False
            for i in range(0, self.jumpHeight):
                self.rect.y -= 1
        if self.jumpTimer == 0 and not self.isJumping:
            self.isJumping = True
            self.jumpTimer = 60


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

Ground = Object((-10,500),screen.get_width()+50, 5)

platforms = [Ground, Object((100,400),200, 5), Object((200,300),200, 5), Object((300,250),200, 5)]
platformColl = []
for platform in platforms:
    platformColl.append(platform.rect)



while True:#Keyrir leikinn
    screen.fill(WHITE)

    if player.isFalling and not player.isJumping:
        player.rect.y += gravity
    elif player.isJumping:
        if player.jumpTimer > 0:
            player.jumpTimer -= 1
        else:
            player.isJumping = False

        print(player.jumpTimer)
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
                if not player.isJumping and player.jumpTimer == 0:
                    player.jump()
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