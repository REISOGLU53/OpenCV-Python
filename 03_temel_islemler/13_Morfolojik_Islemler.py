import cv2
import numpy as np

img = cv2.imread("ferrari.jpg", 0)
kernel = np.ones((3, 3), dtype=np.uint8)
erosion = cv2.erode(img, kernel, iterations=2)
dilation = cv2.dilate(img, kernel, iterations=2)
morphology = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
morphology1 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
morphology2 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
morphology3 = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
morphology4 = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("original", img)
cv2.imshow("erosion", erosion)
cv2.imshow("dilation", dilation)
cv2.imshow("morphology", morphology)
cv2.imshow("morphology1", morphology1)
cv2.imshow("morphology2", morphology2)
cv2.imshow("morphology3", morphology3)
cv2.imshow("morphology4", morphology4)
cv2.waitKey(0)
cv2.destroyAllWindows()
