import cv2
import datetime
cap = cv2.VideoCapture(0)  
cap.set(3, 600)  #here 3 for width
cap.set(4, 800)  #here 4 for height 
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
       font = cv2.FONT_HERSHEY_COMPLEX_SMALL
       text = ' Height: ' + str(cap.get(4))+' Width: '+ str(cap.get(3))
       date_data = "Date: "+str(datetime.datetime.now())
       frame = cv2.putText(frame, text, (10, 20), font, 1,
                           (0, 155, 255), 1, cv2.LINE_AA)
       frame = cv2.putText(frame, date_data, (20, 50), font, 1,
                           (100, 255, 255), 1, cv2.LINE_AA)
       #Rectangle - accept parameter(img,start_co,end_co,colot ,thickness)
       cv2.rectangle(frame, (384, 10), (510, 128), (128, 0, 255), 8)
       cv2.imshow('frame', frame)
       if cv2.waitKey(1) & 0xFF == ord('Q'):
         break
    else:
        break
cap.release()
cv2.destroyAllWindows()