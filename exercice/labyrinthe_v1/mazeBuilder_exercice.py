# -*- coding: utf-8 -*-
import random
import constants as c
import drawMaze as draw
from Maze import Maze

def run(maze):
 
 # Initialise l'affichage   
 draw.drawInit()
 
 # t_world devient un alias de la liste présente comme attribut dans l'objet maze
 # autrement dit si vous modifiez t_world c'est comme si vous modifiez maze.t_world
 t_world = maze.t_world

 # A propos de l'objet Maze :
 #------------------------------
 # maze est un objet, il possede donc des fonctions qui peuvent être appelé  : 
 # maze.setValueAtXY(x,y,value) modifie la matrice t_world (n'oubliez pas que t_world est une liste, donc mutable, et que sa référence est donc partagé avec maze.t_world)
 # maze.getValueAtXY(x,y) renvoie la valeur à la position x,y

 sortie = False
 # contient la direction du robot, utile pour avancer :)
 directionRobot = ""

 # Intialisation x y entree et sortie, x y robot

 # Correspondance couleurs <-> chiffre 
 # Les autres couleurs sont dans le fichier constants.py qui est importé en début de programme
 draw.addColorRules(c.cWall,c.cWhite)
 draw.addColorRules(c.cEmpty,c.cBlack)

# BOUCLE INFINIE JEU PRINCIPALE
 while sortie == False:
	# Pour recuperer les événements dans pygame (permet de quitter avec la croix de la fenetre) 
	draw.events()
	
	# Indicateur de sortie
	if sortie == False:



		# Dessine le labyrinthe, a une vitesse donné en paramètre
		draw.drawScreen(t_world,40)

	else:
		# Permet de quitter sans que l'utilisateur ai besoin de cliquer sur la croix
		# c'est à dire dès que l'on a trouvé la sortie
		sortie = True

def avance(direction,x,y):
	
	print "avance"
	
	#return [newX,newY]

def calculeChemin(t_world,xRobot,yRobot):
 
	# Stocke les valeurs X,Y contenues dans le voisinnage
	valueVoisinnage = []

	# par defaut , la valeur est a None, un mot clef special de python
	# Testable avec if, ou is : http://stackoverflow.com/questions/3965104/not-none-test-in-python
	endCaseResult = None
	emptyCaseResult = None
	paintedCaseResult = None

	print "calculeChemin"

	# Trois return dans cette fonction
	# return 1 : return [endCaseResult,c.cWay]
	# return 2 : return [emptyCaseResult, c.cWay]
	# return 3 : return [paintedCaseResult, c.cNoWay]

def getDirection(tableau, valueToFind):
	# MAPPING ENTRE DIRECTION ET VALEUR RETOURNE
	# INDICE 0 = G ; INDICE 1 = H ; INDICE 2 = D ; INDICE 3 = 
	# Exemple : indiceToDirection[0] renvoie "G"
	indiceToDirection = {0:"G",1:"H",2:"D",3:"B"}

	# Soit la premiere direction au format caractere, soit la valeur None
	# return 1 : return charDirection
	# return 2 : None

def randomDirection(tableau,valueToFind):
	# MAPPING ENTRE DIRECTION ET VALEUR RETOURNE
	# INDICE 0 = G ; INDICE 1 = H ; INDICE 2 = D ; INDICE 3 = B  
	# Exemple : indiceToDirection[0] renvoie "G"
	indiceToDirection = {0:"G",1:"H",2:"D",3:"B"}

	print "random direction"

	# Soit un caractère indiquant une direction au hasard, soit retourne None, qui est un mot 
	# clef special de python que l'on peut ensuite tester avec un if
	# return 1 : return randomCharDirection
	# return 2 : return None

def returnEmptyCase(t_world):
 # on va de 0 a taille - 1
 x = random.randint(0,len(t_world[0]) - 1 )
 y = random.randint(0,len(t_world) - 1 )
 # Tant que cela n'est pas une case vide
 while (t_world[y][x] != c.cEmpty):
	print t_world[y][x] 
	x = random.randint(0,len(t_world[0]) - 1 )
	y = random.randint(0,len(t_world) - 1 )
 return [x,y]

 # Traitement pour la recherche de motif (cul de sac) dans la carte
def returnWallCase(t_world):
 
 # on va de 0 a taille - 1
 x = random.randint(0,len(t_world[0]) - 1 )
 y = random.randint(0,len(t_world) - 1 )

 # Renvoie un X,Y correspondant à la recherche de motif 
 # pour le placement de l'entree / sortie
 return [x, y]

def xyVoisinnage(t_world, xRobot, yRobot):
 yMaxSize = len(t_world)
 xMaxSize = len(t_world[0])
 voisinnage = []

 # Traitement

 # retourne [X,Y] une fois ajouté au tableau voisinnage
 # return voisinnage
 
# ENTREE DU PROGRAMME
if __name__ == "__main__":
 #taille du labyrinthe
 size = 20

 maze = Maze(size,size)

 run(maze)
