# Silverhawk rpg game:
import pygame as pg
from tilemap import *
from os import path
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
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(title)
        #variable that holds pygame clock method
        self.clock = pg.time.Clock()
        #sets how long key should repeat when pressed
            #(how long to wait before repeat, length of repeat in ms)
        pg.key.set_repeat(250, 100)
        self.loadData()
        #print current working directory to console
        print(path.dirname(__file__))
    
    def loadData(self):
        #create a variable that holds the path of the game files
        gameFolder = path.dirname(__file__)
        imgFolder = path.join(gameFolder, 'img')
        self.map = Map(path.join(gameFolder, 'map4.txt'))
        self.playerImg = pg.image.load(path.join(imgFolder, PLAYER_IMG)).convert_alpha()
    
    def newGame(self):
        #start a new Game
        self.allSprites = pg.sprite.Group()
        
        self.walls = pg.sprite.Group()
        #enumerate row index position and tile data from list mapdata
        for row, tiles in enumerate(self.map.data):
            #enumerate index  of each column and data of each tile
            #this provides x and y position of each tile within mapData list
            for col, tile in enumerate(tiles):
                #if the tile contains a 1
                if tile == '1':
                    #spawn a wall at the position
                    Wall(self, col, row) 
                if tile == 'P':
                    #draw the player at tile 10 by 10
                    self.player = Player(self, col, row)
        #spawn camera:
        self.camera = Camera(self.map.width, self.map.height)


    def run(self):
        #Game Loop
        self.playing = True
        while self.playing:
            #keep running at the right speed
            #dt stands for delta t
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
        self.camera.update(self.player)
    def events(self):
        #Process input (events)
        for event in pg.event.get():
            #Check for closing the window
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

    def drawGrid(self):
        #draw vertical lines to the screen
        #draw lines from 0 to width in increments of tilesize
        for x in range(0, WIDTH, tileSize):
            #use pygame line method draw to screen in light grey
                #draw from coordinates x,0 to x,height 
            pg.draw.line(self.screen, lightGrey, (x, 0), (x, HEIGHT))
        #draw horizontal lines
        for y in range(0, HEIGHT, tileSize):
            pg.draw.line(self.screen, lightGrey, (0, y), (WIDTH, y))
    
    def draw(self):
        #Draw / render
        self.screen.fill(bgColor)
        #Draw grid
        self.drawGrid()
        #Draw sprites
        for sprite in self.allSprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
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
    

