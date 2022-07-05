import cv2 
import numpy as np

def conv(img, mask):
    new_img = img.copy()
    padded_img = np.pad(new_img, pad_width=1, mode='constant', constant_values=127)
    for i in range(1, len(padded_img)-1):
        for j in range(1, len(padded_img[0])-1):
            new_img[i-1][j-1] = np.sum([
                padded_img[i-1][j-1] * mask[0][0],
                padded_img[i-1][j] * mask[0][1],
                padded_img[i-1][j+1] * mask[0][2],
                padded_img[i][j-1] * mask[1][0],
                padded_img[i][j] * mask[1][1],
                padded_img[i][j+1] * mask[1][2],
                padded_img[i+1][j-1] * mask[2][0],
                padded_img[i+1][j] * mask[2][1],
                padded_img[i+1][j+1] * mask[2][2]
                ])
    return new_img

img = cv2.imread('lena_ruido.jpg', 0)

kernel1 = np.array([[0,1,0], [1,1,1], [0,1,0]]) * (1/5)
kernel2 = np.array([[1,1,1], [1,1,1], [1,1,1]]) * (1/9)
kernel3 = np.array([[1,3,1], [3,16,3], [1,3,1]]) * (1/32)
kernel4 = np.array([[0,1,0], [1,4,1], [0,1,0]]) * (1/8)


cv2.imwrite('ex16/lena_ruido_mask1.jpg', conv(img, kernel1))
cv2.imwrite('ex16/lena_ruido_mask2.jpg', conv(img, kernel2))
cv2.imwrite('ex16/lena_ruido_mask3.jpg', conv(img, kernel3))
cv2.imwrite('ex16/lena_ruido_mask4.jpg', conv(img, kernel4))