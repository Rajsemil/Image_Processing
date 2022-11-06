import cv2
import numpy as np
img = cv2.imread("color_balls.jpg")
#img = cv2.VideoCapture(0)
while True:
	hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	upper_value = np.array([48,255,248])
	lower_value = np.array([20,143,139])
	mask = cv2.inRange(hsv,lower_value,upper_value)
	res = cv2.bitwise_and(img,img,mask=mask)
	cv2.imshow("original image",img)
	cv2.imshow("Detect image",res)
	k = cv2.waitKey()
	if k==ord("q"):
		break
cv2.destroyAllWindows()