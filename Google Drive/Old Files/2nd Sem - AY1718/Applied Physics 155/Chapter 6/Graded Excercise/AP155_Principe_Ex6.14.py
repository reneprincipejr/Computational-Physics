# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 09:42:20 2018

@author: Karahan
"""

from scipy.constants import hbar, elementary_charge
import numpy as np
import matplotlib.pyplot as plt

V = 20 #eV
w = 1e-9 #meters
m = 3.1094e-31
e_c = elementary_charge
E = np.arange(0,21)

y1_list = np.zeros(len(E))
y2_list = np.zeros(len(E))
y3_list = np.zeros(len(E))

rene = 0
for e in E:
    y1_list[rene] = np.tan(np.sqrt(((w**2)*(m*1.6)*(e*e_c))/(2*(hbar**2))))
    y2_list[rene] = np.sqrt((V-(e*e_c))/(e*e_c))
    y3_list[rene] = -np.sqrt((e*e_c)/(V-(e*e_c)))
    rene += 1

print(y1_list,y2_list,y3_list)    

#I had to separate the graphs because an error occurs
#whenever I remove the plt.show() on every plot


plt.ylim(-10,20)
plt.xlim(0,20)
plt.plot(E,y1_list, "g-")
plt.plot(E,y2_list, "r-")
plt.plot(E,y3_list, "b-")
plt.show()