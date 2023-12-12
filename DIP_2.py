import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('remove_blue.png')
img2 = cv2.imread('remove_red.png')
dst = cv2.addWeighted(img1,0.7, img2, 0.4, 0)
cv2.imwrite('add_img.jpg', dst)
 
plt.subplot(2,2,1)

cv2.imshow('add_img.jpg', dst)
