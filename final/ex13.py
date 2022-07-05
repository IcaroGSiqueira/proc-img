import cv2 
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt

img = cv2.imread("./forma1.png", 1)
img2 = cv2.imread("./forma2.png", 1)

cv2.imwrite('ex13/forma1&forma2.bmp', img&img2)
cv2.imwrite('ex13/forma1|forma2.bmp', img|img2)
cv2.imwrite('ex13/forma1!forma2.bmp', cv2.bitwise_xor(img,img2))
cv2.imwrite('ex13/!forma1.bmp', cv2.bitwise_not(img))
cv2.imwrite('ex13/!forma2.bmp', cv2.bitwise_not(img2))
