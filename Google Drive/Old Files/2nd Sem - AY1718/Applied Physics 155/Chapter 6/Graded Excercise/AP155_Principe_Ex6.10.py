# In[56]:


from math import exp
import numpy as np
import matplotlib.pyplot as plt


accuracy = 10e-6
x1 = 1.0
error = 1.0
c = 2
n = 0

while error>accuracy:
    x1, x2 = 1 - exp(-c*x1), x1
    error = abs((x1-x2)/(1-1/(c*exp(-c*x1))))
    n += 1
    print("error is", error, "for", n, "iterations")
    

print("The value of x if c=2 is", x1)


# In[84]:


c = np.arange(0.01,3,0.1)
x = []
for C in c:
    x1 = 1.0
    error = 1.0
    
    while error>accuracy:
        x1,x2 = 1 - exp(-C*x1), x1
        error = abs((x1-x2)/(1-1/(C*exp(-C*x1))))
    x.append(x1)

#print(x,c)    
plt.plot(c,x)
plt.ylim(-0.1,1.1)
plt.xlabel("c")
plt.ylabel("x")
plt.title("Percolation Transition")
plt.annotate('epidemic threshold', xy=(1.05,0), xytext=(1.5, 0.05),
            arrowprops=dict(facecolor='red', shrink=0.01),)
plt.show()

