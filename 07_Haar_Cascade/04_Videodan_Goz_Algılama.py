import cv2

#cap = cv2.VideoCapture("eye.mp4")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

while True:
    ret, frame = cap.read()
    if ret==0: break
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (480, 360))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 225), 2)

        eyes = eye_cascade.detectMultiScale(frame)

        for (x1, y1, w1, h1) in eyes:
            if (x1>x and y1>y) and (w1<w and h1<h): cv2.rectangle(frame, (x1, y1),
                                                                  (x1+w1, y1+h1),
                                                                  (0, 0, 255), 2)
            else: pass

    cv2.imshow("img", frame)
    if cv2.waitKey(1) & 0xFF==ord("q"): break

cap.release()
cv2.destroyAllWindows()
