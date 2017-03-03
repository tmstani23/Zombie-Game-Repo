import pygame as pg

#Define colors
WHITE = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
lightGrey = (100, 100, 100)
darkGrey = (40, 40, 40)
yellow = (255, 255, 0)
BROWN = (186, 55, 5)



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
PLAYER_SPEED = 300 
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'manBlue_gun.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)

#Mob settings
MOB_IMG = 'zombie1_hold.png'
MOB_SPEED = 150
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
