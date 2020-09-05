import cv2

font = cv2.FONT_HERSHEY_COMPLEX_SMALL
img = cv2.imread("polygons.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 175, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours[1:]:
    epsilon = .0085*cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)

    draw = cv2.drawContours(img, [approx], 0, color=(255, 0, 0), thickness=3)
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if len(approx) == 3: cv2.putText(img, "Triangle", (x, y), font, 1, color=(0, 0, 255), thickness=3)
    elif len(approx) == 4: cv2.putText(img, "Rectangle", (x, y), font, 1, color=(0, 0, 255), thickness=3)
    elif len(approx) == 5: cv2.putText(img, "Pentagon", (x, y), font, 1, color=(0, 0, 255), thickness=3)
    elif len(approx) == 6: cv2.putText(img, "Hexagon", (x, y), font, 1, color=(0, 0, 255), thickness=3)
    else: cv2.putText(img, "Ellipse", (x, y), font, 1, color=(0, 0, 255), thickness=3)

cv2.imshow("_", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
