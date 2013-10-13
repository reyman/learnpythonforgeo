# -*- coding: utf-8 -*-
sac = int(raw_input("nombre de pièces dans votre sac ?"))

def douane(sac):
    taxe = 15
    if sac > taxe:
        print("par ici la monnaie")
        return sac - taxe
    else:
        print("pas de taxe pour les pauvres")
        return sac

print douane(sac)