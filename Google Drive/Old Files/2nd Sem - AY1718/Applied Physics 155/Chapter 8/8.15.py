# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 14:00:01 2018

@author: Rene
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import pi, sin, cos

l = 40.0
g = 9.81


def f(r,t):
    a1 = r[0]
    a2 = r[0]
    w1 = r[1]
    w2 = r[1]
    denom = 3 - cos(2*a1-2*a2)
    fa1 = w1
    fa2 = w2
    fw1 = -(w1**2*sin(2*a1-2*a2) + 2*w2**2*sin(a1-a2) + (g/l)*(sin(a1-2*a2)+3*sin(a1)))/denom
    fw2 = (4*w1**2*sin(a1-a2) + w2**2*sin(2*a1-2*a2) + (g/l)*(sin(2*a1-a2)-sin(a2)))/denom
    return np.array(([fa1,fa2],[fw1,fw2]),float)

a = 0.0
b = 100.0
N = 1000
h = (b-a)/N

tpoints = np.arange(a,b,h)
xpoints = []
ypoints = []

r = np.array(([pi/2,0],[pi/2,0]),float)
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6

plt.plot(tpoints,xpoints)
plt.show()

