import cv2
from matplotlib import pyplot as plt
import numpy as np




sample = cv2.imread('jose-g-ortega-castro-UGAyT0Xll0k-unsplash.jpg')
# to split call split method

blue, green, red = cv2.split(sample)


zeros = np.zeros(blue.shape, np.uint8)
blue_BGR = cv2.merge((blue, zeros, zeros))
green_BGR = cv2.merge((zeros, green, zeros))
red_BGR = cv2.merge((zeros, zeros, red))
remove_blue= cv2.merge((zeros, green, red))
remove_red= cv2.merge((blue, green, zeros))
remove_green = cv2.merge((blue, zeros, red))
cv2.imwrite('blue.png', blue_BGR)
cv2.imwrite('green.png', green_BGR)
cv2.imwrite('red.png', red_BGR)
cv2.imwrite('remove_blue.png', remove_blue)
cv2.imwrite('remove_red.png', remove_red)
cv2.imwrite('remove_green.png', remove_green)

plt.subplot(2,4,1)
plt.imshow(blue_BGR)
plt.subplot(2,4,2)
plt.imshow(green_BGR)
plt.subplot(2,4,3)
plt.imshow(red_BGR)
plt.subplot(2,4,4)
plt.imshow(remove_blue)
plt.subplot(2,4,5)
plt.imshow(remove_red)
plt.subplot(2,4,6)
plt.imshow(remove_green)
plt.show()
