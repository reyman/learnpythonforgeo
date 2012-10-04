# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 14:32:50 2012

@author: srey
"""

from random import randint
 
# Monty Python game
# par défaut on meurt, sauf si on répond bien aux trois questions ...			
die = True
name = raw_input("Quel est le nom de ton explorateur ? ")
print "..."
print "Il fait nuit et vous entendez un bruit sourd qui s'approche ... cela vous reveille ... "
print "Tump.. Tump ... Tump .. ?! Grrr !"
print "Monstre : Quel est ton nom explorateur imprudent ?"
rep1 = raw_input()
if rep1 in ["lancelot","robin","galahad","arthur"]:
	if rep1 != name:
		print "Tu mens ! "
	else:
		print "Monstre : Quel est ta quête ?"
		rep2 = raw_input()
		if rep2 in ["graal"]:
			numQuestion = randint(0,2)
			if (numQuestion == 0):
				print "Monstre : Quel est ta couleur préférée ?"
				rep3 = raw_input()
				if rep3 in ["bleu"]: die = False
			elif (numQuestion == 1):
				print "Monstre : Quel est la capitale de l'Assyrie ?"
				rep3 = raw_input()
				if rep3 in ["Assur", "Kalkhu", "Dur-Sharrukin","Ninive"]: die = False
			elif (numQuestion == 2):
				print "Monstre : A quelle vitesse vole une hirondelle non chargée ?"
				rep3 = raw_input()
				if rep3 in ["une hirondelle africaine ou une européenne ?"]: 
					print "Monstre : Aahhh ...  *R.I.P* "								
					die = False
					
if die == True:
	print "Aahhh ...  *R.I.P* "