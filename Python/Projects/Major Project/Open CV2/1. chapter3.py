# starting webcam.
import cv2
capture = cv2.VideoCapture(0)
# capture.
while True:
    success, img = capture.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
