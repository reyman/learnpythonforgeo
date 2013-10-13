# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 14:52:20 2012

@author: srey
"""
from random import randint
import os
import constants as c
import drawRogue as draw
import sys, pygame
from constants import *
from pygame.locals import *
from fontrenderer import *

mapLoaded = ['~~~~~~~~~~~~~~~~~~~~~~~~~~~YYYYYYYYYYYYYYY',
             '~~~~~~~~~~~~~~~~~~~~~~~~~~~...YYYYYYYYYYYY',
             '~~~~~~~~~~~~~~~~~~~~~~~~~~.......YYYYYYYYY',
             '~~~~~~~~~~~~~~~~~..~~~~~~~~....Y..YYYYYYYY',
             '~~~~~~~~~~~~~~~~......~~~~....YYY.YYYYYYYY',
             '~~~~~~~~~~~~~~~......||||.....YY...YYYYYYY',
             '~~~~~~~~~~~~~~~~....~~~~..........YYYYYYYY',
             '~~~~~~~~~~~~~~~~~..~~~~~~......YY....YYYYY',
             '~~~~~~~~~~~~~~~~~~~~~~~~.....YYYYYY..YYYYY',
             '~~~~~~~~~~~~~~~~~~~~~~~~~~...YYYY....YYYYY',
             '~~~~~~~~~~~~~~~~~~~~~~~~....YYYYYY..YYYYYY',
             '~~~~~~~~~~~~~~~~~~~~~~~....YYYYYY....YYYYY',
             '~~~~~~~~~~~~~~~~~~~~.....YYYYYY....YYYYYYY',
             '~~~~~~~~~~~~~~~~~~.......YYYYYY..YYYYYYYYY',
             '~~~~~~~~~~~~~~~~~..YYY...YYYYY....YYYYYYYY',
             '~~~~~~~.~~~~~~~~~.YYYYYY.........YYYYYYYYY',
             '~~~~~~...~~~~~~~~..YYYY....YYYYYYYYYYYYYYY',
             '~~~~~......~~~~~~~...Y.....YYYYYYYYYYYYYYY',
             '~~~~~~........YYY....YY........YYYYYYYYYYY',
             '~~~~~........YYYY..YYYY...........YYYYYYYY',
             '~~~~~~~....YYYYY...YY.....YYYY....YYYYYYYY',
             '~~~~~~~~~..YYYY..YYYYYY...YYYYY.....YYYYYY',
             '~~~~~~~~~~..YYY...YYYYY...YYYYYY...YYYYYYY',
             '~~~~~~~~~~...Y..YYYYYYY...YYYYY......YYYYY',
             '~~~~~~~~~~..YY...YYYYY......YYY..Y...YYYYY',
             '~~~~~~~~~YY.....YYYYY............YY...YYYY',
             '~~~~~~~YYYYYYYYYYYYY.........YYYYYY..YYYYY',
             '~~~~YYYYYYYYYYYYYYYYYY......YYYYY.....YYYY',
             '~~YYYYYYYYYYYYYYYYYY....YYYYYYYYYY......YY',
             'YYYYYYYYYYYYYYYYYYY.....YYYYYYYY......YYYY',
             'YYYYYYYYYYYYYYYY.......YYYYYYYYYYY...YYYYY',
             'YYYYYYYYYYYYYYY......YYYYYYYYYYY.....YYYYY',
             'YYYYYYYYYYYYYYYYYY...YYYYYYYYYY..YYYYYYYYY',
             'YYYYYYYYYYYYYYYYYYYY...YYYYYYY....YYYYYYYY',
             'YYYYYYYYYYYYYYYYYYY....YYYYY....YYYYYYYYYY',
             'YYYYYYYYYYYYYYYYYY.....YYY...YYYYYYYYYYYYY',
             'YYYYYYYYYYYYYYYYYYY.........YYYYYYYYYYYYYY',
             'YYYYYYYYYYYYYYYYYYYYYYYY+YYYYYYYYYYYYYYYYY',
             'YYYYYYYYYYYYYYYYYYYY.....YYYYYYYYYYYYYYYYY',
             'YYYYYYYYYYYYYYYYYYY........YYYYYYYYYYYYYYY',
             'YYYYYYYYYYYYYYYYYYY..YYYYYYYYYYYYYYYYYYYYY',
             'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY']

#def draw_msg_area(self, area, msg):
#          """
#          Draws the message area above the game area.
#          You must call update_screen to see the results!
#
#          Keyword arguments:
#          area -- The map from which to obtain dimensions
#          msg -- Message object from which to obtain history
#          """
#          font = pygame.font.Font(self.font_type, self.font_size - 4)
#          clear_surface = pygame.Surface((TILE_SIZE_X*COLUMNS, TILE_SIZE_Y + 1))  # Create a blank black surface
#          clear_surface.fill((0, 0, 0))
#          history = msg.get_history()
#          for i in range(min(len(history), 5)):
#                  sign = font.render(history[i], 1, (250, 250, 250), (0, 0, 0))
#                  pos = (0, i*TILE_SIZE_Y)
#                  self.background.blit(clear_surface, pos)                    # Erase old
#                  self.background.blit(sign, pos)

class Case(object):
    #a tile of the map and its properties
    def __init__(self, name, char, position, blocked, color=(255, 255, 255), bgcolor=(0, 0, 0), door=None):
        self.name = name
        self.blocked = blocked
        self.char = char
        self.color = color
        self.bgcolor = bgcolor
        self.door = door
        self.position = position
        #store item dropped by user or monster
        self.objects = []
        self.in_FOV = False

