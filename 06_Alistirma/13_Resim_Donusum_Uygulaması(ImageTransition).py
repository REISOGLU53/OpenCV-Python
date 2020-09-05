import cv2

def nothing(x): pass

img1 = cv2.imread("aircraft.jpg")
img1 = cv2.resize(img1, (512, 512))
img2 = cv2.imread("starwars.jpg")
img2 = cv2.resize(img2, (512, 512))

cv2.namedWindow("Transition Program")
cv2.resizeWindow("Transition Program", (512, 512))

output = cv2.addWeighted(img1, .5, img2, .5, 0)
cv2.createTrackbar("Alpha-Beta", "Transition Program", 0, 1000, nothing)
while True:
    cv2.imshow("Transition Program", output)
    alpha = cv2.getTrackbarPos("Alpha-Beta", "Transition Program")/1000
    beta = 1 - alpha
    print("alpha: "+str(round(alpha, 4)),  "\t", "beta: "+str(round(beta, 4)))
    output = cv2.addWeighted(img1, alpha, img2, beta, 0)

    if cv2.waitKey(1) & 0xFF==ord("q"): break
cv2.destroyAllWindows()
