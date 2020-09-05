import cv2

cap = cv2.VideoCapture("car.mp4")
body_cascade = cv2.CascadeClassifier("car_cascade.xml")

while True:
    ret, frame = cap.read()
    if ret == 0: break
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (640, 360))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bodies = body_cascade.detectMultiScale(gray, 1.2, 2)

    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF==ord("q"): break

cap.release()
cv2.destroyAllWindows()
