##
import os
import sys
import time
import pygame as pg

pg.init()

# create the window 
WindowWidth = 500
WindowHeight = 500
windowSurface = pg.display.set_mode((WindowWidth, WindowHeight), 0, 32)
pg.display.set_caption("Demo of Animation")

# set direction vars
UpLeft = 'upleft'
UpRight = 'upright'
DownLeft = 'downleft'
DownRight = 'downright'

MoveSpeed = 1

# set up the colors
white = (255, 255, 255)
teal = (0, 128, 128)
red  = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# set up the boxes
box_1 =  {'rect': pg.Rect(300, 80, 50, 110), 'color': red, 'direct': UpRight}
box_2 =  {'rect': pg.Rect(100, 100, 30, 30), 'color': green, 'direct': DownLeft}

boxes = [box_1, box_2 ]

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
    for b in boxes:
        if b['direct'] == DownLeft:
            b['rect'].left -= MoveSpeed
            b['rect'].top  += MoveSpeed
        elif b['direct'] == UpRight:
            b['rect'].left += MoveSpeed
            b['rect'].top  -= MoveSpeed
        elif b['direct'] == UpLeft:
            b['rect'].left -= MoveSpeed
            b['rect'].top  -= MoveSpeed
        elif b['direct'] == DownRight:
            b['rect'].left += MoveSpeed
            b['rect'].top  += MoveSpeed
        # check whether the box has moved out of the window
        if b['rect'].top < 0:
            # the box has moved past the top
            if b['direct'] == UpLeft:
                b['direct'] = DownLeft
            elif b['direct'] == UpRight:
                b['direct'] = DownRight
        if b['rect'].bottom > WindowHeight:
            if b['direct'] == DownLeft:
                b['direct'] = UpLeft
            elif b['direct'] == DownRight:
                b['direct'] = UpRight
        if b['rect'].left < 0:
            if b['direct'] == UpLeft:
                b['direct'] = UpRight
            elif b['direct'] == DownLeft:
                b['direct'] = DownRight
        if b['rect'].right > WindowWidth:
            if b['direct'] == UpRight:
                b['direct'] = UpLeft
            elif b['direct'] == DownRight:
                b['direct'] = DownLeft

        # re-draw the boxes
        pg.draw.rect(windowSurface, b['color'], b['rect'])
            
            

    # draw the window onto the screen
    pg.display.update()
    time.sleep(0.02)  # 50 HZ
