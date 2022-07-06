import cv2
import numpy as np
import matplotlib.pyplot as plt

def equalize(imagem, channel):
    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2YCrCb)
    imagem[:, :, channel] = cv2.equalizeHist(imagem[:, :, channel])
    equalized_img = cv2.cvtColor(imagem, cv2.COLOR_YCrCb2BGR)
    return equalized_img

def equalize_color(imagem):
    imagem[:, :, 0] = cv2.equalizeHist(imagem[:, :, 0])
    imagem[:, :, 1] = cv2.equalizeHist(imagem[:, :, 1])
    imagem[:, :, 2] = cv2.equalizeHist(imagem[:, :, 2])
    return imagem


img = cv2.imread("./orig_images/lena_gray.bmp", 1)
img2 = cv2.imread("./orig_images/lena_cor.bmp", 1)

a = equalize(img, 0)
cv2.imwrite('ex10/lena_gray_eq1.bmp', a)

c = equalize(a, 0)
cv2.imwrite('ex10/lena_gray_eq3.bmp', c)

d = img2.copy()
d = equalize_color(d)

cv2.imwrite('ex10/lena_gray_eq4.bmp', d)
