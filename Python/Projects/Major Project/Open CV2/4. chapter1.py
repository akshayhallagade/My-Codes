# creating blank image with using arrays.
import cv2
import numpy as np

# creating image with zeroes. It is a greyscale img.
# np.zeroes creates the array of the zeroes.
img = np.zeros((512, 512, 3), np.uint8)
print(img)  # printing that array of the image.

# coloring the image.
# 255,0,0 is the blue color.
# [150:190, 150:210] it denotes the part of image.
img[150:190, 150:210] = 255, 0, 0

cv2.imshow("image", img)
cv2.waitKey(0)
