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



#Game options/settings
title = "Zombie Survival!"
WIDTH = 1024
HEIGHT = 640
fps = 60
bgColor = darkGrey

tileSize = 64
gridWidth = WIDTH / tileSize
gridHeight = HEIGHT / tileSize

#Player settings
PLAYER_SPEED = 300 
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'manBlue_gun.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
