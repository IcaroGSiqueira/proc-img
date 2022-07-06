import cv2 
import numpy as np

def mse(imgA, imgB):
    err = np.sum((imgA.astype("float") - imgB.astype("float")) ** 2)
    err /= float(imgA.shape[0] * imgA.shape[1])
    return err

img = cv2.imread('./orig_images/folha.png', 0)

img_borda_adj4 = img.copy()
img_borda_adj8 = img.copy()

for i in range(1, len(img)-1):
    for j in range(1, len(img[0])-1):
        if (not(
            img[i+1][j+1] ==
            img[i-1][j+1] ==
            img[i+1][j-1] ==
            img[i-1][j-1]
            )):
            img_borda_adj4[i][j] = 0
        else:
            img_borda_adj4[i][j] = 255

        if (not(
            img[i+1][j+1] ==
            img[i-1][j+1] ==
            img[i][j+1] ==
            img[i-1][j-1] ==
            img[i+1][j-1] ==
            img[i][j-1] ==
            img[i+1][j] ==
            img[i-1][j]
            )):
            img_borda_adj8[i][j] = 0
        else:
            img_borda_adj8[i][j] = 255

cv2.imwrite('ex6/folha_borda_adj4.jpg', img_borda_adj4)

cv2.imwrite('ex6/folha_borda_adj8.jpg', img_borda_adj8)

print(mse(img_borda_adj4, img_borda_adj8))
