import cv2
import numpy as np

img = cv2.imread("coins.jpg")
#img = cv2.resize(img, (640, 512))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 5)
circle = cv2.HoughCircles(image=blur, method=cv2.HOUGH_GRADIENT, dp=1,
                          minDist=img.shape[0] / 4, param1=200, param2=10,
                          minRadius=15, maxRadius=89)  # param1: gradiend, param2: threshold

if circle is not None:
    circle = np.uint16(np.around(circle))
    for i in circle[0, :]:
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)

cv2.imshow("__", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
