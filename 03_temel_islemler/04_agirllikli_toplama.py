import cv2
import numpy as np

circle = np.zeros((512, 512, 3), dtype = np.uint8) + 255
cv2.circle(circle, (256, 256), 50, color = (0, 0, 255), thickness = -1)

rectangle = np.zeros((512, 512, 3), dtype = np.uint8) + 255
cv2.rectangle(rectangle, (200, 200), (300, 300), color=(0,255,0), thickness=-1)

dst = cv2.addWeighted(circle, .7, rectangle, .3, 0 )

cv2.imshow("circle", circle)
cv2.imshow("reclangle", rectangle)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()