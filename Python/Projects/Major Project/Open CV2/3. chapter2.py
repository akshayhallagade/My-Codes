# Changing the size if the image.
import cv2

img = cv2.imread("images/example_01.jpg")
resizeImg = cv2.resize(img, (300, 300))
# finding the size of the image)
print(resizeImg.shape)
# prints the size of the resized image.

cv2.imshow("Output", img)  # showing image.
cv2.imshow("ResizeOutputn", resizeImg)  # showing resized image.
cv2.waitKey(0)
