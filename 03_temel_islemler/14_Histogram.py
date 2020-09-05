import cv2
from matplotlib import pyplot as plt

img = cv2.imread("ferrari.jpg")
cv2.imshow("ferrari", img)

b, g, r = cv2.split(img)

plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])
#plt.hist(img.ravel(), 256, [0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindow()