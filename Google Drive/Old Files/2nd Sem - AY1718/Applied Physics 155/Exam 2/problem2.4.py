# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 11:55:04 2018

@author: Rene
"""

import numpy as np
import matplotlib.pyplot as plt
from cmath import exp,pi

N = 1000

#GENERATE A SQUARE WAVE

y = -np.ones(N)
y[:N//2]=1

#PERFORM A DISCRETE FOURIER TRANSFORM ON y

def dft(y):
    N = len(y)
    c = np.zeros(N,complex)
    for k in range(N):
        for n in range(N):
            c[k] += y[n]*exp(-2j*pi*k*n/N)
    return c/N

c = (dft(y))

#SETTING THE FOURIER COEFFICIENTS, c, AFTER THE 10TH TERM TO 0

c[10:len(c)]= np.zeros(len(c)-10)

#PERFORM AN INVERSE DISCRETE FOURIER TRANSFORM ON THE MODIFIED c

def inv_dft(c):
    N = len(c)
    y_i = np.zeros(N,complex)
    for k in range(N):
        for n in range(N):
            y_i[k] += c[n]*exp(2j*pi*k*n/N)
    return 2*y_i

y_recovered = (inv_dft(c))

#PLOTS

plt.plot(y, label="Square Wave")
plt.plot(y_recovered, label="Recovered Square Wave")
plt.title("FOURIER FILTERING")
plt.legend()
plt.xlabel("Time, s")
plt.ylabel("Amplitude")
plt.show()

print("The wiggles and artifacts that is seen on the recovered square wave is best described by the Gibb's Phenomenon.")
print('"It is created when one tries to estimate a function that has a jump discontinuity with a Fourier series."')
print("Since our function is a square wave, the estimation tends to overshoot on the jump.")
print("This could be lessened/smoothed if more harmonics were used, but in the graph, I only used the first 10 coefficients that's why the wiggles/overshoots are visible.")
print("")
print("Source: Merz, S. 'What is Gibb's Phenomenon'. Quora. (2017)")
print("URL: https://www.quora.com/What-is-Gibbs-phenomenon")
print("Date retrieved: April 7, 2017")
