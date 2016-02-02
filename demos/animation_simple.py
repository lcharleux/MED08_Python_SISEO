# -*- coding: utf-8 -*-
"""
Animation simple

@author: lcharleux
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

x = np.linspace(0., 10., 1000)
y = np.exp(-x / 10.) * np.sin(2.* np.pi * x)


fig = plt.figure("Animation !")
plt.clf()
line = plt.plot([], [])[0]
plt.grid()
plt.xlim(0., 10.)
plt.ylim(-1., 1.)


def init():
  line.set_data([], [])
  return (line,) 

dx = .1
def animate(i):
  x2 = x + i * dx
  y = np.exp(-x2 / 10.) * np.sin(2.* np.pi * x2)
  line.set_data(x,  y)
  return (line,)
  
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=5000, interval=20, blit=True)

plt.show()  