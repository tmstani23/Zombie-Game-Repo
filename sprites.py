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
        self.x = x
        self.y = y

    #dx and dy are default x and y arguments that can be passed in
    def move(self, dx = 0, dy = 0):
        #if not colliding with wall allow player movement
        if not self.wallCollision(dx, dy):
            self.x += dx
            self.y += dy
    
    def wallCollision(self, dx = 0, dy = 0):
        #iterate through each wall in wall group
        for wall in self.game.walls:
            #check if wall x coord = player x plus xmove coord
                #and wall y = player y + ymove coord\
            #essentially, is space moving into = wall x and wall y?
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        #if not True
        return False 

    def update(self):
        self.rect.x = self.x * tileSize
        self.rect.y = self.y * tileSize

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