# -*- coding: utf-8 -*-
class Navigateur(object):
   def __init__(self,yeux,bras,jambes): # <1>
      self.tete = 1 # <2>
      self.nbYeux = yeux # <3>
      self.nbBras = bras
      self.nbJambes = jambes
      self.afficheInfo() # <4>
      
   def afficheInfo(self): # <5>
      print "Bonjour ! J'ai ", self.nbYeux, "yeux, ", self.tete, " tête, ", self.nbBras, " bras, et ", self.nbJambes, " jambes ..." 
   
   def accident(self,type): # <6>
      if type == "bras":
         self.nbBras = self.nbBras - 1 # <7>
      elif type == "jambe":
         self.nbJambes = self.nbJambes - 1
      elif type == "yeux":
         self.nbYeux = self.nbYeux - 1
   
   def initGrade(self):
      self.grade = "minable" # <8>
      print "je suis un pirate ", self.grade  
   
   def augmenteGrade(self):   
      if self.grade == "minable": 
         self.grade = "minus" 
      elif self.grade == "minus":
         self.grade = "chef"
      elif self.grade == "chef":
         self.grade = "capitaine"

