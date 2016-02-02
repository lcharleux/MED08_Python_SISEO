# -*- coding: utf-8 -*-
"""
Tracé d'une courbe

@author: lcharleux
"""
import numpy as np
import matplotlib.pyplot as plt


def mafonction(t, omega= 1., tau = 10.):
  """
  Une fonction mathématique
  
  Entrées:
  
  * t: une variable
  * omega: pulsation
  * tau: temps caractéristique
  
  Renvoie:
  Une sinusoide amortie.
  """  
  return np.exp(-t / tau) * np.sin(omega * t)
  
    
t = np.linspace(0., 10., 1000)
omega = range(5) # valeurs de omega

 
colors = "ygcmkrbg"
# Tracé de la figure
plt.figure("Une figure")
plt.clf() # purge la figure
for i in xrange(len(omega)):
  o = omega[i]
  c = colors[i%len(colors)]
  a = mafonction(t, omega = o)
  plt.plot(t, a, color = c, label = "$\omega = {0:.0f}$".format(o))
plt.legend()
plt.grid()
plt.xlabel("Temps, $t$ [s]")
plt.ylabel("Amplitude, $a$, [N]")
#plt.show()
plt.savefig("mafigure.pgf")