# In[46]:


import numpy as np
import matplotlib.pyplot as plt 

accuracy = 1e-10

def p(x):
    return 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1
def dpdx(x):
    return 6*924*x**5 - 5*2772*x**4 + 4*3150*x**3 - 3*1680*x**2 + 2*420*x - 42

def poly(p, dpdx, x, accuracy):
    delta = 1.0
    while abs(delta)>accuracy:
        delta = p(x)/dpdx(x)
        x -= delta
    return x

t = np.linspace(0.000001,1)
ypoints = np.zeros(len(t))


plt.plot(t, p(t))
plt.plot(t, np.zeros(len(t)))
plt.xlabel("x")
plt.ylabel("P(x)")
plt.title("Sixth Order Polynomial")
plt.annotate('0.3', xy=(0.03,0), xytext=(0.04,0.1),
            arrowprops=dict(facecolor='red', shrink=0.01),)
plt.annotate('0.17', xy=(0.17,0), xytext=(0.15,0.1),
            arrowprops=dict(facecolor='red', shrink=0.01),)
plt.annotate('0.38', xy=(0.38,0), xytext=(0.39,0.1),
            arrowprops=dict(facecolor='red', shrink=0.01),)
plt.annotate('0.61', xy=(0.61,0), xytext=(0.6,0.1),
            arrowprops=dict(facecolor='red', shrink=0.01),)
plt.annotate('0.83', xy=(0.83,0), xytext=(0.84,0.1),
            arrowprops=dict(facecolor='red', shrink=0.01),)
plt.annotate('0.96', xy=(0.96,0), xytext=(0.95,0.1),
            arrowprops=dict(facecolor='red', shrink=0.01),)                                       
                                                                                                             
rene = 0
for i in t:
    ypoints[rene] = poly(p, dpdx, i, accuracy)
    rene += 1

print(ypoints)
print('')
print("The solutions are 0.03376524, 0.16939531, 0.38069041, 0.61930959, 0.83060469, 0.96623476")

