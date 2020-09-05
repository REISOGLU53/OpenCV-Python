import cv2

img_filter = cv2.imread("filter.png")
img_median = cv2.imread("median.png")
img_bilateral = cv2.imread("bilateral.png")

blur = cv2.blur(img_filter, (11, 11))
blur1 = cv2.GaussianBlur(img_filter, (11, 11), cv2.BORDER_DEFAULT)
median = cv2.medianBlur(img_median, 25)
bilateral =cv2.bilateralFilter(img_bilateral, 5 , 67, 67)

#cv2.imshow("median blur", median)
#cv2.imshow("median", img_median)
#cv2.imshow("bilateral_filter", bilateral)
#cv2.imshow("bilateral", img_bilateral)
#cv2.imshow("blur", blur)
#cv2.imshow("filter", img_filter)
#cv2.imshow("Gausian Blur", blur1)

cv2.waitKey(0)
cv2.destroyAllWindows()