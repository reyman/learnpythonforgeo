# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 14:52:20 2012

@author: srey
"""

from random import randint
import os

clear = lambda: os.system('clear')

if __name__ == "__main__":
	
   clear()
	
	#Par defaut on a envie de jouer :)
	iWanToPlay = True
	turn_message = ["Vous avez chaud ... le soleil tape aujourd'hui", 
					"encore quelques jours de marche vers le saint graal",
					"un lapin vous mord la jambe sans raison, heureusement vous êtes solide",
					"vous avez perdu votre carte, c'est balot pour un explorateur comme vous",
					"si seulement je pouvais trouver un jardinet ...", 
					"Clap Clap Clap... Clap Clap Clap..."]
					
	#Par defaut on ne fait pas un tour suivant, on attend la réponse de l'utilisateur
	nextTurn = False
				
	name = raw_input("Quel est le nom de ton explorateur ?")
	print "(L pour lister les commandes)"
	print "%s entre dans un monde inconnu et dangereux, à la recherche d'aventure.." % name
	print "Sache %s que tu as quelques jours avant que le grand nazgul se reveille et parte a ta recherche" % (name)
	raw_input("Appuie sur une touche ")
	
	# Boucle de jeu principale
	while(iWanToPlay == True ):
		
      clear()
		
		#On affiche un message different a chaque tour, histoire de rajouter un peu d'ambiance
		if nextTurn == True:
		  
			num = randint(0,len(turn_message))
			print turn_message[num]
			
		nextTurn = False
		
		# Boucle de tour de jeu
		while(nextTurn == False):
			
			line = raw_input("> ")
			clear()
			cmd = line.split()
			# print "ligne contient = " , cmd
			# Est ce que la commande existe et est ce que sa longueur superieure a zero ?
			if len(cmd) > 0:
				commandFound = False
				
				# Est ce que la commande existe ?
				if "Q" in cmd:
					commandFound = True
					nextTurn = True
					iWanToPlay = False
				
				if "L" in cmd:
					commandFound = True
					print "Q = Quitter le jeu"
					print "L = Lister l'ensemble des commandes"
							
				if commandFound == False:
					print "%s ?! Je ne comprend pas votre commande." % name
				
				
				
		if iWanToPlay == False :
			print " bye bye %s !" % name


		
