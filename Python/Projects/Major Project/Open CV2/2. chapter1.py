import cv2
import numpy as np

img = cv2.imread("images/example_01.jpg")
kernel = np.ones((5, 5), np.uint8)

# to make B&W (Black and White).
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# to make BLUR.
imgBlur = cv2.GaussianBlur(imgGray, (25, 25), 0)
# to make draw outline of the image.
imgCanny = cv2.Canny(img, 100, 100)
# to increase the width of outline of the image.
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
# to decrese the width of outline of image.
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDilation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)
