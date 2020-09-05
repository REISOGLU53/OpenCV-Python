import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

def nothing(x): pass

cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar", 500, 500)

cv2.createTrackbar("LOWER - H", "Trackbar", 0, 180, nothing)
cv2.createTrackbar("LOWER - S", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("LOWER - V", "Trackbar", 0, 255, nothing)

cv2.createTrackbar("UPPER - H", "Trackbar", 0, 180, nothing)
cv2.createTrackbar("UPPER - S", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("UPPER - V", "Trackbar", 0, 255, nothing)

cv2.setTrackbarPos("UPPER - H", "Trackbar", 180)
cv2.setTrackbarPos("UPPER - S", "Trackbar", 255)
cv2.setTrackbarPos("UPPER - V", "Trackbar", 255)

while True:

    ret, frame = cap.read()
    if ret == 0: break
    frame = cv2.flip(frame, 1)

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_h = cv2.getTrackbarPos("LOWER - H", "Trackbar")
    lower_s = cv2.getTrackbarPos("LOWER - S", "Trackbar")
    lower_v = cv2.getTrackbarPos("LOWER - V", "Trackbar")

    upper_h = cv2.getTrackbarPos("UPPER - H", "Trackbar")
    upper_s = cv2.getTrackbarPos("UPPER - S", "Trackbar")
    upper_v = cv2.getTrackbarPos("UPPER - V", "Trackbar")

    lower_color = np.array([lower_h, lower_s, lower_v])
    upper_color = np.array([upper_h, upper_s, upper_v])

    mask = cv2.inRange(frame_hsv, lower_color, upper_color)

    cv2.imshow("Original", frame)
    cv2.imshow("Mask", mask)
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release()
cv2.destroyAllWindows()

