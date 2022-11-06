import cv2
img = cv2.imread('E:\\raj.png',0)
img = cv2.resize(img,(1200,700))
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()