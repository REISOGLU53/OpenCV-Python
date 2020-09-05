import cv2

img=cv2.imread("../02_video_islemleri/lamb.jpg", 1)
cv2.namedWindow("lamborgini", cv2.WINDOW_NORMAL)
cv2.imshow("lamborgini", img)
cv2.imwrite("lamb2.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()