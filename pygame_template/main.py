import pygame as pg
import random
import math
#from colors import *


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        #self.rect.bottomright = (0,0)
        self.rect.center = (WIDTH/2,HEIGHT/2)
        self.speedx = 5
        self.speedy = 5

    def update(self):
        pass


class NPC(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((15,15))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        #self.rect.bottomright = (0,0)
        self.rect.center = (WIDTH/2,HEIGHT/2)
        self.speedx = 5
        self.speedy = 5

        self.center_x = self.rect.centerx
        self.center_y = self.rect.centery

        self.angle = 1
        self.radius = 75
        self.speed = .1
    def update(self):
        # self.rect.x+= self.speedx
        # self.rect.y+= self.speedy

            #cirlce move
        self.rect.centerx = self.radius * math.sin(self.angle) + self.center_x
        self.rect.centery = self.radius * math.cos(self.angle) + self.center_y
        self.angle += self.speed







        # if self.rect.centerx > WIDTH/2:
        #     self.speedx = 5
        #     self.speedy = -5
        #
        # if self.rect.bottomleft :



            #square
        # if self.rect.right == WIDTH:
        #     self.speedx = 0
        #     self.speedy = -5
        #
        # if self.rect.top == 0:
        #     self.speedx = -5
        #     self.speedy = 0
        #
        # if self.rect.left == 0:
        #     self.speedx = 0
        #     self.speedy = 5
        #
        # if self.rect.bottom == HEIGHT and self.rect.right != WIDTH:
        #     self.speedx = 5
        #     self.speedy = 0


            #warping
        # if self.rect.left > WIDTH:
        #     self.speedy = -5
        #     self.speedx = 0
        #     self.rect.centerx = WIDTH/2
        #     self.rect.top=HEIGHT
        #
        # if self.rect.bottom < 0:
        #     self.speedx = 5
        #     self.speedy = 0
        #     self.rect.centery = HEIGHT/2
        #     self.rect.right = 0
        #
        # if self.rect.right < 0:
        #     self.speedy = 5
        #     self.speedx = 0
        #     self.rect.centery = HEIGHT / 2
        #     self.rect.bottom =0
        #
        # if self.rect.bottom < 0:
        #     self.speedx = 5
        #     self.speedy = 0
        #     self.rect.centery = HEIGHT / 2
        #     self.rect.right = 0



        #basic screen wraps
        # if self.rect.left > WIDTH:
        #     self.rect.right=0
        # if self.rect.right < 0:
        #     self.rect.left=WIDTH
        # if self.rect.top > HEIGHT:
        #     self.rect.bottom=0
        # if self.rect.bottom < 0:
        #     # self.rect.top=HEIGHT




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
NPC_group = pg.sprite.Group()

#creat objects
player = NPC()


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
        if event.type == pg.KEYDOWN:
            if event.key == pg.k_LEFT:
                player.speedx = -5
            if event.key == pg.k_RIGHT:
                player.speedx = 5
            if event.key == pg.k_UP:
                player.speedy = -5
            if event.key == pg.k_DOWN:
                player.speedy = 5



    #basic grid movment
    # for event in pg.event.get():
    #     if event.type == pg.KEYDOWN:
    #         if event.type == pg.K_DOWN or event.type == pg.K_s:
    #             player.rect.y -= 50
    #
    #         if event.type == pg.K_RIGHT or event.type == pg.K_d:
    #             player.rect.x += 50
    #
    #         if event.type == pg.K_UP or event.type == pg.K_w:
    #             player.rect.y += 50
    #
    #         if event.type == pg.K_LEFT or event.type == pg.K_a:
    #             player.rect.x -= 50



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