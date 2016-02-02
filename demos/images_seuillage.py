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

Z = R #On Garde un canal
Zs = Z > 100

fig = plt.figure("mes images")
plt.clf()
ax = fig.add_subplot(2,2,1)
plt.imshow(Z, cmap = cm.gray)
ax.set_title("Orginal")
ax = fig.add_subplot(2,2,2)
plt.imshow(Zs, cmap = cm.gray)
ax.set_title("Seuil")
ax = fig.add_subplot(2,2,3)
plt.hist(Z.flatten(), bins = 250)
plt.show()
