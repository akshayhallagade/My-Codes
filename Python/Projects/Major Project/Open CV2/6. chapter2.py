# joining image
import cv2
import numpy as np

img = cv2.imread("images/example_02.jpg")
imgVer = np.vstack((img, img, img))
cv2.imshow("Img output", imgVer)
cv2.waitKey(0)
