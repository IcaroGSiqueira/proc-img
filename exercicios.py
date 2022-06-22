import numpy as np

entrada1 = [[5, 8, 9], [2, 0, 9], [5, 4, 2], [2, 3, 9]] 

entrada2 = [[5, 8], [2, 0], [5, 4]]

saida1 = dict(zip(entrada1[0], entrada1[1:]))

saida2 = dict(zip(entrada2[0], entrada2[1:]))

print('\nEx 2.1:\n', saida1)
print('\nEx 2.2:\n', saida2)

A = [[1, 2], [3, 4]]
B = [[4, 5], [6, 7]]

R = [[0, 0], [0, 0]]
 
for i in range(len(A)):  
    for j in range(len(B[0])):
        R[i][j] = A[i][j] + B[i][j]

print('\nEx 3:\n', R)

A = [[1, 2], [3, 4]]
B = [[4, 5], [6, 7]]

R = [[0, 0], [0, 0]]
 
for i in range(len(A)):  
    for j in range(len(B[0])):
        R[i][j] = A[i][j] - B[i][j]

print('\nEx 4:\n', R)

N = 5

M = np.zeros((N, N), dtype=int)

k = 1

for i in range(len(M)):
    for j in range(len(M[0])):
        M[i][j] = k
        k+=1

if(N % 2 == 0):
    for i in range(len(M)):
        if(i % 2 == 1):
            x = 0
            y = N - 1

            while(x < y):
                buff = M[i][x]
                M[i][x] = M[i][y]
                M[i][y] = buff
                x+=1
                y-=1

print('\nEx 5:')
print(M)
