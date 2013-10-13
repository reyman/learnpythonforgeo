# -*- coding: utf-8 -*-

mapRogue = ['~~~~~~~~~~',
             '~~~~.....Y',
             'YYYYY+YYYY',
             'YYYY....YY']

class Tile(object):
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

tilesObject = {".": {"name": 'floor', "obj": Tile, "bgcolor": (233, 207, 177), "block": False},
               "Y": {"name": 'forest', "obj": Tile, "bgcolor": (25, 150, 64), "block": True},
               "~": {"name": 'water', "obj": Tile, "bgcolor": (10, 21, 35), "block": False},
               "+": {"name": 'doors', "obj": Door, "bgcolor": (10, 10, 25), "block": False}}

def load(mymap):
    tileMap = []
    x, y = (0,0)
    for line in mymap:
        tileLine = []
        for value in line:
            try:
                tile = tilesObject[value]
            except KeyError:
                return "Error on key"
            if tile["obj"].__name__ ==  "Door":
                obj = tile["obj"](name=tile["name"], position=(x, y), char=value, blocked=tile["block"],bgcolor=tile["bgcolor"], key="42isTheKey", open=False)
            else:
                obj = tile["obj"](name=tile["name"], position=(x, y), char=value, blocked=tile["block"],bgcolor=tile["bgcolor"])

            x += 1
            tileLine.append(obj)
        x = 0
        y += 1
        tileMap.append(tileLine)
    return tileMap


for line in load(mapRogue):
    for obj in line:
        print obj , "\n"

#
#class Tile(object):
#    #a tile of the map and its properties
#    def __init__(self, name, char, position, blocked, color=(255, 255, 255), bgcolor=(0, 0, 0)):
#        self.name = name
#        self.blocked = blocked
#        self.char = char
#        self.color = color
#        self.bgcolor = bgcolor
#        self.position = position
#        #store item dropped by user or monster
#        self.objects = []
#        self.in_FOV = False
#
#class Door(Tile):
#    def __init__(self,  name, char, position, blocked, bgcolor, key,color=(255, 255, 255), open=False ):
#        Tile.__init__( self,name, char, position, blocked, color, bgcolor)
#        self.state = open
#        self.key = key
#
#    def opening(self, key):
#        if self.key == key:
#            self.state = True
#
#tilesObject = {".": {"name": 'floor', "obj": Tile, "bgcolor": (233, 207, 177), "block": False},
#               "Y": {"name": 'forest', "obj": Tile, "bgcolor": (25, 150, 64), "block": True},
#               "~": {"name": 'water', "obj": Tile, "bgcolor": (10, 21, 35), "block": False},
#               "+": {"name": 'doors', "obj": Door, "bgcolor": (10, 10, 25), "block": False}}
#import types
#def load(mymap):
#    tileMap = []
#    x, y = (0,0)
#    for line in mymap:
#        tileLine = []
#        for value in line:
#            try:
#                tile = tilesObject[value]
#            except KeyError:
#                return "Error on key"
#            if tile["obj"].__name__ ==  "Door":
#                obj = tile["obj"](name=tile["name"], position=(x, y), char=value, blocked=tile["block"],bgcolor=tile["bgcolor"], key="42isTheKey", open=False)
#            else:
#                obj = tile["obj"](name=tile["name"], position=(x, y), char=value, blocked=tile["block"],bgcolor=tile["bgcolor"])
#
#            x += 1
#            tileLine.append(obj)
#        x = 0
#        y += 1
#        tileMap.append(tileLine)
#    return tileMap
#
#
#for line in load(mapRogue):
#    for obj in line:
#        print obj , "\n"
#
#
#
	

		
