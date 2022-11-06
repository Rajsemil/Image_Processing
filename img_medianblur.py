import cv2
import numpy as np
i = input("Enter a image path with name: ")
img = cv2.imread(i)
j = int(input("ENter a number for blur image:"))
img1 = cv2.medianBlur(img,j)
cv2.imshow("Original",img)
cv2.imshow("original",img1)
k = cv2.waitKey()
if k==ord("q"):
	pass
cv2.destroyAllWindows()