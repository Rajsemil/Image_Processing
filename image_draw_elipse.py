import numpy as np 
import cv2
s = input("Enter a image location with name: ")
img = cv2.imread(s)
#ellipse-accept(img,start_cor,(length,height),color,thickness)
img = cv2.ellipse(img,(400,600),(100,50),0,0,180,155,5)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows() 