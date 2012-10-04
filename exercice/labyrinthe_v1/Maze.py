# -*- coding: utf-8 -*-
import random
import constants as c


class Maze():

 def __init__(self,sizeX,sizeY):
  self.height = sizeY
  self.width = sizeX
  self.t_build = self.mazeBuilder([[c.cEmpty]*sizeX for x in xrange(sizeX)],self.height)
  self.t_world = self.mazePrinter(self.t_build)
 
 def getHeight(self):
  return self.height

 def getWidth(self):
  return self.width
 
 def getValueAtXY(self,x,y):
  return self.t_world[y][x]

 def setValueAtXY(self,value,x,y):
  self.t_world[y][x] = value

 def mazePrinter(self, t_world):
     sizeY = len(t_world) 
     sizeX = len(t_world[0])
     
     t_view = [[c.cEmpty]*((sizeX )*2 + 1) for x in xrange(((sizeY )*2)+ 1)] 
     
     for j in xrange(len(t_view)):
      t_view[len(t_view)-1][j] = c.cWall

     for i in xrange(len(t_view)):
      t_view[i] [len(t_view)-1]= c.cWall
     
     for i in xrange(sizeX):
        for j in xrange(sizeY):
         #XY POSITION = t_view(i * 2 + 1, j * 2 + 1)
            
         #add a wall
         
         t_view[j * 2][i * 2] = c.cWall

         #if NO edge connecting x,y and x-1,y add a wall
         if ((t_world[j][i] & c.cW) == 0):
          #xy start at bottom right (i * 2 +1) et (j *2 + 1)
          t_view[j * 2 + 1][i * 2 + 1 - 1] = c.cWall
          print "i : ", i, "j :", j, "value = ", t_world[j][i], "to : j = ", j * 2 + 1, "and i = ", i * 2 + 1 - 1
          

         #if NO edge connecting x,y and x,y-1 add a wall
         if ((t_world[j][i] & c.cN) == 0):
          t_view[j * 2 + 1 - 1][i * 2 + 1] = c.cWall
    			
     return t_view

 def choisiIndex(self, myCase, myOption):
     size = 0
     myIndex = size

     if (myOption == "backtrack"):
      size = len(myCase)
      myIndex = size - 1
     elif (myOption == "random"):
      size = len(myCase) - 1
      myIndex = random.randint(0, size)
     return myIndex


#-------------------------------------------------------------------------------------------------------------------------------------
# Copyright jamisbuck
# Algorithm transform for Python : Sebastien Rey
# url : http://weblog.jamisbuck.org/2011/1/27/maze-generation-growing-tree-algorithm#
#
# 1. Given a maze with n x m cells, initialize an empty grid to be n*2+1 x m*2+1.
# 2. Mark the entire last row and the last column of the grid as "wall" (e.g. column n*2 and row m*2).
# 3. For each cell x,y in the original grid:
#
#  3a. Add a wall in the grid at x*2,y*2.
#  3b. If there is NO edge connecting x,y and x-1,y, add a wall to x*2-1,y*2.
#  3c. If there is NO edge connecting x,y and x,y-1, add a wall to x*2,y*2-1
#
# The algorithm works by treating each node in the original graph as a 2x2 block in the grid,
# with the node itself at the bottom-right of the 2x2 block, so you adapt x,y to bottom right coord before add wall. You then tile the grid with those 2x2 blocks,
# filling in the last row/column with walls to finish it off.
#
# In my implementations, I treat each cell as a bitfield, where each bit represents a directed edge to a neighbor.
# Because I'm doing a directed graph, each node needs it's own edge pointing to a neighbor.
# Thus, if A and B are connected, there are two edges involved: A would have a bit set pointing in B's direction, and B would have a bit set (in the opposite direction) toward A.
# Without setting the opposite bit on the neighbor, you'll wind up with one-way passages; you could go fro A to B, but not from B to A.
#
# Naturally, there are many different ways to represent a graph. I'm using a two-dimensional array of bitfields, with each bit representing a directed edge to a neighbor.
# You can use whichever technique you are familiar with, but I think the 2d array works really well and efficiently for grid-style mazes.
#
#-------------------------------------------------------------------------------------------------------------------------------------
 
 def mazeBuilder(self, t_world, i_size): 
     t_direction = ['N','S','E','W']
     t_emptyCase = []
     
     cellX = random.randint(0,len(t_world)-1)
     cellY = random.randint(0,len(t_world)-1)
     t_emptyCase.append((cellX,cellY))
      
     while True:
      
      index = self.choisiIndex(t_emptyCase, "random" ) 
      cell = t_emptyCase[index]
       
      random_direction = t_direction[:]
      random.shuffle(random_direction)
       
      for myDirection in t_direction:
       valueDirection = 0
       
       if (myDirection == "E"):
        nx = cell[0] + 1
        valueDirection = c.cE
       elif (myDirection == "W"):
        nx = cell[0] - 1
        valueDirection = c.cW
       else:
        nx = cell[0]
            
       if (myDirection == "S"):
        ny = cell[1] + 1
        valueDirection = c.cS
       elif (myDirection == "N"):
        ny = cell[1] - 1
        valueDirection = c.cN
       else:
        ny = cell[1]
       
       valueDirection2 = 0
       
       if (nx >= 0 and ny >= 0 and nx < i_size and ny < i_size):
        if (t_world[ny][nx] == c.cEmpty):
          t_world[cell[1]][cell[0]] = (t_world[cell[1]][cell[0]] | valueDirection)  
          
          if (myDirection == "E"):
           valueDirection2 = c.cW
          elif (myDirection == "W"):
           valueDirection2 = c.cE
        
          if (myDirection == "S"):
           valueDirection2 = c.cN
          elif (myDirection == "N"):
           valueDirection2 = c.cS
          
          t_world[ny][nx] = (t_world[ny][nx] | valueDirection2)      
         
          t_emptyCase.append((nx,ny))
          
          index = -255
          break
     
      if (index != -255):
       t_emptyCase.pop(index)
           
      if (len(t_emptyCase) == 0):
       break

     print t_world
     
     return t_world 