# reading video
import cv2
capture = cv2.VideoCapture("video/videoplayback.mp4")
# capture.
while True:
    success, img = capture.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
