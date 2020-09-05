import cv2

img = cv2.imread("../02_video_islemleri/lamb.jpg", 1)
cv2.namedWindow("lamb")

img = cv2.resize(img, (250, 300))

cv2.imshow("lamb", img)

cv2.waitKey(0)
cv2.destroyAllWindows()