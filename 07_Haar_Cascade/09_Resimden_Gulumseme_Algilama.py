import cv2

img = cv2.imread("ertugrul1.jpg")
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.2, 5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

    roi = img[y:y+h, x:x+w]
    roi1 = gray[y:y+h, x:x+w]

    smile_cascade = cv2.CascadeClassifier("smile.xml")
    smiles = smile_cascade.detectMultiScale(roi1, 1.2, 6)

    for (x1, y1, w1, h1) in smiles:
        cv2.rectangle(roi, (x1, y1), (x1+w1, y1+h1), (0, 0, 255), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
