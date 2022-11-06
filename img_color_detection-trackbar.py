import cv2
import numpy as np
ti = input("Enter a image location with name:")
img = cv2.imread(ti)
img = cv2.resize(img,(600,400))

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
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
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
    res = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("img", img)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()