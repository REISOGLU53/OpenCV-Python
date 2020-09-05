import cv2

img = cv2.imread("ferrari.jpg", -1)
print(img.shape)

roi = img[100:150, 150:250]
cv2.imshow("ferrari", img)
cv2.imshow("roi", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()