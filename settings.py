import pygame as pg
vec = pg.math.Vector2

#Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHTGREY = (100, 100, 100)
DARKGREY = (40, 40, 40)
YELLOW = (255, 255, 0)
BROWN = (186, 55, 5)
CYAN = (0, 255, 255)



#Game options/settings
title = "Zombie Survival!"
WIDTH = 1024
HEIGHT = 640
fps = 60
BGCOLOR = BROWN

tileSize = 64
gridWidth = WIDTH / tileSize
gridHeight = HEIGHT / tileSize

WALL_IMG = 'wallTile_367.png'

#Player settings
PLAYER_HEALTH = 100
PLAYER_SPEED = 300 
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'manBlue_gun.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(30, 10)

#Gun settings
BULLET_IMG = 'bullet.png'
BULLET_SPEED = 500
BULLET_LIFETIME = 1000
BULLET_RATE = 150
KICKBACK = 200
GUN_SPREAD = 5
BULLET_DAMAGE = 10

#Mob settings
MOB_IMG = 'zombie1_hold.png'
MOB_SPEED = 150
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20
