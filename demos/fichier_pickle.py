# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:24:01 2016

@author: lcharleux
"""

import numpy as np
import pickle

data = ["truc", "machin", [1,2,3]]

f = open("data.pckl", "w")
pickle.dump(data, f)
f.close()

del data # On efface fonc

f = open("data.pckl", "r")
data2 = pickle.load(f)
f.close()
