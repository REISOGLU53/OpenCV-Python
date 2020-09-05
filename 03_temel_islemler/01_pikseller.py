import cv2
import numpy as np

img = cv2.imread("ferrari.jpg", -1)
#shape of img
dimension = img.shape
print(dimension)
#resize the img
img = cv2.resize(img, (1000, 1000))
color = img[256, 256]
print(color)
#for blue color
blue = img[256, 256][0]
print(blue)
blue1 = img.item(256, 256, 0)
print(blue1)
img.itemset((256, 256, 0), 250)
print(color)
#changing ofimg piksels
img[700, 700][0]= 255
cv2.imshow("ferrari", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
