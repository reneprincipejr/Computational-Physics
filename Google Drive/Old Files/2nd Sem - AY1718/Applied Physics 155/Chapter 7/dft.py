# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 12:32:39 2018

@author: Rene
"""

from numpy import zeros,loadtxt
from matplotlib.pyplot import plot,xlim,show
from cmath import exp,pi

def dft(y):
    N = len(y)
    c = zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*exp(-2j*pi*k*n/N)
    return c

y = loadtxt("pitch.txt",float)
c = dft(y)
plot(abs(c))
plot
xlim(0,500)
show()