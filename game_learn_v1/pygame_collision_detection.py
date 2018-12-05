import sys, os
import pygame as pg
import random

# set up pygame 
pg.init()
mainClock = pg.time.Clock()

# set up the window surface
WindowWidth = 500
WindowHeight = 500
windowSurface = pg.display.set_mode((WindowWidth, WindowHeight), 0, 32)
pg.display.set_caption('Collsion Detection')

# set up the colors 
black = (0, 0, 0)
green = (0,  255, 0)
white = (255, 255, 255)

# set up player and food
foodCounter = 0
newFood = 40
foodSize = 20
player = pg.Rect(300, 100, 50, 50)
foods = []

for i in range(20):
    foods.append(pg.Rect(random.randint(0, WindowWidth - foodSize), \
                         random.randint(0, WindowHeight - foodSize),\
                         foodSize, foodSize))

# set up movement variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
moveSpeed = 6

# run the game loop
while True:
    # check for events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT or event.type == pg.K_a:
                moveRight = False
                moveLeft = True

