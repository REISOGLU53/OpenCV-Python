import cv2
import numpy as np

cap = cv2.VideoCapture("line.mp4")
while True:
    ret, frame = cap.read()
    if ret == 0: break
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (640, 512))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([20, 100, 100], dtype=np.uint8)
    upper_yellow = np.array([30, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    edges = cv2.Canny(mask, 50, 255)
    h_lines = cv2.HoughLinesP(edges, 1, np.pi/180, 10, maxLineGap=5)
    for line in h_lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

    cv2.imshow("_", edges)
    cv2.imshow("__", frame)
    if cv2.waitKey(5) & 0xFF == ord("q"): break

cap.release()
cv2.destroyAllWindows()
