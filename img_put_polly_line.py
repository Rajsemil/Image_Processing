import numpy as np 
import cv2
s = input("Enter a image location with name: ")
img = cv2.imread(s)
# Draw poly line on image
pts = np.array([[100,150],[200,30],[170,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,155))
cv2.imshow("iamge",img)
cv2.waitKey(0)
cv2.destroyAllWindows() 