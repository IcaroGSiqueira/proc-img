import cv2 
import numpy as np
from scipy import ndimage

roberts_vert = np.array([
                        [1, 0],
                        [0,-1],
                        ])
 
roberts_horz = np.array([
                        [ 0, 1],
                        [-1, 0],
                        ])

x = np.array([
                [15, 18, 13, 16, 20],
                [30, 37, 40, 32, 28],
                [16, 10, 15, 18, 14],
                [70, 77, 66, 55, 60],
            ])

vert = ndimage.convolve( x, roberts_vert )
horz = ndimage.convolve( x, roberts_horz )

z = np.sqrt( np.square(horz) + np.square(vert))

# plota imagens lado a lado para comparação
cv2.imwrite('ex1/orig_img.bmp', x)
cv2.imwrite('ex1/filt_img.bmp', z)
