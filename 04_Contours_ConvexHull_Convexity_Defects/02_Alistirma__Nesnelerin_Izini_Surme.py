import cv2
import numpy as np

cap = cv2.VideoCapture("dog.mp4")
while True:
    ret, frame = cap.read()
    if ret == 0: break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # iz sürmek için / for scenting out
    sensitivity = 15
    lower_white = np.array([0, 0, 255 - sensitivity])  # hsv code for white code
    upper_white = np.array([255, sensitivity, 255])  # hsv code for white code
    mask = cv2.inRange(hsv, lower_white, upper_white)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("dog_ori", frame)
    cv2.imshow("dog_res", res)
    cv2.imshow("dog_mask", mask)
    if cv2.waitKey(10) & 0xFF == ord("q"): break

cap.release()
cv2.destroyAllWindows()
