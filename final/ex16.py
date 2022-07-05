import cv2 
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt

mask1 = np.array([[0, 1, 0], [1, 1, 1], [0,1,0]])*(1/5)
mask2 = np.array([[1, 1, 1], [1, 1, 1], [1,1,1]])*(1/9)
mask3 = np.array([[1, 3, 1], [3, 16, 3], [1, 3, 1]])*(1/32)
mask4 = np.array([[0,1,0], [1,4,1], [0,1,0]])*(1/8)
img = cv2.imread("/content/drive/MyDrive/Classroom/2022_01/PROCESSAMENTO DIGITAL DE IMAGENS/EXAME/lena_ruido.bmp", 1)

def convolve2D(image, kernel, padding=0, strides=1):
    # Cross Correlation
    kernel = np.flipud(np.fliplr(kernel))

    # Gather Shapes of Kernel + Image + Padding
    xKernShape = kernel.shape[0]
    yKernShape = kernel.shape[1]
    xImgShape = image.shape[0]
    yImgShape = image.shape[1]

    # Shape of Output Convolution
    xOutput = int(((xImgShape - xKernShape + 2 * padding) / strides) + 1)
    yOutput = int(((yImgShape - yKernShape + 2 * padding) / strides) + 1)
    output = np.zeros((xOutput, yOutput))

    # Apply Equal Padding to All Sides
    if padding != 0:
        imagePadded = np.zeros((image.shape[0] + padding*2, image.shape[1] + padding*2))
        imagePadded[int(padding):int(-1 * padding), int(padding):int(-1 * padding)] = image
        print(imagePadded)
    else:
        imagePadded = image

    # Iterate through image
    for y in range(image.shape[1]):
        # Exit Convolution
        if y > image.shape[1] - yKernShape:
            break
        # Only Convolve if y has gone down by the specified Strides
        if y % strides == 0:
            for x in range(image.shape[0]):
                # Go to next row once kernel is out of bounds
                if x > image.shape[0] - xKernShape:
                    break
                try:
                    # Only Convolve if x has moved by the specified Strides
                    if x % strides == 0:
                        output[x, y] = (kernel * imagePadded[x: x + xKernShape, y: y + yKernShape]).sum()
                except:
                    break

    return output
print(mask1,'\n', mask2, mask3, mask4)
imgmask1 = convolve2D(img, mask1)
imgmask2 = convolve2D(img, mask2)
imgmask3 = convolve2D(img, mask3)
imgmask4 = convolve2D(img, mask4)
cv2.cvtColor(imgmask1, cv2.CV_8U)

# print(img)
plt.subplot(231),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(imgmask1),plt.title('Mascara 1')
plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.imshow(imgmask2),plt.title('Mascara 2')
plt.xticks([]), plt.yticks([])
plt.subplot(234),plt.imshow(imgmask3),plt.title('Mascara 3')
plt.xticks([]), plt.yticks([])
plt.subplot(235),plt.imshow(imgmask4),plt.title('Mascara 4')
plt.xticks([]), plt.yticks([])