import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    #haarcascade için görüntüyü gri tona çevirmemiz gerekir.
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


    #Yüzleri Algıla
    faces = face_cascade.detectMultiScale(gray_frame,scaleFactor=1.1,minNeighbors=5)

    #Bulunan yüz üstüne dikdörtgen çizelim
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)


    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

