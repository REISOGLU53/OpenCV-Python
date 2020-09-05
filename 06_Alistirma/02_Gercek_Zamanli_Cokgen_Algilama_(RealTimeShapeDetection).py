import cv2
import numpy as np

def nothing(x): pass

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cv2.namedWindow("settings")
cv2.resizeWindow("settings", 500, 500)

cv2.createTrackbar("Lower-Hue", "settings", 0, 180, nothing)
cv2.createTrackbar("Lower-Saturation", "settings", 0, 255, nothing)
cv2.createTrackbar("Lower-Value", "settings", 0, 255, nothing)
cv2.createTrackbar("Upper-Hue", "settings", 0, 180, nothing)
cv2.createTrackbar("Upper-Saturation", "settings", 0, 255, nothing)
cv2.createTrackbar("Upper-Value", "settings", 0, 255, nothing)

cv2.setTrackbarPos("Upper-Hue", "settings", 180)
cv2.setTrackbarPos("Upper-Saturation", "settings", 255)
cv2.setTrackbarPos("Upper-Value", "settings", 255)

font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, frame = cap.read()
    if ret == 0: break
    frame = cv2.flip(frame, 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("Lower-Hue", "settings")
    l_s = cv2.getTrackbarPos("Lower-Saturation", "settings")
    l_v = cv2.getTrackbarPos("Lower-Value", "settings")

    u_h = cv2.getTrackbarPos("Upper-Hue", "settings")
    u_s = cv2.getTrackbarPos("Upper-Saturation", "settings")
    u_v = cv2.getTrackbarPos("Upper-Value", "settings")

    lower_color = np.array([l_h, l_s, l_v])
    upper_color = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, lower_color, upper_color)
    kernel = np.ones((9, 9), dtype=np.uint8)
    mask = cv2.erode(mask, kernel)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours[1:]:
        area = cv2.contourArea(cnt)
        epsilon = .02*cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)

        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if area > 400:
            cv2.drawContours(frame, [approx], 0, (0, 0, 0), 2)
            if len(approx)==3: cv2.putText(frame, "Triangle", (x, y), font, 1, (0, 0, 255), 2)
            elif len(approx) == 4: cv2.putText(frame, "Rectangle", (x, y), font, 1, (0, 0, 255), 2)
            elif len(approx) == 5: cv2.putText(frame, "Pentagon", (x, y), font, 1, (0, 0, 255), 2)
            else: cv2.putText(frame, "Circle", (x, y), font, 1, (0, 0, 255), 2)

    cv2.imshow("_", frame)
    cv2.imshow("__", mask)
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release()
cv2.destroyAllWindows()
