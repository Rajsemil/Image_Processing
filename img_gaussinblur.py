import cv2
import numpy as np
i = input("Enter a image path with name: ")
img = cv2.imread(i)
j = int(input("ENter a number for blur image:"))
img1 = cv2.GaussianBlur(img,(j,j),0)
cv2.imshow("Original",img)
cv2.imshow("original",img1)
m = input("Enter a location with name for saving: ")
k = cv2.waitKey()
if k==ord("q"):
	pass
cv2.destroyAllWindows()