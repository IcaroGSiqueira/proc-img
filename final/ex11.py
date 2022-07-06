import cv2
import numpy as np
from skimage import exposure
import matplotlib.pyplot as plt

img = cv2.imread("./orig_images/image1.png", 1)
img_gray = cv2.imread("./orig_images/lena_gray.bmp", 1)

multi = True if img.shape[-1] > 1 else False
matched = exposure.match_histograms(img, img_gray, multichannel=multi)

cv2.imwrite('ex11/img1_match_lena.bmp', matched)
