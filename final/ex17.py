import cv2 
import numpy as np

img = cv2.imread('lena_ruido.jpg', 0)

kernel = np.array([[1,0,1], [0,1,0], [1,0,1]])*1/2

new_img = img.copy()
padded_img = np.pad(new_img, pad_width=1, mode='constant', constant_values=127)
for i in range(1, len(padded_img)-1):
    for j in range(1, len(padded_img[0])-1):
        new_img[i-1][j-1] = np.sum([
            padded_img[i-1][j-1] * kernel[0][0],
            padded_img[i-1][j] * kernel[0][1],
            padded_img[i-1][j+1] * kernel[0][2],
            padded_img[i][j-1] * kernel[1][0],
            padded_img[i][j] * kernel[1][1],
            padded_img[i][j+1] * kernel[1][2],
            padded_img[i+1][j-1] * kernel[2][0],
            padded_img[i+1][j] * kernel[2][1],
            padded_img[i+1][j+1] * kernel[2][2]
            ])

cv2.imwrite('ex17/lena_ruido_blur.jpg', new_img) 