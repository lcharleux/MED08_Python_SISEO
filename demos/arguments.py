# -*- coding: utf-8 -*-
"""
Objets avec Python

@author: lcharleux
"""
def fonction(x, y, z, *args, **kwargs):
  print x, y, z
  print args, kwargs
  
fonction(1,2, z = 5, truc = 36, machin= 12)  

def somme(*args, **kwargs):
  return sum(args) + sum(kwargs.values())
  
print somme(3, 5, 12, x= 36)  
 

def fonc(lapin, pomme):
  print lapin, pomme
  
fonc(4, 5)  

dic = {"pomme":"pourrie", "lapin":"oreilles"}

fonc(*dic)