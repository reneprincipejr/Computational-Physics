import numpy as np
from numpy import sqrt
import matplotlib.pyplot as plt
#from cmath import exp, pi
from math import factorial



def H(n,x):
    if n==0:
        return 1
    elif n==1:
        return 2*x
    else:
        return 2*x*H(n-1,x)-2*(n-1)*H(n-2,x)

def ksi(n,x):
	
	return 1/sqrt(2**n*factorial(n)*sqrt(np.pi)) * np.exp(-x**2/2) * H(n,x)

	
x = np.linspace(-4,4,100)
n = [0,1,2,3]

for ni in n:
	plt.plot(x,ksi(ni,x),label=ni)

plt.legend()
plt.show()

x = np.linspace(-10,10,200)
plt.plot(x,ksi(30,x))
plt.show()

#
#
##Integration
#
#uncertainty = lambda n,x: x**2*ksi(n,x)**2
#
#def gaussxw(N):
#
#    # Initial approximation to roots of the Legendre polynomial
#    a = linspace(3,4*N-1,N)/(4*N+2)
#    x = cos(pi*a+1/(8*N*N*tan(a)))
#
#    # Find roots using Newton's method
#    epsilon = 1e-15
#    delta = 1.0
#    while delta>epsilon:
#        p0 = ones(N,float)
#        p1 = copy(x)
#        for k in range(1,N):
#            p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
#        dp = (N+1)*(p0-x*p1)/(1-x*x)
#        dx = p1/dp
#        x -= dx
#        delta = max(abs(dx))
#
#    # Calculate the weights
#    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)
#
#    return x,w
#
#N = 100
##x,w = gaussxw(N)
#
## 5.68
#def x_sq(n):
#	a = -1
#	b = 1
#	xp = 0.5*(b-a)*x + 0.5*(b+a)
#	wp = 0.5*(b-a)*w
#	
#	y = (1 + xp**2)/(1-xp**2)**2*uncertainty(n,xp/(1-xp**2))
#	s = sum(y*wp)
#	return s
#
#n = 5
##RMS = sqrt(sum([x_sq(ni)**2 for ni in range(1,n)]))
##print(RMS)
## 5.70
#a = -np.pi/2
#b = np.pi/2
#xp = 0.5*(b-a)*x + 0.5*(b+a)
#wp = 0.5*(b-a)*w
#
#n = 5
#y = uncertainty(n,np.tan(xp))/np.cos(xp)**2
#s = sum(y*wp)
#print(s)
#
#a = -10
#b = 10
#xp = 0.5*(b-a)*x + 0.5*(b+a)
#wp = 0.5*(b-a)*w
#
#n = 5
#y = uncertainty(n,xp)
#s = sum(y*wp)
#print(s)
