import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()
from itertools import count
import numpy as np
import cv2 as cv
import csv
import pickle 
import pytesseract
import imutils
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
recog=cv.face.LBPHFaceRecognizer_create()
recog.read("trainer.yml")  
coount=0
labels={"person_name":1}
with open ("labels.pickle","rb") as f:
    og_labels=pickle.load(f)
    labels={v:k for k,v in og_labels.items()}
    

def hello ():  
    label1 = tk.Label(root, text= 'Hello World!', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)
    
def imageprocess():
    vid=cv.VideoCapture(0)

    while(True):
        #Capture frame by frame
        ret, frame=vid.read()
        frame=cv.flip(frame,1)
        
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5) 
        eyes = eye_cascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 4)
        
        for (x,y,w,h) in faces:
            coount=coount+1
            
            print(x,y,w,h)
            roi_gray=gray[y:y+h, x:x+w]
            id,conf=recog.predict(roi_gray)
            #print(conf)
            if conf>=45 and conf<=110:
                print(id)
                cv.imwrite("faces/"+str(id)+str(coount)+".jpg",frame)
            
                print(labels[id])
                font=cv.FONT_HERSHEY_SIMPLEX
                name=labels[id]
                color=(255,255,255)
                stroke=2
                cv.putText(frame,name,(x,y),font,1,color,stroke,cv.LINE_AA)
                with open("static/data/facecount.csv",'w') as f:
                    csv.writer(f).writerow([coount,name])
                    f.close()

            else:
                cv.imwrite("faces/unknown"+str(coount)+".jpg",frame)
                with open("static/data/facecount.csv",'w') as f:
                    csv.writer(f).writerow([coount,"unknown"])
                    f.close()
            #face_img="my_img.png"
            #cv.imwrite(face_img,roi_gray)
            
            color=(255,255,255)
            stroke=1
            #print(w,h)
            width=x+w
            height=y+h
            x1=int(w)
            y1=int(h)
            print(x1,y1)
            cv.rectangle(frame,(x,y),(width,height),color,stroke)
            #cv.circle(frame,(x+int(w/4),y+int(y/3)),int(w/5),color,2)#x,y are starting coordinates, width and height are ending coordinates
        
        for (x2,y2,w,h) in eyes:
                cv.circle(frame,(int(x2+w/2),int(y2+h/2)),(int((w+h)/10)),(255,255,255),1)
                cv.circle(frame,(int(x2+w/2),int(y2+h/2)),(int((w+h)/6.5)),(255,255,255),1)
                
        img2 = cv.imread('bg.png')


        cv.imshow('noicw',frame)
        cv.imwrite('static/data/live_feed/livefeed.jpg',frame)
        
        if cv.waitKey(20) & 0XFF== ord('b'):
            break

    vid.release()
    cv.destroyAllWindows()

    
    
button1 = tk.Button(text='Click Me',command=imageprocess, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()