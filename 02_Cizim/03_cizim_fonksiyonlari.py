import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255
cv2.line(canvas, (0, 0), (512, 512), (512, 0, 0), thickness=3)
cv2.line(canvas, (0, 512), (512, 0), (0, 0, 255), thickness=3)
cv2.line(canvas, (0, 256), (512, 256), (0, 255, 0), thickness=3)
cv2.line(canvas, (256, 0), (256, 512), (126, 255, 0), thickness=3)

cv2.rectangle(canvas, (50, 50), (200, 80), (0, 100, 255), thickness=-1)

cv2.circle(canvas, (256,256), 50, (0, 0, 255), thickness=1, lineType=4)

cv2.line(canvas, (400, 0), (256, 200), (512, 0, 0), thickness=3)
cv2.line(canvas, (256, 200), (512, 200), (512, 0, 0), thickness=3)
cv2.line(canvas, (512, 200), (400, 0), (512, 0, 0), thickness=3)

points = np.array([[[50,50], [50, 450], [450, 450], [450, 50]]], np.int32)
cv2.polylines(canvas, [points], True, (0, 0, 255), 1)

cv2.ellipse(canvas, (256, 256), (200, 25), 10, 90, 360, (0, 255, 0), 1)

cv2.imshow("canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()