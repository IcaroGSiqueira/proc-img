import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.filters import sobel

img = np.array([
    [15, 18, 13, 16, 20],
    [30, 37, 40, 32, 28],
    [16, 10, 15, 18, 14],
    [70, 77, 66, 55, 60],
    ])

op_sobel = sobel(img)

print(op_sobel)