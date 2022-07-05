import cv2 
import numpy as np

img = cv2.imread('./orig_images/folha.png', 0)

new_img = img.copy()

for i in range(1, len(img)-1):
    for j in range(1, len(img[0])-1):
        if (not(img[i+1][j+1] == img[i-1][j+1] == img[i+1][j-1] == img[i-1][j-1])):
            new_img[i][j] = 0
        else:
            new_img[i][j] = 255

cv2.imwrite('ex6/folha_borda.jpg', new_img)