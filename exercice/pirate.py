# -*- coding: utf-8 -*-

import random

# Definition des classes du monde des pirates !
class Navigateur(object):
    def __init__(self, nom, yeux=2, bras=2, jambes=2, argent=0, force=1, grade="minable"):
        self.nom = nom
        self.tete = 1
        self.nbYeux = yeux
        self.nbBras = bras
        self.nbJambes = jambes
        self.argent = argent
        self.force = force
        self.grade = grade
        self.afficheInfo()

    def afficheInfo(self):
        print "Bonjour ! Je suis ", self.nom, " un navigateur", self.grade, "et de force", self.force, "\n"
        print "J'ai ", self.nbYeux, "yeux, ", self.tete, " tête, ", self.nbBras, " bras, et ", self.nbJambes, " jambes ...\n"
        print "J'ai ", self.argent, " dans ma bourse \n"

    def augmenteGrade(self):
        if self.grade == "minable":
            self.grade = "minus"
        elif self.grade == "minus":
            self.grade = "chef"
        elif self.grade == "chef":
            self.grade = "capitaine"

        self.force = self.force + 1

class Taverne(object):
    def __init__(self, listeDeNoms, listeDePrenoms):
        self.listDeNoms = listeDeNoms
        self.listDePrenoms = listeDePrenoms

    def debaucher(self):
        salaire = random.randint(1, 10)
        force = salaire * 1.5
        nomPrenom = " ".join([self.listDeNoms[random.randint(0, len(self.listDeNoms) - 1)],
                              self.listDePrenoms[random.randint(0, len(self.listDePrenoms) - 1)]])
        return Navigateur(nomPrenom, force=int(force))


class Equipage(object):
    def __init__(self, marins):
        self.marins = marins

    def jourDePaye(self, sommeParMarin):
        print ("ajoute de l'argent à la bourse de chacun des marins")


class Navire(object):
    def __init__(self, nom, marins):
        self.nom = nom
        self.equipage = Equipage(marins)

    def combat(self, ennemi):
        print "combat le bateau ennemi ! "

# Fonction pour construire equipage
def buildEquipage(nbMarins):
    equipage = []
    for x in range(nbMarins):
        equipage.append(taverneAPirate.debaucher())
    return equipage

# Programme principal
if __name__ == "__main__":
    nomDePirate = ["Bonny", "Jack", "Teach", "Drake", "Morgan", "Nau", "Read"]
    prenomDePirate = ["Anne", "Calico", "Edward", "Francis", "Henry", "Jean", "Mary"]

    taverneAPirate = Taverne(nomDePirate, prenomDePirate)

    Navire("Queen Anne's Revenge", buildEquipage(10))
    Navire("Adventure Galley", buildEquipage(10))

    # Combat

    # Jour de paye
