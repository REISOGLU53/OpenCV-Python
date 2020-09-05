import cv2

# the photo is in "bgr" space in first time
img = cv2.imread("ferrari.jpg", -1)
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img3 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)





cv2.imshow("ferrari", img)
cv2.imshow("rgb", img1)
cv2.imshow("hsv", img2)
cv2.imshow("gray", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
