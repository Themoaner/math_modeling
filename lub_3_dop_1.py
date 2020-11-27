import numpy as np 
M=int(input( ))
N=int(input( ))

A = np.zeros((N, M))
for i in range (N):
  for j in range (M):
    A[i][j] = int(input( ))

B = np.zeros((N, M))
for i in range (N):
  for j in range (M):
    B[i][j] = int(input( ))

C = np.zeros((N, M))
for i in range (N):
  for j in range (M):
    if A[i][j] > B[i][j]:
     C[i][j] = A[i][j]
    else:
      C[i][j] = B[i][j]

print(A)
print(B)
print(C)
