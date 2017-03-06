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


#HUD functions
def draw_player_health(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 20
    fill = pct * BAR_LENGTH
    outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
    if pct > 0.6:
        col = GREEN
    elif pct > 0.3:
        col = YELLOW
    else:
        col = RED
    pg.draw.rect(surf, col, fill_rect)
    pg.draw.rect(surf, WHITE, outline_rect, 2)

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
        mapFolder = path.join(gameFolder, 'map')
        self.map = TiledMap(path.join(mapFolder, 'level1.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pg.image.load(path.join(imgFolder, PLAYER_IMG)).convert_alpha()
        self.bullet_img = pg.image.load(path.join(imgFolder, BULLET_IMG)).convert_alpha()
        self.mob_img = pg.image.load(path.join(imgFolder, MOB_IMG)).convert_alpha()
        self.wall_img = pg.image.load(path.join(imgFolder, WALL_IMG)).convert_alpha()
        self.wall_img = pg.transform.scale(self.wall_img, (tileSize, tileSize))

    
    def newGame(self):
        #start a new Game
        self.allSprites = pg.sprite.Group()
        
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        #enumerate row index position and tile data from list mapdata
        '''for row, tiles in enumerate(self.map.data):
            #enumerate index  of each column and data of each tile
            #this provides x and y position of each tile within mapData list
            for col, tile in enumerate(tiles):
                #if the tile contains a 1
                if tile == '1':
                    #spawn a wall at the position
                    Wall(self, col, row) 
                if tile == 'M':
                    #spawn a mob at the position
                    Mob(self, col, row) 
                if tile == 'P':
                    #draw the player at tile 10 by 10
                    self.player = Player(self, col, row)'''
        #spawn player:
        self.player = Player(self, 5, 5)
        
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
        #Mob hits player:
        hits = pg.sprite.spritecollide(self.player, self.mobs, False, collide_hit_rect)
        for hit in hits:
            #subtract mob damage from player health
            self.player.health -= MOB_DAMAGE
            #move mob back a bit
            hit.vel = vec(0, 0)
            #game over if player health reaches 0
            if self.player.health <= 0:
                self.playing = False
            if hits:
                #player is knocked back a bit and continues facing same direction
                self.player.pos += vec(MOB_KNOCKBACK, 0).rotate(-hits[0].rot)

        #Bullets hit mobs
        #false/true - mobs dont disappear bullets do when hit
        hits = pg.sprite.groupcollide(self.mobs, self.bullets, False, True)
        for hit in hits:
            hit.health -= BULLET_DAMAGE
            hit.vel = vec(0, 0)
    
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
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        #Draw / render
        #self.screen.fill(BGCOLOR)
        #draw map to screen:
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        #Draw grid
        #self.drawGrid()
        #Draw sprites
        for sprite in self.allSprites:
            #if sprite is a mob:
            if isinstance(sprite, Mob):
                sprite.draw_health()        
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        #After drawing always flip the display
        #pg.draw.rect(self.screen, WHITE, self.player.hit_rect, 2)
        #Draw HUD functions:
        draw_player_health(self.screen, 10, 10, self.player.health / PLAYER_HEALTH)
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
    

