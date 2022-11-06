import cv2
import numpy as np
img = cv2.imread("E:\\raj.png")
bdr =  cv2.copyMakeBorder(img,10,10,5,5,cv2.BORDER_CONSTANT,value = [255,0,125])
cv2.imshow("res",bdr)
cv2.waitKey()
cv2.destroyAllWindows()