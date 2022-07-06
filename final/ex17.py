import cv2 
import numpy as np

img = cv2.imread('./orig_images/lena_ruido.jpg', 0)

median = cv2.medianBlur(img,3) # De acordo com o valor digitado obtemos diferentes resultados.

cv2.imwrite('ex17/lena_ruido_blur.jpg', median)