# Cropping the size if the image.
import cv2

img = cv2.imread("images/example_02.jpg")
croppingImg = img[150:240, 150:360]
# cropping the image and putting it in varible croppingImg.

print(img.shape)
print(croppingImg.shape)
# size of cropped image.

cv2.imshow("output", img)
cv2.imshow("Cropped Output", croppingImg)  # showing resized image.
cv2.waitKey(0)
