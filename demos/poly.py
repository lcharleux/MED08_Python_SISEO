# -*- coding: utf-8 -*-
"""
Polynomes et interpolation

@author: lcharleux
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

Np = 11

# Raw data
x = np.linspace(0., 10., Np) 
y = np.random.rand(Np)



xi = np.linspace(-1., 11., 1000)

fig = plt.figure("Interpolation")
plt.clf()
plt.plot(x, y, "or", label = "Data")
for i in xrange(11):
  p = np.poly1d(np.polyfit(x, y, deg = i))  
  plt.plot(xi, p(xi), label = "Deg = {0}".format(i))

plt.grid()
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()