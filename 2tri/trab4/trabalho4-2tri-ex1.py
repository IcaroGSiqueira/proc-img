import cv2 
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter    

################ GAUSSIANO ################

image = Image.open('image.jpg')

image = image.filter(ImageFilter.GaussianBlur)

image.save("filterGaussiano.jpg")

################ BILATERAL ################

img = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

op_bilateral = cv2.bilateralFilter(img,9,75,75)

plt.imshow(op_bilateral)#, cmap=plt.cm.viridis)
plt.savefig('filterBilateral.jpg', format='jpg')

