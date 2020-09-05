import cv2

img = cv2.imread("ferrari.jpg", 0)

ret, th1 = cv2.threshold(img, 25, 200, cv2.THRESH_BINARY)
ret, th2 = cv2.threshold(img, 25, 200, cv2.THRESH_BINARY_INV)
th3 = cv2.adaptiveThreshold(img, 200, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 2)
th4 = cv2.adaptiveThreshold(img, 200, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 2)

cv2.imshow("threshold1", th1)
cv2.imshow("threshold2", th2)
cv2.imshow("threshold3", th3)
cv2.imshow("threshold4", th4)
cv2.waitKey(0)
cv2.destroyAllWindows()
