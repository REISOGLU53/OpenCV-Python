import cv2

cap = cv2.VideoCapture("eye_motion.mp4")
while True:
    ret, frame = cap.read()
    if ret == 0: break
    frame = cv2.flip(frame, 1)

    roi = frame[80:210, 190:400]
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 2, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
    rows, cols, channels = roi.shape

    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)

        cv2.rectangle(roi, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.line(roi, (int(x+w/2), int(y)), (int(x+w/2), int(y+h)), (255, 0, 0), 2)
        cv2.line(roi, (int(x), int(y+h/2)), (int(x+w), int(y+h/2)), (255, 0, 0), 2)

        cv2.rectangle(thresh, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.line(thresh, (int(x+w/2), int(y)), (int(x+w/2), int(y+h)), (255, 0, 0), 2)
        cv2.line(thresh, (int(x), int(y+h/2)), (int(x+w), int(y+h/2)), (255, 0, 0), 2)
        break

    frame[80:210, 190:400] = roi
    cv2.imshow("frame", frame)
    cv2.imshow("roi", thresh)
    if cv2.waitKey(90) & 0xFF == ord("q"): break

cap.release()
cv2.destroyAllWindows()
