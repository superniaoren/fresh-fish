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
