import numpy as np 
import cv2
s = input("Enter a image location with name: ")
img = cv2.imread(s)
t = str(input("Enter a characters for putting on image: "))
#circle - accept(img,star_co,radius,color,thickness)
j = int(input("Enter a X-axis number: "))
k = int(input("Enter a Y-axis number: "))
print("Enter a color number 0 to 255")
l = int(input("Enter a blue color number: "))
m = int(input("Enter a green color number: "))
n = int(input("Enter a red color number: "))
i = int(input("Enter a thickness number for drawing circle: "))
font = cv2.FONT_ITALIC
#puttext -accept(img,text,start_co,font,fontsize,color,thickness,linetype)
img = cv2.putText(img, t, (j, k), font, 4, (l, m, n), i,cv2.LINE_AA)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows() 