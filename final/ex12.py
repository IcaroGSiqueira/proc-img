import cv2 

img = cv2.imread("./orig_images/cena1.png", 0)

img2 = cv2.imread("./orig_images/cena2.png", 0)

# A

img2_1 = img2 - img

cv2.imwrite('ex12/cena2-1.bmp', img2_1)

# B e C

dummy, img_bina = cv2.threshold(img2_1, 125, 255, cv2.THRESH_BINARY)

cv2.imwrite('ex12/cena2-1_limiar.bmp', img_bina)

# D

img2_1_lim = img2_1.copy()

for i in range(len(img)):
    for j in range(len(img[0])):
        if (img2_1[i][j] < 150 and img2_1[i][j] > 20):
            img2_1_lim[i][j] = 255

cv2.imwrite('ex12/cena2-1_white.bmp', img2_1_lim)
