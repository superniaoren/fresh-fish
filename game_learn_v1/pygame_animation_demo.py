##
import os
import sys
import time
import pygame as pg

pg.init()

# create the window 
WindowWidth = 400
WindowHeight = 300
windowSurface = pg.display.set_mode((WindowWidth, WindowHeight), 0, 32)
pg.display.set_caption("Demo of Animation")

# set direction vars
UpLeft = 'upleft'
UpRight = 'upright'
DownLeft = 'downleft'
DownRight = 'downright'

MoveSpeed = 4

# set up the colors
white = (255, 255, 255)
teal = (0, 128, 128)
red  = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# set up the boxes
box_1 =  {'rect': pg.Rect(300, 80, 50, 110), 'color': red, 'direct': UpRight}

boxes = [box_1 ]

# run the main loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
    # color the background by white
    # [zoo] NOTE: will not show the render result if not update
    windowSurface.fill(white)

    # TODO: add the box move 

    # draw the window onto the screen
    pg.display.update()
    time.sleep(0.02)  # 50 HZ
