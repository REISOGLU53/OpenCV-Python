"""
#video
import cv2
cap = cv2.VideoCapture("ayder.mp4")
while True:
    ret, frame = cap.read()
    if ret ==0:break
    frame=cv2.flip(frame, 1)
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF==ord("e"):
        break

cap.release()
cv2.destroyAllWindows()

"""
# webcam
import cv2
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frame=cv2.flip(frame, 1)
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF==ord("e"):
        break

cap.release()
cv2.destroyAllWindows()
