import cv2 
import numpy as np 

import matplotlib.pyplot as plt

from PIL import Image, ImageFilter    

from skimage.io import imread
from skimage.filters import roberts
from skimage.filters import sobel
from skimage.filters import prewitt

################ MEDIA ################

img = cv2.imread('harpia.jpg', 0) 
x, y = img.shape 
   
mask = np.ones([3, 3], dtype = int) 
mask = mask / 9
   
new_img = np.zeros([x, y]) 
  
for i in range(1, x-1): 
    for j in range(1, y-1): 
        temp = (
            img[i-1, j-1]*mask[0, 0]+
            img[i-1, j]*mask[0, 1]+
            img[i-1, j + 1]*mask[0, 2]+
            img[i, j-1]*mask[1, 0]+
            img[i, j]*mask[1, 1]+
            img[i, j + 1]*mask[1, 2]+
            img[i + 1, j-1]*mask[2, 0]+
            img[i + 1, j]*mask[2, 1]+
            img[i + 1, j + 1]*mask[2, 2]
            )

        new_img[i, j]=temp
          
new_img = new_img.astype(np.uint8) 
cv2.imwrite('filterMedia.jpg', new_img)

################ MEDIANA ################

img = cv2.imread('harpia.jpg', 0) 
x, y = img.shape 
   
new_img = np.zeros([x, y]) 
  
for i in range(1, x-1): 
    for j in range(1, y-1): 
        mat = [img[i-1, j-1],  
               img[i-1, j], 
               img[i-1, j + 1], 
               img[i, j-1], 
               img[i, j], 
               img[i, j + 1], 
               img[i + 1, j-1], 
               img[i + 1, j], 
               img[i + 1, j + 1]] 
        mat = sorted(mat) 
        new_img[i, j]= mat[4] 
  
new_img = new_img.astype(np.uint8) 
cv2.imwrite('filterMediana.jpg', new_img) 

################ MODA ################

image = Image.open('harpia.jpg')

image = image.filter(ImageFilter.ModeFilter)

image.save("filterModa.jpg")

################ ROBERT ################

img = cv2.imread("harpia.jpg", cv2.IMREAD_GRAYSCALE)
op_roberts = roberts(img)

plt.imshow(op_roberts, cmap=plt.cm.gray)
plt.savefig('filterRoberts.jpg', format='jpg')

################ SOBEL ################

img = cv2.imread("harpia.jpg", cv2.IMREAD_GRAYSCALE)
op_sobel = sobel(img)

plt.imshow(op_sobel, cmap=plt.cm.gray)
plt.savefig('filterSobel.jpg', format='jpg')

################ NEGATIVO ################

img = cv2.imread('harpia.jpg', 1) 
x, y, _ = img.shape 

for i in range(0, x-1): 
    for j in range(0, y-1): 
        
        temp = img[i, j] 
        temp[0] = 255 - temp[0] 
        temp[1] = 255 - temp[1] 
        temp[2] = 255 - temp[2] 
        img[i, j] = temp 

img = img.astype(np.uint8) 
cv2.imwrite('filterNegativo.jpg', img) 

################ GAUSSIANO ################

image = Image.open('harpia.jpg')

image = image.filter(ImageFilter.GaussianBlur)

image.save("filterGaussiano.jpg")

################ LAPLACE ################

image = Image.open('harpia.jpg')

image = image.convert("L")

image = image.filter(
    ImageFilter.Kernel(
        (3, 3),
        (-1, -1, -1, -1, 8, -1, -1, -1, -1),
    1, 0)
)
  
image.save("filterLaplace.jpg")

################ PREWITT ################

img = cv2.imread("harpia.jpg", cv2.IMREAD_GRAYSCALE)
op_prewitt = prewitt(img)

plt.imshow(op_prewitt, cmap=plt.cm.gray)
plt.savefig('filterPrewitt.jpg', format='jpg')

################ BINÁRIO ################

img = cv2.imread('harpia.jpg', cv2.IMREAD_GRAYSCALE) 
  
ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) 
bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) 
  
cv2.imwrite('filterBinario.jpg', bw_img) 

################ BINARIO INV, ################

img = cv2.imread('harpia.jpg', cv2.IMREAD_GRAYSCALE)
  
ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV) 
bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV) 
  
cv2.imwrite('filterBinarioInv.jpg', bw_img) 

################ TRUNC ################

img = cv2.imread("harpia.jpg", cv2.IMREAD_GRAYSCALE)
thresh = 127
max_value = 255
th, dst = cv2.threshold(img, thresh, max_value, cv2.THRESH_TRUNC)

cv2.imwrite('filterTrunc.jpg', dst)

################ TOZERO ################

img = cv2.imread("harpia.jpg", cv2.IMREAD_GRAYSCALE)
thresh = 127
max_value = 255
th, dst = cv2.threshold(img, thresh, max_value, cv2.THRESH_TOZERO)

cv2.imwrite('filterTozero.jpg', dst) 

################ TOZERO INV. ################

img = cv2.imread("harpia.jpg", cv2.IMREAD_GRAYSCALE)
thresh = 127
max_value = 255
th, dst = cv2.threshold(img, thresh, max_value, cv2.THRESH_TOZERO_INV)

cv2.imwrite('filterTozeroInv.jpg', dst) 

################ SHARP ################

img = cv2.imread('harpia.jpg', 1)

kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
new_img = cv2.filter2D(img, -1, kernel)
cv2.imwrite('filterSharp.jpg', new_img) 

################ NORMALIZANDO DUAS IMAGENS ################
    ################ SHARP ################

img = cv2.imread("filterSharp.jpg")
new_img = cv2.normalize(img, None, alpha=0,beta=200, norm_type=cv2.NORM_MINMAX)

new_img = new_img.astype(np.uint8) 
cv2.imwrite('normalizedFilterSharp.jpg', new_img) 

    ################ GAUSSIANO ################

img = cv2.imread("filterGaussiano.jpg")
new_img = cv2.normalize(img, None, alpha=0,beta=200, norm_type=cv2.NORM_MINMAX)

new_img = new_img.astype(np.uint8) 
cv2.imwrite('normalizedFilterGaussiano.jpg', new_img) 
