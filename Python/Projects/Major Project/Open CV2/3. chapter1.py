# finding the size if the image.
import cv2

img = cv2.imread("images/example_01.jpg")
print(img.shape)  # prints the size of the image.

cv2.imshow("Output", img)
cv2.waitKey(0)
