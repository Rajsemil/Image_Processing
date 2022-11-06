import cv2
import numpy as np
#Read an Image---
img = cv2.imread("E:\\raj.png")
cv2.imshow("res",img)
print("shape==",img.shape) #returns a tuple of number of rows, columns, and channels
print("no.of pixels==",img.size) #returns Total number of pixels is accessed
print("datatype==",img.dtype) #returns Image datatype is obtained
print("Imagetype==",type(img))
print(img)#show image in array
print("Split image==",cv2.split(img))
b,g,r = cv2.split(img)

cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)
cv2.waitKey()
cv2.destroyAllWindows()