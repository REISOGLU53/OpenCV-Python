"""import cv2

vid = cv2.VideoCapture("car.mp4")
ret, first_frame = vid.read()
first_frame = cv2.resize(first_frame, (640, 512))
first_frame = cv2.flip(first_frame, 1)
gray1 = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
blur1 = cv2.GaussianBlur(gray1, (9, 9), 0)

while True:
    ret, frame = vid.read()
    if ret == 0: break
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (640, 512))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)

    diff = cv2.absdiff(blur1, blur, 0)
    _, diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

    cv2.imshow("frame", frame)
    cv2.imshow("diff", diff)
    if cv2.waitKey(1) & 0xFF == ord("q"): break

vid.release()
cv2.destroyAllWindows()"""


"""import cv2

vid = cv2.VideoCapture("car.mp4")
subtractor = cv2.createBackgroundSubtractorMOG2(history=1000, varThreshold=50, detectShadows=True)

while True:
    ret, frame = vid.read()
    if ret == 0: break
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (640, 480))

    mask = subtractor.apply(frame)

    cv2.imshow("_", frame)
    cv2.imshow("__", mask)
    if cv2.waitKey(1) & 0xFF == ord("q"): break

vid.release()
cv2.destroyAllWindows()"""
