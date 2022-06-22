import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
from vcam import vcam,meshGen
import PIL

img = cv2.imread('/home/icaro/Pictures/EfzSNEKWoAI-Xbr.jpeg')
img2 = PIL.Image.open('/home/icaro/Pictures/EfzSNEKWoAI-Xbr.jpeg')

print(img)
print(img2)
# rows, cols, depts = img.shape

# #####################
# # Vertical wave

# img_output = np.zeros(img.shape, dtype=img.dtype)

# for i in range(rows):
#     for j in range(cols):
#         offset_x = int(25.0 * math.sin(100*3.14 * i / 180))
#         offset_y = 0
#         if j+offset_x < rows:
#             img_output[i,j] = img[i,(j+offset_x)%cols]
#         else:
#             img_output[i,j] = 0

# plt.subplot(121),plt.imshow(img),plt.title('Input')
# plt.subplot(122),plt.imshow(img_output),plt.title('Output')
# plt.show()


# Reading the input image. Pass the path of image you would like to use as input image.
# img = cv2.imread("/content/sample_data/download.jpg")
H,W = img.shape[:2]

# Creating the virtual camera object
c1 = vcam(H=H,W=W)

# Creating the surface object
plane = meshGen(H,W)

# plt.plot(img)
cv2.imshow('original', img)

for mode in range(8):
  if mode == 0:
    plane.Z += 20*np.exp(-0.5*((plane.X*1.0/plane.W)/0.1)**2)/(0.1*np.sqrt(2*np.pi))
  elif mode == 1:
    plane.Z += 20*np.exp(-0.5*((plane.Y*1.0/plane.H)/0.1)**2)/(0.1*np.sqrt(2*np.pi))
  elif mode == 2:
    plane.Z -= 10*np.exp(-0.5*((plane.X*1.0/plane.W)/0.1)**2)/(0.1*np.sqrt(2*np.pi))
  elif mode == 3:
    plane.Z -= 10*np.exp(-0.5*((plane.Y*1.0/plane.W)/0.1)**2)/(0.1*np.sqrt(2*np.pi))
  elif mode == 4:
    plane.Z += 20*np.sin(2*np.pi*((plane.X-plane.W/4.0)/plane.W)) + 20*np.sin(2*np.pi*((plane.Y-plane.H/4.0)/plane.H))
  elif mode == 5:
    plane.Z -= 20*np.sin(2*np.pi*((plane.X-plane.W/4.0)/plane.W)) - 20*np.sin(2*np.pi*((plane.Y-plane.H/4.0)/plane.H))
  elif mode == 6:
    plane.Z += 100*np.sqrt((plane.X*1.0/plane.W)**2+(plane.Y*1.0/plane.H)**2)
  elif mode == 7:
    plane.Z -= 100*np.sqrt((plane.X*1.0/plane.W)**2+(plane.Y*1.0/plane.H)**2)
  pts3d = plane.getPlane()

  # Projecting / capturing the 3D points using the virtual camera
  pts2d = c1.project(pts3d)
  map_x,map_y = c1.getMaps(pts2d)

  output = cv2.remap(img,map_x,map_y,interpolation=cv2.INTER_LINEAR)

  print(" ")
  # cv2_imshow(np.hstack((img,output)))
  # plt.plot(output)
  cv2.imshow('saida', output)
