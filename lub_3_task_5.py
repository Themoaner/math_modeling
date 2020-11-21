import numpy as np
from numpy import sin
N = int(input( ))
M = int(input( ))
A = np.zeros((N,M))
for i in range(N):
  for j in range(M):
    if i == 0 and j == 0:
      A[i][j] = sin(N*(i+1) + M*(j+1))
    else:
      A[i, j] = sin(N * i + M * j)
    if A[i][j] < 0:
      A[i][j] = 0 
print(A)
C = np.zeros(N)
d= int(input())
e= int(input())
for i in range(N):
  C[i] = A[i][d-1]
  A[i][d-1] = A[i][e-1]
  A[i][e-1] = C[i]
print(A)