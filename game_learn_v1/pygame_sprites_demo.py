import os, sys
import time, random
import pygame as pg
from pygame.locals import *

# initialization
pg.init()
mainClock = pg.time.Clock()
print(mainClock)

# set up window
WindowWidth = 400
WindowHeight = 400
windowSurface = pg.display.set_mode((WindowWidth, WindowHeight), 0, 32)
pg.display.set_caption("Sprites demo")

# set up the colors
white = (255, 255, 255)
teal = (0, 128, 128)
red  = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# set up player and foods
player = pg.Rect(300, 100, 40, 40)
playerImage = pg.image.load('./sprites_demo/player.png') 
playerStretchedImage = pg.transform.scale(playerImage, (40, 40))

foodSize = 20
foodImage = pg.image.load('./sprites_demo/cherry.png')
foods = []
for i in range(20):
    foods.append(pg.Rect(random.randint(0, WindowWidth - 20), \
                         random.randint(0, WindowHeight- 20), \
                         foodSize, foodSize))

foodCounter = 0
newFood = 40

# setup music
pickupSound = pg.mixer.Sound('./sprites_demo/pickup.wav')
pg.mixer.music.load('./sprites_demo/background.mid')
# playe music (-1: infinite, start: 0.0)
pg.mixer.music.play(-1, 0.0)
musicPlaying = True

# keyboard vars
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
moveSpeed = 6

# run main loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT or event.key == pg.K_a:
                moveRight = False
                moveLeft = True
            elif event.key == pg.K_RIGHT or event.key == pg.K_d:
                moveRight = True
                moveLeft = False
            elif event.key == pg.K_DOWN or event.key == pg.K_s:
                moveDown = True
                moveUp = False
            elif event.key == pg.K_UP or event.key == pg.K_w:
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
            if event.key == pg.K_m:
                if musicPlaying:
                    pg.mixer.music.stop()
                else:
                    pg.mixer.music.play(-1, 0.0)
        if event.type == pg.MOUSEBUTTONUP:
            foods.append(pg.Rect(event.pos[0], event.pos[1], foodSize, foodSize))
            #foods.append(pg.Rect(event.pos[0]-10, event.pos[1]-10, foodSize, foodSize))
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
        # draw player, associate player with image
        #pg.draw.rect(windowSurface, black, player)
        windowSurface.blit(playerStretchedImage, player)

        # check the collision, player grow bigger after eating food
        for food in foods[:]:
            if player.colliderect(food):
                foods.remove(food)
                player = pg.Rect(player.left, player.top, \
                                 player.width + 2, \
                                 player.height + 2)
                playerStretchedImage = pg.transform.scale(playerImage, (player.width, player.height))
                if musicPlaying:
                    pickupSound.play()

        # draw foods
        for food in foods:
            windowSurface.blit(foodImage, food)
            #pg.draw.rect(windowSurface, green, foods[i])

        # draw the window onto the screen
        pg.display.update()
        mainClock.tick(40)






