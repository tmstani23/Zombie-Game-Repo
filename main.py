# Silverhawk rpg game:
import pygame as pg
import random
import os
import sys
#import all variables from settings.py file
    #so appending isn't necessary
from settings import *
#import all from sprites.py file
from sprites import *

class Game:
    def __init__(self):
        #Initialize pygame and create window
        pg.init()
        #initialize sound mixer
        pg.mixer.init()
        #create screen variable that initializes the display
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption(title)
        #variable that holds pygame clock method
        self.clock = pg.time.Clock()
        #sets how long key should repeat when pressed
            #(how long to wait before repeat, length of repeat in ms)
        pg.key.set_repeat(250, 100)
        #create a variable that holds the path of the game files
        self.dir = os.path.dirname(__file__)
        #print current working directory to console
        print(os.getcwd())
        
    
    def newGame(self):
        #start a new Game
        self.allSprites = pg.sprite.Group()
        #draw the player at tile 10 by 10
        self.player = Player(self, 10, 10)
        self.walls = pg.sprite.Group()
        #spawn a wall from 10 to 20 tiles
        for x in range(10, 20):
            #create the wall at x of 10 to 20 and y of 5 tiles
            Wall(self, x, 5) 

    def run(self):
        #Game Loop
        self.playing = True
        while self.playing:
            #keep running at the right speed
            self.dt = self.clock.tick(fps) / 1000
            self.events()
            self.update()
            self.draw()
    
    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        #Update game screen
        self.allSprites.update()
    
    def events(self):
        #Process input (events)
        for event in pg.event.get():
            #Check for closing the window
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=+1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=+1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)


    def drawGrid(self):
        #draw vertical lines to the screen
        #draw lines from 0 to width in increments of tilesize
        for x in range(0, width, tileSize):
            #use pygame line method draw to screen in light grey
                #draw from coordinates x,0 to x,height 
            pg.draw.line(self.screen, lightGrey, (x, 0), (x, height))
        #draw horizontal lines
        for y in range(0, height, tileSize):
            pg.draw.line(self.screen, lightGrey, (0, y), (width, y))
    
    def draw(self):
        #Draw / render
        self.screen.fill(bgColor)
        #Draw grid
        self.drawGrid()
        #Draw sprites
        self.allSprites.draw(self.screen)
        #After drawing always flip the display
        pg.display.flip()
    
    def showStartScreen(self):
        #game start screen
        pass

    def showOverScreen(self):
        #show game over screen
        pass



    
    
    
g = Game()
g.showStartScreen()


while True:
    g.newGame()
    g.run()
    g.showOverScreen
    

