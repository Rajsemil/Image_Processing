import cv2
path = input("Enter your image path: ")
print("You are entered path: ",path)
i = int(input("Enter a number between -1 to 1: "))
img = cv2.imread(path,i)
if i==-1:
	print("You are entered bold scale")
elif i==0:
	print("You are entered gray scale")
elif i==1:
	print("You are entered original scale")
else:
	print("You are enterd wrong digit please take right input, Good Luck!")
cv2.imshow('Image',img)
k = cv2.waitKey(0)
s = input("Enter image path with name for save image: ")
print("You are entered saving image location: ",s)
if k == ord("s"):
		cv2.imwrite(s,img)
else:
	cv2.destroyAllWindows()