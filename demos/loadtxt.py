# -*- coding: utf-8 -*-
"""
Usage de loadtxt avec des virgules

@author: lcharleux
"""

import numpy

path = "fichiers/data"
conv = {}
conv[0] = lambda txt : txt.replace(",", ".")    
conv[1] = lambda txt : txt.replace(",", ".")    
data = np.loadtxt(path, converters = conv)

lambda x: x**2