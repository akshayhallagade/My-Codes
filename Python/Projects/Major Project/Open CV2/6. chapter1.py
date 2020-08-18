# joining image
import cv2
import numpy as np

img = cv2.imread("images/cards.jpg")
imgHor = np.hstack((img, img, img))
cv2.imshow("Img output", imgHor)
cv2.waitKey(0)
