import cv2 

img = cv2.imread("./orig_images/lena_gray.bmp", 0)

# A

laplacian = cv2.Laplacian(img, cv2.CV_64F, -1)

cv2.imwrite('ex18/lena_gray_laplace.bmp', laplacian)

# B

gaussian = cv2.GaussianBlur(img, (0, 0), 2.0)
unsharp_masking = cv2.addWeighted(img, 2.0, gaussian, -1.0, 0)

cv2.imwrite('ex18/lena_gray_unsharp.bmp', unsharp_masking)

# C

def highBoostFiltering(image,boost_factor):
    resultant_image = image.copy()
    for i in range(1,image.shape[0]-1):
        for j in range(1,image.shape[1]-1):
            blur_factor = ( image[i-1, j-1] + image[i-1, j] -
                            image[i-1, j+1] + image[i, j-1] +
                            image[i, j]     + image[i, j+1] +
                            image[i+1, j+1] + image[i+1, j] +
                            image[i+1, j+1])/ 9

            mask = boost_factor*image[i, j] - blur_factor
            resultant_image[i, j] = image[i, j] + mask

    return resultant_image

cv2.imwrite('ex18/lena_gray_highboost.bmp', highBoostFiltering(img,1/9))
