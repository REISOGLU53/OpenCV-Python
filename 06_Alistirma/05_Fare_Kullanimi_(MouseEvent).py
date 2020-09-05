import cv2

cap = cv2.VideoCapture("line.mp4")
circles = list()

def mouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        circles.append((x,y))

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", mouse)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (512, 512))

    for center in circles:
        cv2.circle(frame, center, 20, (255, 0, 0), 3)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == ord("q"): break
    elif key == ord("w"): circles = list()

cap.release()
cv2.destroyAllWindows()

