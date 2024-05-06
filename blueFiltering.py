import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    frame = cv2.resize(frame,(540,360))
    
    if not ret:
        break

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_blue = np.array([90,100,100])
    upper_blue = np.array([130,255,255])

    mask = cv2.inRange(hsv,lower_blue,upper_blue)

    result = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('Original',frame)
    cv2.imshow("Masked",mask)
    cv2.imshow("Filtered",result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()