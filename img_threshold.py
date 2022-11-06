import cv2
import numpy as np
i = input("Enter a image location with name: ")
img = cv2.imread(i)
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
k = int(input("Enter threshold minimum range: "))
l = int(input("Enter threshold maximum range: "))
ret,thresh = cv2.threshold(img1,k,l,0)
cv2.imshow("Original Image",img)
cv2.imshow("Grsy Image",img1)
cv2.imshow("threshold Image",thresh)
cv2.waitKey()
cv2.destroyAllWindows()