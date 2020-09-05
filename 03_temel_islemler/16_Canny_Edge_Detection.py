import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if ret == 0: break

    edge = cv2.Canny(frame, 100, 200)

    frame = cv2.flip(frame, 1)
    cv2.imshow("webcam", frame)
    cv2.imshow("webcam1", edge)
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release()
cv2.destroyAllWindows()