import cv2

img = cv2.imread("ertugrul2.jpg")
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface.xml")
# img = cv2.resize(img, (512, 512))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # cvt:convert
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces: 
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

