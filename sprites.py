import pygame as pg
from settings import *
from tilemap import *
vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.allSprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        #spawn player rectangle
        self.rect = self.image.get_rect()
        #spawn hitbox rectangle
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect_center = self.rect.center
        #create velocity variable
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * tileSize
        #variable that holds player rotation 
        self.rot = 0
       
       #begin video at 4:13 - adding vel to getKeys and other functions

    def getKeys(self):
        self.rot_speed = 0
        self.vel = vec(0, 0)
        #variable that shows which key is pressed:
        keys = pg.key.get_pressed()
        #if key is pressed add/subtract player speed to velocity
        #this moves the player
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rot_speed = PLAYER_ROT_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rot_speed  = -PLAYER_ROT_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            #move in the x direction at player speed and 0 speed in the y direction
                #rotate by the opposite of self.rotation amount
            self.vel = vec(PLAYER_SPEED, 0).rotate(-self.rot)
        if keys[pg.K_DOWN] or keys[pg.K_s]:
             #move backwards in the x direction at half player speed and 0 speed in the y direction
                #rotate by the opposite self.rotation amount
            self.vel = vec(-PLAYER_SPEED / 2, 0).rotate(-self.rot)
        
    
    def wallCollision(self, direction):
        if direction == 'x':
            #checks to see if sprite collides with wall object
            #use result of collide_hit_rect instead of player rect
            hits = pg.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits:
                #if player sprite was moving to the right:
                if self.vel.x > 0:
                    #x coord = position of thing hit - center of hit rect
                    self.pos.x = hits[0].rect.left - self.hit_rect.width / 2
                #if player sprite was moving to the left:
                if self.vel.x < 0:
                    #x coord = position of thing hit + center of hit rect
                    self.pos.x = hits[0].rect.right + self.hit_rect.width / 2
                self.vel.x = 0
                self.hit_rect.centerx = self.pos.x
        if direction == 'y':
            #checks to see if sprite collides with wall object
            hits = pg.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits:
                #if player sprite was moving up:
                if self.vel.y > 0:
                    #y coord = position of thing hit - center of hit rect
                    self.pos.y = hits[0].rect.top - self.hit_rect.height / 2
                #if player sprite was moving down:
                if self.vel.y < 0:
                    #x coord = position of thing hit + center of hit rect
                    self.pos.y = hits[0].rect.bottom + self.hit_rect.height / 2
                self.vel.y = 0
                self.hit_rect.centery = self.pos.y

    def update(self):
        self.getKeys()
        #update rotation
        #%360 restricts remainder angle to whole #'s between 1 and 360
        self.rot = (self.rot + self.rot_speed * self.game.dt) % 360 
        #rotate sprite image by self.rot
        self.image = pg.transform.rotate(self.game.player_img, self.rot)
        #get new rectangle
        self.rect = self.image.get_rect()
        #put center of rectangle as self.pos variable:
        self.rect.center = self.pos
        #add velocity * game time to the player's position
        self.pos += self.vel * self.game.dt
        #set center of hit rect to player x position
        self.hit_rect.centerx = self.pos.x
        self.wallCollision('x')
        #set center of hit rect to player y position
        self.hit_rect.centery = self.pos.y
        self.wallCollision('y')
        self.rect.center = self.hit_rect.center
       

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