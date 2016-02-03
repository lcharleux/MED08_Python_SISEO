# -*- coding: utf-8 -*-
"""
Gestion des fichiers

@author: lcharleux
"""

import os

liste_fichiers = os.listdir("./")
f = liste_fichiers[0]
print os.path.exists(f)
