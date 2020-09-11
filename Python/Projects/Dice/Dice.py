import random
import cv2


def findint():
    value = random.randint(1, 7)
    return value


def showing(no):
    img = cv2.imread("img/"+str(no)+".jpg")
    return img


value = int(findint())
print(value)
A = showing(value)
cv2.imshow("Image", A)
cv2.waitKey(0)
