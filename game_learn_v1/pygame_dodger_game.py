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
    score = 0
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
            #elif event.type == pg.KEYDOWN:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_z:
                    reverseCheat = True 
                elif event.key == pg.K_x:
                    slowCheat = True 
                elif event.key == pg.K_LEFT or event.key == pg.K_a:
                    moveLeft = True
                    moveRight = False
                elif event.key == pg.K_RIGHT or event.key == pg.K_d:
                    moveLeft = False
                    moveRight = True
                elif event.key == pg.K_UP or event.key == pg.K_w:
                    moveUp = True
                    moveDown = False
                elif event.key == pg.K_DOWN or event.key == pg.K_s:
                    moveUp = False
                    moveDown = True
            #elif event.type == pg.KEYUP:
            if event.type == pg.KEYUP:
                if event.key == pg.K_z:
                    reverseCheat = False
                    score = 0
                elif event.key == pg.K_x:
                    slowCheat = False
                    score = 0
                elif event.key == pg.K_ESCAPE:
                    terminate() 
                elif event.key == pg.K_LEFT or event.key == pg.K_a:
                    moveLeft = False
                elif event.key == pg.K_RIGHT or event.key == pg.K_d:
                    moveRight = False
                elif event.key == pg.K_UP or event.key == pg.K_w:
                    moveUp = False
                elif event.key == pg.K_DOWN or event.key == pg.K_s:
                    moveDown = False
            #elif event.type == pg.MOUSEMOTION:
            if event.type == pg.MOUSEMOTION:
                # move the player to the cursor
                playerRect.centerx = event.pos[0]
                playerRect.centery = event.pos[1]
            # add new baddies 
            if not reverseCheat and not slowCheat:
                baddieAddCounter += 1
                #print("baddie Add counter = {}".format(baddieAddCounter))
            if baddieAddCounter == addNewBaddieRate:
                baddieAddCounter = 0
                baddieSize = random.randint(baddieMinSize, baddieMaxSize)
                newBaddie = {'rect': pg.Rect(random.randint(0, WindowWidth - baddieSize), \
                                             0 - baddieSize, baddieSize, baddieSize), 
                             'speed': random.randint(baddieMinSpeed, baddieMaxSpeed),
                             'surface': pg.transform.scale(baddieImage, (baddieSize, baddieSize)), }
                baddies.append(newBaddie)
                #print(" == {}, baddie Add counter = {}".format(addNewBaddieRate,baddieAddCounter))
        # move the player
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * playerMoveRate, 0)
        elif moveRight and playerRect.right < WindowWidth:
            playerRect.move_ip(+1 * playerMoveRate, 0)
        elif moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * playerMoveRate)
        elif moveDown and playerRect.bottom < WindowHeight:
            playerRect.move_ip(0, +1 * playerMoveRate)
        # move the baddie down
        for bd in baddies:
            if not reverseCheat and not slowCheat:
                bd['rect'].move_ip(0, bd['speed'])
            elif reverseCheat:
                bd['rect'].move_ip(0, -5)
            elif slowCheat:
                bd['rect'].move_ip(0, 1)
        # delete fallen baddie
        for bd in baddies[:]:
            if bd['rect'].top > WindowHeight:
                baddies.remove(bd)
        # draw the window
        windowSurface.fill(backgroundColor)
        # draw the score + top score
        drawText('score: %s' % (score), font, windowSurface, 10, 0)
        drawText('top score: %s' % (topScore), font, windowSurface, 10, 40)
        # draw the player
        windowSurface.blit(playerImage, playerRect)
        # draw baddie
        for bd in baddies:
            windowSurface.blit(bd['surface'], bd['rect'])

        pg.display.update()
        # collide check
        if playerHitBaddie(playerRect, baddies):
            if score > topScore:
                topScore = score
            break
        mainClock.tick(fps)

    # stop game
    pg.mixer.music.stop()
    gameoverSound.play()
    drawText('game over', font, windowSurface, (WindowWidth / 3), (WindowHeight / 3))
    drawText('press a key to play again', font, windowSurface, WindowWidth/3-80, WindowHeight/3+50)
    pg.display.update()
    waitForPlayerToPressKey()

    gameoverSound.stop()
