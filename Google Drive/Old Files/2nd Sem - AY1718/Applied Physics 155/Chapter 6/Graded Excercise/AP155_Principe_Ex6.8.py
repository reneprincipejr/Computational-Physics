# In[82]:

import numpy as np
from numpy.linalg import norm,eigh


A = np.array([[1, 4, 8, 4],
              [4, 2, 3, 7],
              [8, 3, 6, 9],
              [4, 7, 9, 2],], dtype=float)
n = len(A)

def decomposition(A):
    Q = np.zeros((n,n))
    R = np.zeros((n,n))
    
    for i in range(n):
        sum = 0
        for j in range(i):
            qa = np.dot(Q[:,j],A[:,i])
            sum += qa*Q[:,j]
            R[j,i] = qa
        u = A[:,i]-sum
        q = u/norm(u)
        Q[:,i] = q
        R[i,i] = norm(u)
    return (Q,R)

Q,R = decomposition(A)
QR = np.dot(Q,R)

print("b.)")
print("The original matrix A is")
print(A)
print("Multiplying Q and R results to")
print(QR)
print("A = QR, thus, the original matrix was recovered")


# In[119]:


I = np.identity(n)
error = 10e-6

for i in range(n):
    for j in range(i):
        if i != j:
            while abs(A[i,j]) > error:
                Q,R = decomposition(A)
                A = np.dot(R,Q)
                I = np.dot(I,Q)

print("c.)")
print("")
print("the eigenvalues are", np.diagonal(A))

