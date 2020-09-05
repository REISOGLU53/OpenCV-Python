import cv2

img = cv2.imread("starwars.jpg")
img = cv2.resize(img, (640, 480))
blur = cv2.medianBlur(img, 9)
Laplacian = round(cv2.Laplacian(blur, cv2.CV_64F).var(), 4)
print(Laplacian)

if Laplacian < 500:
    print("the image is blured")
else:
    print(":)")

cv2.imshow("img", img)
cv2.imshow("img_blur", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
