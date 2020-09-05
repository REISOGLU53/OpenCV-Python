import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

def nothing(x): pass

cv2.namedWindow("settings")
cv2.resizeWindow("settings", (512, 512))
cv2.createTrackbar("LH", "settings", 0, 180, nothing)
cv2.createTrackbar("LS", "settings", 0, 255, nothing)
cv2.createTrackbar("LV", "settings", 0, 255, nothing)
cv2.createTrackbar("UH", "settings", 0, 180, nothing)
cv2.createTrackbar("US", "settings", 0, 255, nothing)
cv2.createTrackbar("UV", "settings", 0, 255, nothing)

cv2.setTrackbarPos("UH", "settings", 180)
cv2.setTrackbarPos("US", "settings", 255)
cv2.setTrackbarPos("UV", "settings", 255)

while True:
    ret, frame = cap.read()
    if ret == 0: break
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (380, 480))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "settings")
    l_s = cv2.getTrackbarPos("LS", "settings")
    l_v = cv2.getTrackbarPos("LV", "settings")
    u_h = cv2.getTrackbarPos("UH", "settings")
    u_s = cv2.getTrackbarPos("US", "settings")
    u_v = cv2.getTrackbarPos("UV", "settings")

    lower_color = np.array([l_h, l_s, l_v])
    upper_color = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, lower_color, upper_color)
    bitwise = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("_", frame)
    cv2.imshow("__", mask)
    cv2.imshow("___", bitwise)
    if cv2.waitKey(20) & 0xFF == ord("q"): break

cap.release()
cv2.destroyAllWindows()
