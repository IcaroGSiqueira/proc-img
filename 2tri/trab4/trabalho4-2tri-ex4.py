import numpy as np
import cv2

img = cv2.imread('image.jpg', 0)
x, y = img.shape

new_img = np.zeros([x, y])

for i in range(1, x-1):
    for j in range(1, y-1):
        mat = [
                img[i-1, j-1],
                img[i-1, j],
                img[i-1, j+1],
                img[i, j-1],
                img[i, j],
                img[i, j+1],
                img[i+1, j-1],
                img[i+1, j],
                img[i+1, j+1]
                ]
        mat = sorted(mat)
        new_img[i, j]= mat[4]

new_img = new_img.astype(np.uint8)
cv2.imwrite('filterMediana.jpg', new_img)