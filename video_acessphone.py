import cv2
camera = "http://10.212.239.91:8080/video"
cap = cv2.VideoCapture(0)
cap.open(camera)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
k = input("Enter file location with extension: ")
j = cv2.VideoWriter(k,fourcc,20.0,(900,500))
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