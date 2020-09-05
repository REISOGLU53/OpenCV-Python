import cv2

img = cv2.imread("star_.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, 2, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
hull = cv2.convexHull(cnt, returnPoints=False)
defects = cv2.convexityDefects(cnt, hull)

for i in range(defects.shape[0]):
    start, end, far, distance = defects[i, 0]
    start_ = tuple(cnt[start][0])
    end_ = tuple(cnt[end][0])
    far_ = tuple(cnt[far][0])

    cv2.line(img, start_, end_, [12, 52, 155], 2)
    cv2.circle(img, far_, 3, [54, 175, 24], -1)

cv2.imshow("_", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
