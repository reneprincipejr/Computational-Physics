# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 14:47:47 2018

@author: Rene
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigvals, inv


def main(f, m1, m2, q):
    print("Oscillator Chain")
    mat1 =  np.array([[            2*f,    -f,    0, -f*np.exp(-1j*q)],
                      [             -f,   2*f,   -f,                0],
                      [              0,    -f,  2*f,               -f],
                      [-f*np.exp(1j*q),     0,   -f,              2*f]])
    # will cyclic rearrangements of m1 and m2 below change the results? Try it
    # what will be the dimensions/shape of massmat?
    massmat = np.diag([m1, m1, m1, m2])
    # what happens if inv(massmat) * mat1(q) is used instead of 
    # inv(massmat).dot(mat1(q))?
    mat2 = inv(massmat)*mat1
    # what is the python type of kwargs?
    # complete the following line. you should use plot_step
    x_axis = np.arange(-np.pi, np.pi+np.pi/50, np.pi/50) 
    # what is the difference between eigvals() and eig()?
    # replace the following line to use eig() instead of eigvals()
    eigenlist = []
    for i in range(len(x_axis)):
        xvalue = x_axis[i]
        eigenvalue = eigvals(mat2(xvalue)
        eigenlist.append(eigenvalue)
    
    plt.plot(x_axis, eigenlist)
    plt.xticks([r"$\pi$", r"$\frac{\pi}{2}$", "0", r"$\frac{\pi}{2}$", r"$\pi$"])
    #plt.xlim(# ...
    # add x-large axis labels
    # ...
    plt.tick_params('x', labelsize='x-large')
    plt.show()
                  
        
    
        