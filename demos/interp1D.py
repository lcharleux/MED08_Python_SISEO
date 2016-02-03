# -*- coding: utf-8 -*-
"""
Interpolation en 1D

@author: lcharleux
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

Np = 50

# Raw data
x = np.linspace(0., 10., Np) 
y = np.random.rand(Np)

# Interpolation
Npi = 1000
xi = np.linspace(0., 10., Npi)
# Nearest interpolation
y_nearest = interpolate.interp1d(x, y, kind = "nearest")(xi)
y_linear = interpolate.interp1d(x, y, kind = "linear")(xi)
y_quadratic = interpolate.interp1d(x, y, kind = "quadratic")(xi)
y_cubic = interpolate.interp1d(x, y, kind = "cubic")(xi)

fig = plt.figure("Interpolation")
plt.clf()
plt.plot(x, y, "or", label = "Data")
plt.plot(xi, y_nearest, label = "Nearest")
plt.plot(xi, y_linear, label = "Linear")
plt.plot(xi, y_quadratic, label = "Quadratic")
plt.plot(xi, y_cubic, label = "Cubic")
plt.grid()
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()