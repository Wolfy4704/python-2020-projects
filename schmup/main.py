import pygame as pg
import random as r
import math
from os import *


# Game object classes


class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH / 2)
        self.rect.bottom = (HEIGHT - (HEIGHT * .05))
        self.speedx = 0

    def update(self):
        self.rect.x += self.speedx



class NPC(pg.sprite.Sprite):
    def __init__(self):
        super(NPC, self).__init__()
        self.image = pg.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH / 2)
        self.rect.top = (0)
        self.speedy = 0

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx


class Bullet(pg.sprite.Sprite):
    def __init__(self,x,y):
        self.image = pg.Surface((5,10))

    def shoot(self):
        b = Bullet(self.rect.centerx,self.rect.top-1)
    def updates(self):





# Game Constants

HEIGHT = 900
WIDTH = 600
FPS = 60

# Colors (R,G,B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

title = "Shmup"



# initialize pygame and create window

pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(title)
clock = pg.time.Clock()


# load imgs




# create Sprite groups

all_sprites = pg.sprite.Group()
players_group = pg.sprite.Group()
npc_group = pg.sprite.Group()


# create Game Objects

player = Player()
npc = NPC()
for i in range(20):
    npc = NPC()
    npc_group.add(npc)

bullet = Bullet(WIDTH/2,HEIGHT/2)


# add objects to sprite groups

players_group.add(player)
npc_group.add(npc)

for i in players_group:
    all_sprites.add(i)
for i in npc_group:
    all_sprites.add(i)



# Game Loop

# game update Variables

playing = True


while playing:
    # timing

    clock.tick(FPS)


    # collecting Input


    # Quiting the game when we hit the x
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                playing = False
        if event.type == pg.QUIT:
            playing = False


    # Updates

    all_sprites.update()

    # Render


    screen.fill(BLACK)
    all_sprites.draw(screen)

    pg.display.flip()


pg.quit()
