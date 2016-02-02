# -*- coding: utf-8 -*-
"""
Un peu de traitement d'images

@author: lcharleux
"""
import numpy as np
import matplotlib.pyplot as plt
import PIL
from matplotlib import cm

# path = "/home/lcharleux/Documents/Enseignement/Formations_Organisees/2016-01_Python_SISEO/demos/images/koala.jpg" # Chemin absolu
path = "images/koala.jpg" # Chemin relatif
im = PIL.Image.open(path)
R, G, B = im.split() # R = rouge, G = vert, B = bleu
R = np.asarray(R, dtype = np.uint8)
G = np.asarray(G, dtype = np.uint8)
B = np.asarray(B, dtype = np.uint8)

fig = plt.figure("mes images")
plt.clf()
ax = fig.add_subplot(2,2,1)
ax.set_title("Red")
plt.imshow(R, cmap = cm.gray)
plt.grid()
plt.colorbar()
ax = fig.add_subplot(2,2,2)
ax.set_title("Green")
plt.imshow(G, cmap = cm.gray)
plt.grid()
plt.colorbar()
ax = fig.add_subplot(2,2,3)
ax.set_title("Blue")
plt.imshow(B, cmap = cm.gray)
plt.grid()
plt.colorbar()
plt.show()
