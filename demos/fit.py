# -*- coding: utf-8 -*-
"""
Polynomes et interpolation

@author: lcharleux
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

Np = 100
# Raw data
x = np.linspace(0., 10., Np) 


def fonction(x, a, b, c):
  """
  La fonction de mon modèle
  """
  return a * np.cos(x + b) * np.exp(-x/c)


a_sol, b_sol, c_sol = 1., 2., 3.
y_th = fonction(x, a_sol, b_sol, c_sol) 
y_exp = y_th + np.random.normal(loc = 0., scale = .1, size = Np)

xi = np.linspace(-1., 11., 1000)

# Optimisation
a0, b0, c0 = 12., -3., 4. # Valeur initiale assez mal choisie
p_opt = optimize.curve_fit(fonction, x, y_exp)
a_opt, b_opt, c_opt = p_opt[0]
y_opt = fonction(x, a_opt, b_opt, c_opt)
fig = plt.figure("Interpolation")
plt.clf()
plt.plot(x, y_th, "g--", label = "Ideal data")
plt.plot(x, y_exp, "or", label = "Exp. data")
plt.plot(x, y_opt, "b-", label = "Fit")
plt.grid()
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()