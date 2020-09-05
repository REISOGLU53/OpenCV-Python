import cv2

cv2.namedWindow("LiveCam")


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

print("weigth:"+str(cap.get(3)))
print("height:"+str(cap.get(4)))

cap.set(3, 800)
cap.set(4, 720)

print("weigth*:"+str(cap.get(3)))
print("height*:"+str(cap.get(4)))


while True:
    ret, frame = cap.read()
    if ret == 0: break
    frame = cv2.flip(frame, 1)

    cv2.imshow("LiveCam", frame)
    if cv2.waitKey(1) & 0xFF==ord("q"):break

cap.release()
cv2.destroyAllWindows()
