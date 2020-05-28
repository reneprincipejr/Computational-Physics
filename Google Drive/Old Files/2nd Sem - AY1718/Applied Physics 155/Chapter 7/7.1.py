# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 13:42:53 2018

@author: Rene
"""

import numpy as np
import matplotlib.pyplot as plt
from cmath import exp,pi

N = 1000

#GENERATE A SQUARE WAVE
y1 = -np.ones(N)
y1[:N//2]=1
plt.plot(y1)
plt.title("Square Wave")
plt.show()

#GENERATE A SAWTOOTH WAVE

n = np.arange(N)
y2 = n
plt.plot(y2)
plt.title("Sawtooth Wave")
plt.show()

#GENERATE A MODULATED SINE WAVE
n = np.arange(N)
y3 = np.sin(pi*n/N)*np.sin(20*pi*n/N)
plt.plot(y3)
plt.title("Modulated Sine Wave")
plt.show()

#CONVERTING INTO A DISCRETE FORM
def dft(y):
    N = len(y)
    c = np.zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*exp(-2j*pi*k*n/N)
    return c

#FOURIER TRANSFORM OF THE SQUARE WAVE
c1 = dft(y1)
plt.plot(abs(c1))
plt.xlim(0,100)
plt.title("FT of Square Wave")
plt.show()

#FOURIER TRANSFORM OF THE SAWTOOTH WAVE
c2 = dft(y2)
plt.plot(abs(c2))
plt.xlim(0,300)
plt.ylim(0,40000)
plt.title("FT of Sawtooth Wave")
plt.show()

#FOURIER TRANSFORM OF THE MODULATED SINE WAVE
c3 = dft(y3)
plt.plot(abs(c3))
plt.xlim(0,100)
plt.title("FT of Modulated Sine Wave")
plt.show()