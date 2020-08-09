# warp prespective of a object in the image
import cv2
import numpy as np

img = cv2.imread("images/cards.jpg")
width, height = 320, 450

pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
# creating pts1 and pts2 parameters of the matrix.
matrix = cv2.getPerspectiveTransform(pts1, pts2)
# creating prespective.
# perspective takaes out points of the desired object, from where it get cuts from the image and also
# takes the desired pts2 which is points where we have to put our images.
imgOutput = cv2.warpPerspective(img, matrix, (width, height))
# creating warp prespective.
# It takes which image to edit the, (matrix) in the way to cut it, and width and height of the image.

cv2.imshow("image", img)
cv2.imshow("output", imgOutput)
cv2.waitKey(0)
