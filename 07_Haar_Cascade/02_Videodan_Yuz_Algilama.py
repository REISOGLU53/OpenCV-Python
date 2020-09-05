import cv2

# cap = cv2.VideoCapture("faces.mp4")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface.xml")
while True:
    ret, frame = cap.read()
    if ret == 0: break
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 2, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow("frame", frame)
    if cv2.waitKey(50) & 0xFF==ord("q"): break

cap.release()
cv2.destroyAllWindows()
