import cv2

filename = "C:\\Users\ertug\PycharmProjects\OpenCV_\OpenCV\\ilk_video.avi"
codec = cv2.VideoWriter_fourcc("W", "M", "V", "2")
framerate = 30
resolutions = (640, 480)
videoFileOutputs = cv2.VideoWriter(filename, codec, framerate, resolutions)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if ret == 0 : break
    videoFileOutputs.write(frame)
    frame = cv2.flip(frame, 1)
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"): break

videoFileOutputs.release()
cap.release()
cv2.destroyAllWindows()









