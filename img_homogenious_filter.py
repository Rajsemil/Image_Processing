import cv2
import numpy as np
i = input("Enter a image path with name: ")
img = cv2.imread(i)
kernal1 = np.ones((5,5),np.float32)/25
filter_1 = cv2.filter2D(img,-1,kernal1)
cv2.imshow("original",img)
cv2.imshow("Homogenious",filter_1)
k = cv2.waitKey()
if k==ord("q"):
	pass
cv2.destroyAllWindows()