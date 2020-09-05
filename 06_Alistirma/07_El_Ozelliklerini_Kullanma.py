import cv2
import numpy as np
import math

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

def findMaxContour(contours):
    max_i, max_area = 0, 0
    for i in range(len(contours)):
        area_hand = cv2.contourArea(contours[i])
        if max_area < area_hand:
            max_area = area_hand
            max_i = i
        try:
            cnt = contours[max_i]
        except:
            contours = [0]
            cnt = contours[0]
        return cnt

while True:
    ret, frame = cap.read()
    if ret == 0: break
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (512, 512))

    roi = frame[80:400, 150:400]  # frame[y1:y2, x1:x2]
    cv2.rectangle(frame, (150, 80), (400, 400), (0, 0, 255), 0)

    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    lower_hsv = np.array([0, 45, 79], dtype=np.uint8)
    upper_hsv = np.array([17, 255, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    kernel = np.ones((3, 3), dtype=np.uint8)
    mask = cv2.dilate(mask, kernel=kernel, iterations=1)
    mask = cv2.medianBlur(mask, 9)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) is not None:

        cnt = findMaxContour(contours)
        extLeft = tuple(cnt[cnt[:, :, 0].argmin()][0])
        extRight = tuple(cnt[cnt[:, :, 0].argmax()][0])
        extTop = tuple(cnt[cnt[:, :, 1].argmin()][0])
        # We want to create a triangle, so we should erase "extBottom"!

        cv2.circle(roi, extLeft, 5, (0, 0, 255), 2)
        cv2.circle(roi, extRight, 5, (0, 0, 255), 2)
        cv2.circle(roi, extTop, 5, (0, 0, 255), 2)

        cv2.line(roi, extLeft, extTop, (0, 0, 255), 2)
        cv2.line(roi, extTop, extRight, (0, 0, 255), 2)
        cv2.line(roi, extRight, extLeft, (0, 0, 255), 2)

        a = math.sqrt(pow(extRight[0] - extTop[0], 2) + pow(extRight[1] - extTop[1], 2))
        b = math.sqrt(pow(extRight[0] - extLeft[0], 2) + pow(extRight[1] - extLeft[1], 2))
        c = math.sqrt(pow(extLeft[0] - extTop[0], 2) + pow(extLeft[1] - extTop[1], 2))

        try:
            angle_ab = math.acos((a**2 + b**2 - c**2)/ (2*b*c))*57
            cv2.putText(roi, str(round(angle_ab, 2)), (extRight[0]-100, extRight[1]), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 0, 255), 2, cv2.LINE_AA)

            if  angle_ab >= 70: cv2.rectangle(roi, (0, 0), (100, 100), (0, 255, 0), -1)
            else: pass

        except:
            cv2.putText(roi, "?", (extRight[0] - 100, extRight[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,
                        cv2.LINE_AA)

    else:
        pass

    cv2.imshow("mask", mask)
    cv2.imshow("roi", roi)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release()
cv2.destroyAllWindows()
