import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.filters import roberts

################ ROBERT ################

img = cv2.imread("image2.jpg", cv2.IMREAD_GRAYSCALE)
op_roberts = roberts(img)

plt.imshow(op_roberts, cmap=plt.cm.gray)
plt.savefig('filterRoberts.jpg', format='jpg')

################ LAPLACE ################

img = cv2.imread('image2.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
lap = cv2.Laplacian(img, cv2.CV_64F)

img_new = np.vstack([lap])

cv2.imwrite('filterLaplace.jpg', img_new)
