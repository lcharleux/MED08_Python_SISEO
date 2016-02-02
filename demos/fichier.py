# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:24:01 2016

@author: lcharleux
"""

import numpy as np

data = np.random.rand(100,4)

# Première méthode: Python
f = open("data.dat", "w")
for i in xrange(len(data)):
  for j in xrange(len(data[i])):
    f.write( "{0:.2f} ".format(data[i,j]) )
  f.write("\n")
f.close()

# Seconde méthode: Python + Numpy
np.savetxt("data_np.dat", data)

#Charger un fichier
data2 = np.loadtxt("data.dat")
   