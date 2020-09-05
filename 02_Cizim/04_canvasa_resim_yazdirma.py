import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255

font1 = cv2.FONT_HERSHEY_DUPLEX
font2 = cv2.FONT_ITALIC
font3 = cv2.FONT_HERSHEY_COMPLEX
font4 = cv2.FONT_HERSHEY_COMPLEX_SMALL


cv2.putText(canvas, "Canvas", (20, 256), font3, 4, (0, 0, 255), cv2.LINE_8)

cv2.imshow("canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()