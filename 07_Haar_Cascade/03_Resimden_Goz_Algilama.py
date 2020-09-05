import cv2

img = cv2.imread("face.png")
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.8, 5)

for (x, y, w, h) in faces:
    roi = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 225), 2)

    eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
    eyes = eye_cascade.detectMultiScale(roi, 1.3, 7)

    for (x1, y1, w1, h1) in eyes:
        if x1>x and y1>y: roi1 = cv2.rectangle(img, (x1, y1), (x1+w1, y1+h1), (0, 0, 255), 2)
        else: pass

cv2.imshow("img", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()