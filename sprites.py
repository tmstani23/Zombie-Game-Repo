import pygame as pg
from settings import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.allSprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.playerImg
        self.rect = self.image.get_rect()
        #create velocity variable
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * tileSize
       
       #begin video at 4:13 - adding vel to getKeys and other functions

    def getKeys(self):
        self.vel = vec(0, 0)
        #variable that shows which key is pressed:
        keys = pg.key.get_pressed()
        #if key is pressed add/subtract player speed to velocity
        #this moves the player
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vel.x = -playerSpeed
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vel.x  = +playerSpeed
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel.y  = -playerSpeed
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel.y  = +playerSpeed
        #diagonal move speed calculation adjustment:
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071
    
    def wallCollision(self, direction):
        if direction == 'x':
            #checks to see if sprite collides with wall object
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                #if player sprite was moving to the right:
                if self.vel.x > 0:
                    #x coord = position of thing hit - player width
                    self.pos.x = hits[0].rect.left - self.rect.width
                #if player sprite was moving to the left:
                if self.vel.x < 0:
                    #x coord = position of thing hit 
                    self.pos.x = hits[0].rect.right 
                self.vel.x = 0
                self.rect.x = self.pos.x
        if direction == 'y':
            #checks to see if sprite collides with wall object
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                #if player sprite was moving up:
                if self.vel.y > 0:
                    #y coord = position of thing hit - player height
                    self.pos.y = hits[0].rect.top - self.rect.height
                #if player sprite was moving down:
                if self.vel.y < 0:
                    #x coord = position of thing hit 
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0
                self.rect.y = self.pos.y

    def update(self):
        self.getKeys()
        #add velocity * game time to the player's position
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        self.wallCollision('x')
        self.rect.y = self.pos.y
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