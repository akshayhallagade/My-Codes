# reading the images and showing them.
import cv2
print("Package imported.")
img = cv2.imread("images/example_01.jpg")
cv2.imshow("output", img)
cv2.waitKey(0)
