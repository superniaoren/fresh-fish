import os, sys
import random
import pygame as pg

# global vars
WindowWidth = 600
WindowHeight = 600
textColor = (0, 0, 0)  # black
backgroundColor = (255, 255, 255) # white

fps = 50

baddieMinSize = 10
baddieMaxSize = 40
baddieMinSpeed = 1
baddieMaxSpeed = 8
addNewBaddieRate = 6
playerMoveRate = 5

def terminate():
    pg.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    terminate()
                return 

def playerHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, textColor)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# set up pygame
pg.init()
mainClock = pg.time.Clock()
windowSurface = pg.display.set_mode((WindowWidth, WindowHeight))
pg.display.set_caption('dodger')
pg.mouse.set_visible(False)

font = pg.font.SysFont(None, 48)

gameoverSound = pg.mixer.Sound('./dodger_demo/gameover.wav')
pg.mixer.music.load('./dodger_demo/background.mid')

playerImage = pg.image.load('./dodger_demo/player.png')
playerRect = playerImage.get_rect()
baddieImage = pg.image.load('./dodger_demo/baddie.png')

windowSurface.fill(backgroundColor)
drawText('dodger', font, windowSurface, (WindowWidth/3), (WindowHeight/3))

drawText('+' * 40, font, windowSurface, (WindowWidth/3)-25, (WindowHeight/3)-30)
drawText('press a key to start ', font, windowSurface, (WindowWidth/3)-30, (WindowHeight/3)+50)
drawText('+' * 40, font, windowSurface, (WindowWidth/3)-25, (WindowHeight/3)+80)
pg.display.update()
waitForPlayerToPressKey()

topScore = 0
while True:
    # set up the start 
    baddies = []
    score = []
    playerRect.topleft = (WindowWidth / 2, WindowHeight - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0
    pg.mixer.music.play(-1, 0.0)

    # game loop
    while True:
        score += 1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_z:
                    reverseCheat = True 
                elif event.key == pg.K_x:
                    slowCheat = True 
