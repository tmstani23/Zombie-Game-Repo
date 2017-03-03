import pygame as pg
from settings import *
from tilemap import *
vec = pg.math.Vector2


def wallCollision(sprite, group, direction):
        if direction == 'x':
            #checks to see if sprite collides with wall object
            #use result of collide_hit_rect instead of player rect
            hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
            if hits:
                #if player sprite was moving to the right:
                if sprite.vel.x > 0:
                    #x coord = position of thing hit - center of hit rect
                    sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
                #if player sprite was moving to the left:
                if sprite.vel.x < 0:
                    #x coord = position of thing hit + center of hit rect
                    sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
                sprite.vel.x = 0
                sprite.hit_rect.centerx = sprite.pos.x
        if direction == 'y':
            #checks to see if sprite collides with wall object
            hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
            if hits:
                #if player sprite was moving up:
                if sprite.vel.y > 0:
                    #y coord = position of thing hit - center of hit rect
                    sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
                #if player sprite was moving down:
                if sprite.vel.y < 0:
                    #x coord = position of thing hit + center of hit rect
                    sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
                sprite.vel.y = 0
                sprite.hit_rect.centery = sprite.pos.y

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
        wallCollision(self, self.game.walls, 'x')
        #set center of hit rect to player y position
        self.hit_rect.centery = self.pos.y
        wallCollision(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center
       
class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        #create variable that holds all mob objects in a group
        self.groups = game.allSprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.mob_img
        self.rect = self.image.get_rect()
        self.hit_rect = MOB_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.pos = vec(x, y) * tileSize
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.rect.center = self.pos
        self.rot = 0

    def update(self):
        #save vector between mob and player and find
            #angle between that vector and straight x vector
        self.rot = (self.game.player.pos - self.pos).angle_to(vec(1, 0))
        #rotate the mob image by the rotation vector
        self.image = pg.transform.rotate(self.game.mob_img, self.rot)
        #get new mob rectangle
        self.rect = self.image.get_rect()
        #set center of rectangle to mob position
        self.rect.center = self.pos
        #acceleration variable based on mob speed and rotated to face player
        self.acc = vec(MOB_SPEED, 0).rotate(-self.rot)
        self.acc += self.vel * -1
        self.vel += self.acc * self.game.dt
        #position based on motion equation and game time
        self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2
        self.hit_rect.centerx = self.pos.x
        wallCollision(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        wallCollision(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        #create variable that holds all wall objects in a group
        self.groups = game.allSprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * tileSize
        self.rect.y = y * tileSize