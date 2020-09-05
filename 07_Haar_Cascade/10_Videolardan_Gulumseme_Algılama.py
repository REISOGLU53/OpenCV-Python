import cv2

#cap = cv2.VideoCapture("smile.mp4")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface.xml")
smile_cascade = cv2.CascadeClassifier("smile.xml")

while True:
    ret, frame = cap.read()
    if ret==0: break
    frame = cv2.flip(frame, 1)
    #frame = cv2.resize(frame, (640, 640))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        roi = frame[y:y+h, x:x+w]
        roi1 = gray[y:y+h, x:x+w]

        smiles = smile_cascade.detectMultiScale(roi1, 1.7, 6)

        for (x1, y1, w1, h1) in smiles:
            cv2.rectangle(roi, (x1, y1), (x1+w1, y1+h1), (0, 0, 255), 2)

    cv2.imshow("img", frame)
    if cv2.waitKey(50) & 0xFF==ord("q"): break

cap.release()
cv2.destroyAllWindows()

