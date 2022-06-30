import numpy as np

A = [[ 1, 0, 2, 0], 
     [ 2, 1, 1, 1], 
     [ 2, 3, 0, 1], 
     [-1, 1, 2, 2]]

D = [[3,  1, -2, 1],
     [5,  2,  2, 3], 
     [7,  4, -5, 0], 
     [1, -1, 11, 2]]

H = len(A)
W = len(A[0])

# A

sum_m = np.empty((H, W))

for i in range(H):
    for j in range(W):
        sum_m[i][j] = A[i][j] + D[i][j] 

print ("A + D:\n",sum_m)

# B 

sub_m = np.empty((H, W))

for i in range(H):
    for j in range(W):
        sub_m[i][j] = A[i][j] - D[i][j] 

print ("\nA - D:\n",sub_m)

# C 

tA = np.empty((H, W))

for i in range(H):
    for j in range(W):
        tA[i][j] = A[j][i]

print ("\nA transposta:\n",tA)

# D

tD = np.empty((H, W))

for i in range(H):
    for j in range(W):
        tD[i][j] = D[j][i]

print ("\nD transposta:\n",tD)
