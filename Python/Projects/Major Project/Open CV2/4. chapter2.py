# creating shapes and Text on the image
import cv2
import numpy as np

# creating image with zeroes. It is a greyscale img.
# np.zeroes creates the array of the zeroes.
img = np.zeros((512, 512, 3), np.uint8)

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
# cv2.line(img,p1=from,p2=upto,colors,thickness)
cv2.rectangle(img, (0, 0), (350, 350), (0, 0, 255), 3)
# cv2.rectangle(img,p1=from,p2=upto,colors,thickness)
cv2.circle(img, (0, 0), 495, (255, 0, 0), 2)
# cv2.circle(img,p1=center,radius,color,thickness)
cv2.putText(img, "Akshay", (100, 100),
            cv2.FONT_HERSHEY_PLAIN, 4, (0, 255, 0), 2)
# cv2.putText(img, "text",p1=from point, fontstyle,fontsize,color,thickness)

cv2.imshow("image", img)
cv2.waitKey(0)
