# -*- coding: utf-8 -*-
"""
Une classe qui mime une fonction

@author: lcharleux
"""

class mafonction(object):
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
  def __call__(self, a, b, c):
    x = self.x
    y = self.y
    z = self.z
    return a * x  + b * y + c * z
   
mf = mafonction(1,2,3)   
    
