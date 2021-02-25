import pygame as pg
import random
#from colors import *

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
        self.speedx = 5
    def update(self):
        #self.rect.x-= self.speedx
        self.rect.y+= self.speedx

        #if self.rect.right > WIDTH:
            #self.rect.left=0
        if self.rect.left > WIDTH:
            self.rect.right=0
        if self.rect.bottom < HEIGHT:
            self.rect.centery=0
        if self.rect.top < 0:
            self.rect.centery=HEIGHT




WIDTH = 360
HEIGHT = 480
FPS = 30
title = "Template"

#color
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (128,0,128)
BBBLUE = (137,207,240)
RED_ORANGE = (255,69,0)
ORANGE = (255,165,0)
GOLD = (255,215,0)
BBPINK = (255,182,193)
YELLOW = (255,255,0)



pg.init()
pg.mixer.init()


screen=pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption(title)
clock = pg.time.Clock()

#create sprites
all_Sprites = pg.sprite.Group()
players_group = pg.sprite.Group()

#creat objects
player = Player()


#add objects to sprite
all_Sprites.add(player)
players_group.add(player)

#game loop
running = True
while running:
    clock.tick(FPS)

    #process input
    #get list of events
    for event in pg.event.get():
        #checking events
        if event.type == pg.QUIT:
            running = False

    #make updates
    all_Sprites.update()

    #render (Draw)
    screen.fill(GREEN)
    all_Sprites.draw(screen)


    #last thing we do in loop
    pg.display.flip()

pg.quit()