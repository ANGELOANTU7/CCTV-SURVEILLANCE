import numpy as np
import cv2 as cv
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
vid=cv.VideoCapture(0)

while(True):
    #Capture frame by frame
    ret, frame=vid.read()
    frame=cv.flip(frame,1
)
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5) 
    for (x,y,w,h) in faces:
        print("faces found:",len(faces))
        print(x,y,w,h)
        roi_gray=gray[y:y+h, x:x+w]
        face_img="my_img.png"
        cv.imwrite(face_img,roi_gray)
        
    cv.imshow('frame',frame)
    
    if cv.waitKey(20) & 0XFF== ord('b'):
        break

vid.release()
cv.destroyAllWindows()
