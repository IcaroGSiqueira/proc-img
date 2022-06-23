import numpy as np
import cv2

X = np.array([
    [15, 18, 13, 16, 20],
    [30, 37, 40, 32, 28],
    [16, 10, 15, 18, 14],
    [70, 77, 66, 55, 60],
    ])

x, y = X.shape 
   
mask = np.ones([3, 3], dtype = int) 
mask = mask / 9
   
Z = np.zeros([x, y]) 
  
for i in range(1, x-1): 
    for j in range(1, y-1): 
        temp = (
            X[i-1, j-1]*mask[0, 0]+
            X[i-1, j]*mask[0, 1]+
            X[i-1, j + 1]*mask[0, 2]+
            X[i, j-1]*mask[1, 0]+
            X[i, j]*mask[1, 1]+
            X[i, j + 1]*mask[1, 2]+
            X[i + 1, j-1]*mask[2, 0]+
            X[i + 1, j]*mask[2, 1]+
            X[i + 1, j + 1]*mask[2, 2]
            )

        Z[i, j]=temp
          
Z = Z.astype(np.uint8) 

print(np.matrix(Z))

