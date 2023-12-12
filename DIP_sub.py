import cv2
import numpy as np

img1 = cv2.imread('remove_blue.png')
img2 = cv2.imread('add_img.jpg')

res = cv2.subtract(img1, img2)

cv2.imwrite('sub_img.jpg', res)
