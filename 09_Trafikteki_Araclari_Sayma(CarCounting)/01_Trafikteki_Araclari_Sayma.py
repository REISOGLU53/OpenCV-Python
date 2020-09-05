import cv2
import numpy as np

vid = cv2.VideoCapture("traffic.avi")
backGraung = cv2.createBackgroundSubtractorMOG2()
c = 0

while True:
    ret, frame = vid.read()
    if ret:
        fgmask = backGraung.apply(frame)
        cv2.imshow("img", fgmask)

        if cv2.waitKey(1) & 0xFF==ord("q"): break

vid.release()
cv2.destroyAllWindows()
