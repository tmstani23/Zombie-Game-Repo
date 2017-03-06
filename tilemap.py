import pygame as pg
from settings import *
import pytmx


def collide_hit_rect(one, two):
    #return rect one instead of rect two
    #in this case return hit_rect instead of player rect
    return one.hit_rect.colliderect(two.rect)

class Map:
    def __init__(self, filename):
        self.data = []
        #open game folder path and link to map.txt in read mode
        with open(filename, 'rt') as f:
            #for each line in map.txt append line to mapData list
            for line in f:
                self.data.append(line.strip())
    
        #variable that holds how many tiles wide the map is:
        self.tilewidth = len(self.data[0])
        #variable that holds how many tiles high the map is:
        self.tileheight = len(self.data)
        #variables that hold pixel width and height of the map
        self.width = self.tilewidth * tileSize
        self.height = self.tileheight * tileSize

class TiledMap:
    def __init__(self, filename):
        #pixelalpha allows tile transparencies to be transferred
        tm = pytmx.load_pygame(filename, pixelalpha = True)
        #tmwidth is how many tiles across and tm.tilewidth is the pxel width of each tile
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    def render(self, surface):
        #find tile image by data number tiled assigns to each tile(gid)
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            #if it's a tiled tile layer:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        #show tile at correct location on surface
                        surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight))
    
    def make_map(self):
        #create surface that's however big the map is:
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface



class Camera:
    def __init__(self, width, height):
        #create variable that is a rectangle that represents camera view
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        #return entity(sprite)
        #and generate a new rect that is shifted by offset coord amount
        return entity.rect.move(self.camera.topleft)  

    def apply_rect(self, rect):
        #return rect that is moved by camera offset
        return rect.move(self.camera.topleft) 

    def update(self, target):
        x = -target.rect.centerx + int(WIDTH / 2)
        y = -target.rect.centery + int(HEIGHT / 2)
        

        #limit scrolling to map size
        x = min(0, x) #left
        y = min(0, y) #top 
        x = max(-(self.width - WIDTH), x) #right
        y = max(-(self.height - HEIGHT), y) #bottom
        self.camera = pg.Rect(x, y, self.width, self.height) 