import cv2
import numpy as np
import matplotlib.pyplot as plt

def hist(image, size):
    hist = np.zeros(size)
    
    for coord in image:
        hist[coord] += 1
    
    return hist

def cumHist(hist):
    hist = iter(hist)
    v = [next(hist)]
    for i in hist:
        v.append(v[-1] + i)
    return np.array(v)

def normaHist(hist):
  ch = cumHist(hist)

  nh = (ch - ch.min()) * 255
  N = ch.max() - ch.min()

  ch = nh / N

  ch = ch.astype('uint8')

  return ch

img = cv2.imread("./orig_images/lena_gray.bmp", 0)

# A

hist = hist(img, len(img))
plt.plot(hist)
plt.show()

# B

norm = normaHist(hist)
plt.plot(norm)
plt.show()

#C

ch = cumHist(hist)
plt.plot(ch)
plt.show()
