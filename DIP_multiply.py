import cv2
import numpy as np

# two images need to be of same size
img1 = cv2.imread('remove_blue.png')
img2 = cv2.imread('remove_red.png')

res = cv2.multiply(img1, img2)

cv2.imwrite('mul_img.jpg', res)
