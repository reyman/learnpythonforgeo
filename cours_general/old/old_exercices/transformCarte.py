# -*- coding: utf-8 -*-
def drawMap(world):
	mappedWorld = ""
	for line in world:
		for value in line:
			if value == 1:
				mappedWorld += "#"
			else:
				mappedWorld += "."
		mappedWorld += '\n'
	return mappedWorld
