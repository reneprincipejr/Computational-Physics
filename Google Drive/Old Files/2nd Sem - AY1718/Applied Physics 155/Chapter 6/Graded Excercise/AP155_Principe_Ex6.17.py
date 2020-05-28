# In[8]:


#equation for voltage 2
#(V2-V+/R3)+(V2/R4)-Io[(exp((V1-V2)/VT))-1] = 0

import numpy as np
from numpy.linalg import solve, norm
from sympy import symbols, diff
V1, V2 = symbols('x y', real=True)

#V1, V2 = 2, 1
#f1 = V1 + ((15e-6)/4)*[(np.exp((V1-V2)/0.05))-1] - (25/4)
#f2 = V2 - ((5-6)/2)*[(np.exp((V1-V2)/0.05))-1] - (15/6) 


def f(V1,V2):
    f1 = V1 + ((15e-6)/4)*((np.exp((V1-V2)/0.05))-1) - (25/4)
    f2 = V2 - ((5e-6)/2)*((np.exp((V1-V2)/0.05))-1) - (15/6) 
    return np.array([f1,f2],float)


def df(V1,V2):
    f1 = V1 + ((15e-6)/4)*((np.exp((V1-V2)/0.05))-1) - (25/4)
    f2 = V2 - ((5e-6)/2)*((np.exp((V1-V2)/0.05))-1) - (15/6) 
    df11 = diff(f1, V1)
    df12 = diff(f1, V2)
    df21 = diff(f2, V1)
    df22 = diff(f2, V2)
    
    return np.array([[df11,df12],
                     [df21,df22]],float)

V1 = 0.5
V2 = 0.0

V_val = f(V1,V2)
V_norm = norm(V_val, ord = 2)
accuracy = 1e-15

while abs(V_norm) > accuracy:

    delta = solve(df(V1,V2),f(V1,V2))
    V1 -= delta[0]
    V2 -= delta[1]
    
    V_val = f(V1,V2)
    V_norm = norm(V_val, ord = 2)

print(V1,V2, V1-V2)


#def poly1(f_1, df_1, x1, accuracy):
#    delta = np.linalg.solve(f_1(x1),df_1(x1))
#    while abs(delta)>accuracy:
#        delta = f_1(x1)/df_1(x1)
#        x1 -= delta
#    return x1

#
#def poly2(f_2, df_2, x2, accuracy):
#    delta = 1.0
#    while abs(delta)>accuracy:
#        delta = f_2(x2)/df_2(x2)
#        x2 -= delta
#    return x2
#
#
#
