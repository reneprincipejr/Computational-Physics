# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 14:37:52 2018

@author: Rene
"""

import numpy as np
import matplotlib.pyplot as plt
from cmath import exp,pi

#LADING THE DATA
sunspots = np.loadtxt("sunspots.txt",float)
#x = sunspots[:,0]
#y = sunspots[:,1]
x = sunspots[500:1000,0]
y = sunspots[500:1000,1]

#PLOT OF THE DATA
plt.plot(x,y)
plt.show()

#
print("Estimated cycle length, T = 150")
print("k = fN = (1/T)N = (1/150)3000")
print("k is around 20")


def dft(y):
    N = len(y)
    c = np.zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*exp(-2j*pi*k*n/N)
    return c

c = dft(y)
plt.plot(abs(c))
plt.show()
