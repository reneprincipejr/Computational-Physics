# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 08:51:37 2018

@author: Rene
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
from skimage.draw import circle
from skimage.draw import polygon
import matplotlib.image as mpimg
from cmath import exp
from numpy.fft import rfft2,irfft2,fftshift,ifftshift

def FFT(aperture):
    #f = plt.figure()
    #gs = gridspec.GridSpecBase(1, 5)    
    #ax1 = f.add_subplot(gs[0,0:1])
    #ax1.imshow(aperture, cmap = 'gray')
    ft_aperture = rfft2(aperture)
    FT_aperture = fftshift(np.abs(ft_aperture))
    #ax2 = f.add_subplot(gs[0,2])
    #ax2.imshow(FT_aperture, cmap = 'gray')
    ift_aperture = irfft2(ft_aperture)
    #ax3 = f.add_subplot(gs[,3:4])
    #ax3.imshow(np.abs(ift_aperture), cmap = 'gray')
    plt.imshow(aperture, cmap = 'gray')
    plt.show()
    plt.imshow(FT_aperture, cmap = 'gray')
    plt.show()
    plt.imshow(np.abs(ift_aperture), cmap = 'gray')
    plt.show()


L = 256
aperture = np.zeros(shape = (L,L), dtype = float)
center = (L/2,L/2)

def Circle(r): #radius
    x, y = circle(*center, r)
    aperture[x, y] = 1
    
    return aperture
#######

def Rectangle(w,h):
    width = np.arange(center[0]-w//2,center[0]+w//2)
    height = np.arange(center[1]-h//2,center[1]+h//2)
    for i in width:
        for j in height :
            aperture[int(i)][int(j)] = 1
            
    return aperture


