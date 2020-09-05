import cv2

img = cv2.imread("aircraft.jpg")
img = cv2.resize(img, (512, 512))

img1 = cv2.imread("aircraft1.jpg")
img1 = cv2.resize(img1, (512, 512))
img1 = cv2.medianBlur(img1, 101)

img2 = cv2.imread("polygons.png")
img2 = cv2.medianBlur(img2, 25)
img2 = cv2.resize(img2, (512, 512))

if img.shape == img1.shape:
    print("Same Size...")
else:
    print("Not Same...")

diff = cv2.subtract(img, img1)

b, g, r = cv2.split(diff)
# print(b, g, r)

q0 = cv2.countNonZero(b)
q1 = cv2.countNonZero(g)
q2 = cv2.countNonZero(r)

print("blue:", q0, "\n", "gray:", q1, "\n", "red:", q2)

cv2.imshow("difference", diff)
cv2.waitKey(0)
cv2.destroyAllWindows()
