import cv2 
import numpy as np

img = cv2.imread('lena_ruido.jpg', 1)

kernel = np.array([[1/9,1/9,1/9], [1/9,1/9,1/9], [1/9,1/9,1/9]])

new_img = img.copy()

for i in range(1, len(img)-1):
    for j in range(1, len(img[0])-1):
        new_img[i][j] = np.mean([
            img[i-1][j-1] * kernel[0][0],
            img[i-1][j] * kernel[0][1],
            img[i-1][j+1] * kernel[0][2],
            img[i][j-1] * kernel[1][0],
            img[i][j] * kernel[1][1],
            img[i][j+1] * kernel[1][2],
            img[i+1][j-1] * kernel[2][0],
            img[i+1][j] * kernel[2][1],
            img[i+1][j+1] * kernel[2][2]
            ])

cv2.imwrite('ex17/lena_ruido_blur.jpg', new_img) 