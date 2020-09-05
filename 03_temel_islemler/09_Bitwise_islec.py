import cv2

bitwise1 = cv2.imread("bitwise_1.png")
bitwise2 = cv2.imread("bitwise_2.png")

#bit_and = cv2.bitwise_and(bitwise1, bitwise2)
#bit_or = cv2.bitwise_or(bitwise1, bitwise2)
#bit_xor = cv2.bitwise_xor(bitwise1, bitwise2)
bit_not = cv2.bitwise_not(bitwise1, bitwise2)

#cv2.imshow("and", bit_and)
#cv2.imshow("or", bit_or)
#cv2.imshow("xor", bit_xor)
cv2.imshow("not", bit_not)
cv2.imshow("1", bitwise1)
cv2.imshow("2", bitwise2)

cv2.waitKey(0)
cv2.destroyAllWindows()