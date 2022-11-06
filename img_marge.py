import cv2
import numpy as np
#Read an Image---
img = cv2.imread("E:\\raj.png")
cv2.imshow("res",img)
b,g,r = cv2.split(img)
mr1 = cv2.merge((r,g,b))
cv2.imshow("rgb",mr1)
mr2 = cv2.merge((g,b,r))
cv2.imshow("gbr",mr2)
cv2.waitKey()
cv2.destroyAllWindows()