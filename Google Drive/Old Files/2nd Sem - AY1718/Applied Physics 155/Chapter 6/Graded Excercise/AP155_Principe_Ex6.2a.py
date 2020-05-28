from numpy import array,empty
import numpy

A = array([[ 4, -1, -1, -1 ],
           [-1,  0,  3, -1 ],
           [-1,  3,  0, -1 ],
           [-1, -1, -1,  4 ]], float)
v = array([ 5, 5, 0, 0 ],float)
N = len(v)

N = len(v)

for m in range(N):
	
    for i in range(m+1,N):
        if A[m,m] < A[i,m]:
            A[[m,i],:] = A[[i,m],:]	
            v[[m,i]] = v[[i,m]]
	
    div = A[m,m]
    A[m,:] /= div
    v[m] /= div

    for i in range(m+1,N):
        mult = A[i,m]
        A[i,:] -= mult*A[m,:]
        v[i] -= mult*v[m]

x = empty(N,float)
for m in range(N-1,-1,-1):
    x[m] = v[m]
    for i in range(m+1,N):
        x[m] -= A[m,i]*x[i]

a = numpy.linalg.solve(A,v)

    
print(a)
print(x)