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
            if event.key == pg.K_LEFT or event.key == pg.K_a:
                moveRight = False
                moveLeft = True
            if event.key == pg.K_RIGHT or event.key == pg.K_d:
                moveRight = True
                moveLeft = False
            if event.key == pg.K_DOWN or event.key == pg.K_s:
                moveDown = True
                moveUp = False
            if event.key == pg.K_UP or event.key == pg.K_w:
                moveDown = False
                moveUp = True
        if event.type == pg.KEYUP:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
            elif event.key == pg.K_LEFT or event.key == pg.K_a:
                moveLeft = False
            elif event.key == pg.K_RIGHT or event.key == pg.K_d:
                moveRight = False
            elif event.key == pg.K_DOWN or event.key == pg.K_s:
                moveDown = False
            elif event.key == pg.K_UP or event.key == pg.K_w:
                moveUp = False
            if event.key == pg.K_x:
                player.top = random.randint(0, WindowHeight - player.height)
                player.left = random.randint(0, WindowWidth - player.width)
        if event.type == pg.MOUSEBUTTONUP:
            foods.append(pg.Rect(event.pos[0], event.pos[1], foodSize, foodSize))
            foodCounter += 1
            if foodCounter >= newFood:
                foodCounter = 0
                foods.append(pg.Rect(random.randint(0, WindowWidth - foodSize), \
                                     random.randint(0, WindowHeight - foodSize), \
                                     foodSize, foodSize))
        # draw white background
        windowSurface.fill(white)
        # move the player
        if moveLeft and player.left > 0:
            player.left -= moveSpeed
        if moveRight and player.right < WindowWidth:
            player.right += moveSpeed
        if moveUp and player.top > 0:
            player.top -= moveSpeed
        if moveDown and player.bottom < WindowHeight:
            player.bottom += moveSpeed
        # draw player
        pg.draw.rect(windowSurface, black, player)

        # draw foods
        for i in range(len(foods)):
            pg.draw.rect(windowSurface, green, foods[i])


        # draw the window onto the screen
        pg.display.update()
        mainClock.tick(40)


