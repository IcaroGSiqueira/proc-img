import cv2 
from skimage.filters import sobel
from skimage.filters import prewitt
import matplotlib.pyplot as plt

img = cv2.imread("./orig_images/lena_gray.bmp", cv2.IMREAD_GRAYSCALE)

# A

prewitt = prewitt(img)

plt.imshow(prewitt, cmap=plt.cm.gray, interpolation='nearest')
plt.axis('off')
plt.savefig('ex19/lena_gray_prewitt.png', format='png', bbox_inches='tight')

# B

sobel = sobel(img)

plt.imshow(sobel, cmap=plt.cm.gray, interpolation='nearest')
plt.axis('off')
plt.savefig('ex19/lena_gray_sobel.png', format='png', bbox_inches='tight')

# C

plt.imshow(sobel - prewitt, cmap=plt.cm.gray, interpolation='nearest')
plt.axis('off')
plt.savefig('ex19/lena_gray_sobel-prewitt.png', format='png', bbox_inches='tight')