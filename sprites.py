import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.allSprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((tileSize, tileSize))
        self.image.fill(yellow)
        self.rect = self.image.get_rect()
        #create velocity variables
        self.vx, self.vy = 0, 0
        self.x = x * tileSize
        self.y = y * tileSize

    def getKeys(self):
        self.vx, self.vy = 0, 0
        #variable that shows which key is pressed:
        keys = pg.key.get_pressed()
        #if key is pressed add/subtract player speed to velocity
        #this moves the player
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -playerSpeed
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = +playerSpeed
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = -playerSpeed
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = +playerSpeed
        #diagonal move speed calculation adjustment:
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071
    
    def wallCollision(self, direction):
        if direction == 'x':
            #checks to see if sprite collides with wall object
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                #if player sprite was moving to the right:
                if self.vx > 0:
                    #x coord = position of thing hit - player width
                    self.x = hits[0].rect.left - self.rect.width
                #if player sprite was moving to the left:
                if self.vx < 0:
                    #x coord = position of thing hit 
                    self.x = hits[0].rect.right 
                self.vx = 0
                self.rect.x = self.x
        if direction == 'y':
            #checks to see if sprite collides with wall object
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                #if player sprite was moving up:
                if self.vy > 0:
                    #y coord = position of thing hit - player height
                    self.y = hits[0].rect.top - self.rect.height
                #if player sprite was moving down:
                if self.vy < 0:
                    #x coord = position of thing hit 
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y

    
    
    def update(self):
        self.getKeys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.wallCollision('x')
        self.rect.y = self.y
        self.wallCollision('y')
       

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        #create variable that holds all wall objects in a group
        self.groups = game.allSprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((tileSize, tileSize))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * tileSize
        self.rect.y = y * tileSize