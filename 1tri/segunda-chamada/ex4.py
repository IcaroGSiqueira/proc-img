import cv2
import math

img = cv2.imread('harpia.jpg', 0) 

# A

new_img = (0.5 * img) + 1

cv2.imwrite('filterHarpiaA.jpg', new_img)

# B

for i in range(len(img)):
    for j in range(len(img[0])):
        v = img[i][j]
        new_img[i][j] = (25 * math.log2(v+1))

cv2.imwrite('filterHarpiaB.jpg', new_img)

# C

for i in range(len(img)):
    for j in range(len(img[0])):
        v = img[i][j]
        new_img[i][j] = (5 * math.exp(v+1))

cv2.imwrite('filterHarpiaC.jpg', new_img)
