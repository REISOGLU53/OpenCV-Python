import cv2
import numpy as np

img1 = cv2.imread("t.jpg")
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
corners = cv2.goodFeaturesToTrack(gray, 50, .01, 10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img1, (x, y), 3, (0, 0, 255), 2)

cv2.imshow("corner", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
