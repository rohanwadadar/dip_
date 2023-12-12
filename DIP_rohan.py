
import cv2
from matplotlib import pyplot as plt


test_gray_image = cv2.imread('jose-g-ortega-castro-UGAyT0Xll0k-unsplash.jpg', cv2.IMREAD_GRAYSCALE)
thresh = 100
img_binary = cv2.threshold(test_gray_image, thresh, 255, cv2.THRESH_BINARY)[1]
histg = cv2.calcHist([test_gray_image],[0],None,[256],[0,256])
rot_img = cv2.rotate(test_gray_image, cv2.ROTATE_90_COUNTERCLOCKWISE)


(height, width) = test_gray_image.shape[:2]
center = (width/2, height/2)
angle = 45
scale = 1.0
matrix = cv2.getRotationMatrix2D(center, angle, scale)
rotated_by_matrix = cv2.warpAffine(test_gray_image, matrix, (width, height))




# mismatch due to imshow here called from matplotlib, not form opencv
plt.subplot(3,4,1)
plt.imshow(test_gray_image, cmap='gray')
plt.subplot(3,4,3)
plt.imshow(img_binary, cmap='gray')



plt.subplot(3,4,4)        
plt.imshow(rot_img, cmap='gray')


plt.subplot(3,4,6)
plt.plot(histg)




plt.subplot(3,4,8)  
plt.imshow(rotated_by_matrix, cmap='gray')




plt.show()
