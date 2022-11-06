import cv2
import numpy as np
cap = cv2.VideoCapture(0)

def nothing(x):
    pass

cv2.namedWindow("Color Detection")
cv2.createTrackbar("Lower_H", "Color Detection", 0, 255, nothing)
cv2.createTrackbar("Lower_S", "Color Detection", 0, 255, nothing)
cv2.createTrackbar("Lower_V", "Color Detection", 0, 255, nothing)

cv2.createTrackbar("Upper_H", "Color Detection", 255, 255, nothing)
cv2.createTrackbar("Upper_S", "Color Detection", 255, 255, nothing)
cv2.createTrackbar("Upper_V", "Color Detection", 255, 255, nothing)


while True:
    _,frame = cap.read()
    hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("Lower_H", "Color Detection")
    l_s = cv2.getTrackbarPos("Lower_S", "Color Detection")
    l_v = cv2.getTrackbarPos("Lower_V", "Color Detection")

    u_h = cv2.getTrackbarPos("Upper_H", "Color Detection")
    u_s = cv2.getTrackbarPos("Upper_S", "Color Detection")
    u_v = cv2.getTrackbarPos("Upper_V", "Color Detection")
    
    lower_bound = np.array([l_h, l_s, l_v])
    upper_bound = np.array([u_h, u_s, u_v])
    
    #Creating Mask
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    #filter mask with image
    res = cv2.bitwise_and(cap, cap, mask=mask)

    cv2.imshow("cap", cap)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()