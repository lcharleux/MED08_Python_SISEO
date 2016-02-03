# -*- coding: utf-8 -*-
"""
Mon premier module !

@author: lcharleux
"""

import numpy as np

def Montagne(X, Y, zmax = 1000.):
  """
  Une montagne.
  
  Entrées:
  
  * X, Y: coordonnées.
  
  
  Sorties: 
  
  * Z: de même dimensions que X et Y
  """
  R = (X**2 + Y**2)**.5
  Theta = np.arccos(X / R) * np.sign(Y)
  
  Z = zmax - 8 * R**2 + 50 *  R * np.cos(5 * Theta) * (1. + .5 * np.sin(R))
  Z = np.where(Z < 0., 0., Z)
  return Z

from scipy.interpolate import griddata   
def Coupe(X, Y, Z, x, y):
  """
  Calcule une coupe de la montagne selon le trajet défini par (x,y)
  """
  X = X.flatten()
  Y = Y.flatten()
  Z = Z.flatten()
  z = griddata((X, Y), Z, (x, y))
  return z