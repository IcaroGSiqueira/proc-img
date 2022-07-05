import cv2 

img = cv2.imread("./orig_images/lena_cor.bmp")

img_gray = cv2.imread("./orig_images/lena_gray.bmp", 0)

img7b = img.copy()
img6b = img.copy()
img5b = img.copy()
img4b = img.copy()
img3b = img.copy()
img2b = img.copy()
img1b = img.copy()

img_gray7b = img_gray.copy()
img_gray6b = img_gray.copy()
img_gray5b = img_gray.copy()
img_gray4b = img_gray.copy()
img_gray3b = img_gray.copy()
img_gray2b = img_gray.copy()
img_gray1b = img_gray.copy()

for i in range(len(img)):
    for j in range(len(img[0])):
        for k in range(len(img[0][0])):
            img7b[i][j][k] = int(img7b[i][j][k]/2)*2
            img6b[i][j][k] = int(img6b[i][j][k]/4)*4
            img5b[i][j][k] = int(img5b[i][j][k]/8)*8
            img4b[i][j][k] = int(img4b[i][j][k]/16)*16
            img3b[i][j][k] = int(img3b[i][j][k]/32)*32
            img2b[i][j][k] = int(img2b[i][j][k]/64)*64
            img1b[i][j][k] = int(img1b[i][j][k]/128)*128

        img_gray7b[i][j] = int(img_gray7b[i][j]/2)*2
        img_gray6b[i][j] = int(img_gray6b[i][j]/4)*4
        img_gray5b[i][j] = int(img_gray5b[i][j]/8)*8
        img_gray4b[i][j] = int(img_gray4b[i][j]/16)*16
        img_gray3b[i][j] = int(img_gray3b[i][j]/32)*32
        img_gray2b[i][j] = int(img_gray2b[i][j]/64)*64
        img_gray1b[i][j] = int(img_gray1b[i][j]/128)*128

cv2.imwrite('ex4/lena_cor_1bit.bmp', img1b)
cv2.imwrite('ex4/lena_cor_2bit.bmp', img2b)
cv2.imwrite('ex4/lena_cor_3bit.bmp', img3b)
cv2.imwrite('ex4/lena_cor_4bit.bmp', img4b)
cv2.imwrite('ex4/lena_cor_5bit.bmp', img5b)
cv2.imwrite('ex4/lena_cor_6bit.bmp', img6b)
cv2.imwrite('ex4/lena_cor_7bit.bmp', img7b)

cv2.imwrite('ex4/lena_gray_1bit.bmp', img_gray1b)
cv2.imwrite('ex4/lena_gray_2bit.bmp', img_gray2b)
cv2.imwrite('ex4/lena_gray_3bit.bmp', img_gray3b)
cv2.imwrite('ex4/lena_gray_4bit.bmp', img_gray4b)
cv2.imwrite('ex4/lena_gray_5bit.bmp', img_gray5b)
cv2.imwrite('ex4/lena_gray_6bit.bmp', img_gray6b)
cv2.imwrite('ex4/lena_gray_7bit.bmp', img_gray7b)