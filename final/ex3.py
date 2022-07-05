import cv2 
import numpy as np

img = cv2.imread("./lena_cor.bmp")

img_gray = img.copy()

for i in range(len(img)):
    for j in range(len(img[0])):
        img_gray[i][j] = int(np.mean(img_gray[i][j]))


cv2.imwrite('ex3/lena_cor_to_gray.bmp', img_gray)
