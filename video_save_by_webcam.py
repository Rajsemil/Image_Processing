import cv2
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
l = input("Enter file location with extension: ")
j = cv2.VideoWriter(l,fourcc,20.0,(900,500))
while cap.isOpened():
	ret,frame = cap.read()
	if ret == True:
		cv2.imshow('frame',frame)
		k = cv2.waitKey(1)
		if k == ord("q"):
			break
cap.release()
j.release()
cv2.distroyAllWindows()