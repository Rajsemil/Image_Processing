import cv2
camera = "http://10.224.71.93:8080/video"
cap = cv2.VideoCapture(0)  
cap.open(camera)
j = input("Enter a location with extention for video saving: ")
fourcc = cv2.VideoWriter_fourcc(*"XVID") 
output = cv2.VideoWriter(j,fourcc,20.0,(640,480),0)
if j==ord("s"):
    cv2.VideoWriter(j,fourcc,20.0,(900,500))
while(cap.isOpened()):
    ret, frame = cap.read() 
    if ret == True:
        frame = cv2.resize(frame,(700,700))
        cv2.imshow('Colorframe',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):   #press to exit
            break
cap.release()
output.release()
cv2.destroyAllWindows()