# Other composition to do here
class Door(object):
    def __init__(self, key, open=False):
        self.state = open
        self.key = key

    def opening(self, key):
        if self.key == key:
            self.state = True


tilesObject = {".": {"name": 'floor', "obj": Case, "bgcolor": (233, 207, 177), "block": False},
               "Y": {"name": 'forest', "obj": Case, "bgcolor": (25, 150, 64), "block": True},
               "|": {"name": 'pont', "obj": Case, "bgcolor": (190, 150, 35), "block": False},
               "~": {"name": 'water', "obj": Case, "bgcolor": (10, 21, 35), "block": False},
               "+": {"name": 'doors', "obj": Case, "bgcolor": (10, 10, 25), "block": False}}

# Storing moving object into list
# Storing Tile into 2D list
# Tile contain list of item
class MapObject(object):
    def __init__(self, map):
        self.size = len(map)
        self.tilemap = self.load(map)
        #print(type(self.tilemap))
        self.objectmap = []
        self.movingObject = []

    def get_tile(self,x,y):
        return self.tilemap[y][x]

    def load(self, mymap):
        tileMap = []
        x, y = (0,0)
        for line in mymap:
            tileLine = []
            for value in line:

                try:
                    tile = tilesObject[value]
                except KeyError:
                    return "Error on key"
                    # problem due to DOOR and polymorphism ... :/
                #print tile["bgcolor"]
                obj = tile["obj"](name=tile["name"], position=(x, y), char=value, blocked=tile["block"],
                                  bgcolor=tile["bgcolor"])
                x += 1
                tileLine.append(obj)
            x = 0
            y += 1
            tileMap.append(tileLine)
        return tileMap

    def moveObject(self, dx, dy):
        for objToMove in self.movingObject:
            state = self.get_tile(objToMove.x + dx,objToMove.y + dy).blocked
            char = self.get_tile(objToMove.x + dx ,objToMove.y + dy).char
            if state == False :
                objToMove.move(dx, dy)

    def createTileSurface(self, tile):
        s = pygame.Surface((TILESIZE, TILESIZE), pygame.HWSURFACE, 32)
        sText = FontRenderer().render(tile.char, tile.color)
        rectText = sText.get_rect()
        rectText.center = s.get_rect().center
        s.fill((tile.bgcolor))
        s.blit(sText, rectText)
        return s

    def draw_maze(self, screen):
        for row in xrange(self.size):
            for column in xrange(self.size):
                tile = self.tilemap[row][column]
                absolute_pos = _map2absolute_position(tile.position)
                surfTile = self.createTileSurface(tile)
                screen.blit(surfTile, absolute_pos)

    def draw_personnages(self, screen):
        for personnage in self.movingObject:
            s = pygame.Surface((TILESIZE, TILESIZE), pygame.HWSURFACE, 32)
            sText = FontRenderer().render(personnage.char, personnage.color)
            rectText = sText.get_rect()
            rectText.center = s.get_rect().center
            s.blit(sText, rectText)
            screen.blit(s, _map2absolute_position((personnage.x,personnage.y)))


class Object(object):
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        print self.x , "/ ", self.y


import random


def variant(color, neg=-5, pos=5):
    r = []
    for c in color:
        r.append(max(0, c + random.randrange(neg, pos)))
    return tuple(r)


def _map2absolute_position(map_position):
    x, y = map_position
    ox, oy =  player.x, player.y
    return (x - ox + MAPWIDTH / 2) * TILESIZE, (y - oy + MAPHEIGHT / 2) * TILESIZE


def get_cell_rect(row, col):
    off_x = base_offset + col * square_pixels
    off_y = base_offset + row * square_pixels
    return pygame.Rect(off_x + 4, off_y + 4, square_pixels - 6, square_pixels - 6)

# y, x
player = Object(23,39, "@", (255, 255, 255))

def main():
    pygame.init()


    sceneArea = pygame.Surface(SCENEAREA, pygame.HWSURFACE, 32)
    messageArea = pygame.Surface(MESSAGEAREA, pygame.HWSURFACE, 32)

    world = MapObject(mapLoaded)
    world.movingObject = [player]

    #size = width, height = (2*base_offset)+(world.size*square_pixels), (2*base_offset)+(world.size*square_pixels)

    flags = pygame.HWSURFACE
    screen = pygame.display.set_mode(RESOLUTION, flags, 32)

    #screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    pygame.mouse.set_visible(1)

    screen.fill(c.cBlack)

    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                key = event.key
                if key == K_UP:
                    world.moveObject(0, -1)
                elif key == K_RIGHT:
                    world.moveObject(1, 0)
                elif key == K_DOWN:
                    world.moveObject(0, 1)
                elif key == K_LEFT:
                    world.moveObject(-1, 0)
            elif event.type == QUIT:
                return


        world.draw_maze(sceneArea)
        world.draw_personnages(sceneArea)

        #draw the outer border
        #border_rect = (base_offset, base_offset, (world.size*square_pixels), (world.size*square_pixels))
        #pygame.draw.rect(screen, c.cGrey, border_rect, 2)

        screen.blit(sceneArea, (0, 0))

        #pygame.display.flip()
        pygame.display.update()
        clock.tick(20)


clear = lambda: os.system('clear')

if __name__ == "__main__":
    main()
    pygame.quit()



        
	

		
