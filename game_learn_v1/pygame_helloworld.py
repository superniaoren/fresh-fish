## 
import sys
import pygame as pg

pg.init()

windowSurface = pg.display.set_mode((500, 400), 0, 32)
pg.display.set_caption("learn pg, hola")

# colors: rgb
black = (0, 0, 0)
white = (255, 255, 255)
red   = (255, 0, 0)
green = (0, 255, 0)
blue  = (0, 0, 255)

# fonts:
basicFont = pg.font.SysFont(None, 48)

# set up text
text = basicFont.render("HOla", True, white, blue)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# white the superface background
windowSurface.fill(white)

# axis(x, y): -------> y
#             |
#             |
#             v x

# draw a gree polygon onto the surface
pg.draw.polygon(windowSurface, green, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# add some blue lines
pg.draw.line(windowSurface, blue, (60, 60), (120, 60), 4)
pg.draw.line(windowSurface, red,  (120, 60), (180, 60), 5)
pg.draw.line(windowSurface, black, (120, 60), (120, 120), 6)



# draw  the winodw onto the screen
pg.display.update()

# run the game loop
# [zoo, deprecated/error:] or else, the window disapear soon
while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
