import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./lena_gray.bmp")

elem = img.mean(axis=2)
cont, bina = np.histogram(elem, range(255))

# A
plt.bar(bina[1:], cont)
plt.xlim([0, 255])
plt.show()


# B
plt.hist(cont)
plt.show()


# C
cdf = np.cumsum(cont / sum(cont))

plt.plot(bina[1:], cdf)
plt.show()
