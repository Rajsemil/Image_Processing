import cv2
p = input("Enter a video path with extension: ")
cap = cv2.VideoCapture(p)
while True:
	ret,frame = cap.read()
	frame = cv2.resize(frame,(700,450))
	cv2.imshow('frame',frame)
	k = cv2.waitKey(26)
	if k == ord("q"):
		break
cv2.release()
cv2.distroyAllWindows()