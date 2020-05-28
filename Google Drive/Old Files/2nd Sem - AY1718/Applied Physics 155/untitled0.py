# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 00:43:04 2018

@author: Rene
"""

from numpy import euler_gamma as y
from numpy import exp, linspace
import matplotlib.pyplot as plt
import math

def gamma(z):

    def f(x):
	    return (x**(z-1)*exp**-x)
	
    N = 1000
    a = 0
    b = N
    h = (b-z)/N
	
    s = f(z) + f(b) + 4*f(b-h)
    for k in range(1,N//2):
        
        s += 4*f(z + (2*k-1)*h) + 2*f(z+2*k*h)
	
    I = h/3*s/pi
	
    return I