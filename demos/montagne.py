# -*- coding: utf-8 -*-
"""
Tracer et couper une montagne

@author: lcharleux
"""

import monModule
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

x = np.linspace(-10., 10., 100)
y = x
X, Y = np.meshgrid(x, y)
Z = monModule.Montagne(X, Y)

# coupe:
xc1 = x
yc1 = y
zc1 = monModule.Coupe(X, Y, Z, xc1, yc1)
xc2 = x 
yc2 = y /2. + 2.
zc2 = monModule.Coupe(X, Y, Z, xc2, yc2)


# Tracé
fig = plt.figure(0)
plt.clf()
ax = fig.add_subplot(2,2,1)
ax.set_aspect("equal")
plt.contourf(X, Y, Z, 20, 
             cmap = matplotlib.cm.terrain)
cbar = plt.colorbar()
cbar.set_label("Altitude, $z$ [m]")
plt.contour(X, Y, Z, 10, colors = "k")
plt.plot(xc1, yc1, "r-")             
plt.plot(xc2, yc2, "m-")             
plt.grid()
ax = fig.add_subplot(2,2,2)
plt.plot(zc1, yc1, "r-")
plt.plot(zc2, yc2, "m-")
plt.grid()            
ax = fig.add_subplot(2,2,3)
plt.plot(xc1, zc1, "r-")
plt.plot(xc2, zc2, "m-")
plt.grid()             
plt.show()

