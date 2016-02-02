# -*- coding: utf-8 -*-
"""
Objets avec Python

@author: lcharleux
"""

class Personne(object):
  def __init__(self, nom, prenom, numero):
    self.nom    = nom
    self.prenom = prenom
    self.numero = numero
  
  def __repr__(self):
    return "Je suis {0} {1} (tel:{2})".format(self.nom, self.prenom, self.numero)
    
class Doctorant(Personne):
  def __init__(self, sujet, *args, **kwargs):
    Personne.__init__(self, *args, **kwargs)
    self.sujet = sujet
  
  def __repr__(self):
    out = Personne.__repr__(self)
    out += " et je travaille sur {0}".format(self.sujet)  
    return out
    
    
bl = Doctorant(nom = "Bob",  
               prenom = "L'eponge", 
               sujet = "ma thèse...", 
               numero = "06xxxxx")    
               
print bl               