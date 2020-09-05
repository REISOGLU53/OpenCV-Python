import cv2
import numpy as np

img = cv2.imread("starwars.jpg", 0)
temp = cv2.imread("starwars2.jpg", 0)
w, h = temp.shape[::-1]

location = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
where = np.where(location >= .95)

for point in zip(*where[::-1]):
    cv2.rectangle(img, (point[0], point[1]), (point[0]+w, point[1]+h), (0, 0, 255), 2)

cv2.imshow("img", img)
cv2.imshow("temp", temp)
cv2.imshow("location", location)
cv2.waitKey(0)
cv2.destroyAllWindows()
