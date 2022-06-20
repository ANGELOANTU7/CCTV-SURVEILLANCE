import numpy as np
import cv2 as cv
  
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
recog=cv.face.LBPHFaceRecognizer_create()
recog.read("trainer.yml")  
vid=cv.VideoCapture(0)

while(True):
    #Capture frame by frame
    ret, frame=vid.read()
    frame=cv.flip(frame,1)
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5) 
    
    for (x,y,w,h) in faces:
        #print(x,y,w,h)
        roi_gray=gray[x:x+w,y:y+h]
        id,conf=recog.predict(roi_gray)
        #print(conf)
        if conf>=45 and conf<=110:
            print(id)
        #face_img="my_img.png"
        #cv.imwrite(face_img,roi_gray)
        
        color=(255,0,0)
        stroke=2
        width=x+w
        height=y+h
        cv.rectangle(frame,(x,y),(width,height),color,stroke) #x,y are starting coordinates, width and height are ending coordinates


    cv.imshow('frame',frame)
    
    if cv.waitKey(20) & 0XFF== ord('b'):
        break

vid.release()
cv.destroyAllWindows()
