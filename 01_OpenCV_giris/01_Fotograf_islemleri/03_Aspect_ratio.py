import cv2

def Aspect_Ratio(img, weight=None, height=None, inter=cv2.INTER_AREA):

    dimension = None
    (h ,w) = img.shape[: 2]

    if weight is None and height is None:
        return img

    if weight is None:

        r = height / float(h)
        dimension = (int(w*r), height)

    else:

        r = weight / float(w)
        dimension = (weight, (h*r))

    return cv2.resize(img, dimension, interpolation=inter)

img = cv2.imread("../02_video_islemleri/lamb.jpg", 1)
img1 = Aspect_Ratio(img, weight=None, height=850, inter=cv2.INTER_AREA)

cv2.imshow("Original", img)
cv2.imshow("Resized", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
