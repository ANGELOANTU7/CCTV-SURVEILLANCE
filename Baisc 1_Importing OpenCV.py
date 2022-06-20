import cv2
import numpy as np
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img=cv2.imread('avngrs1.jpg')
scale=30
width=int(img.shape[1]*scale/100)
height=int(img.shape[0]*scale/100)
dim=(width,height)
re=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
gray=cv2.cvtColor(re,cv2.COLOR_BGR2GRAY)

#import matplotlib.pyplot as plt
#print(cv2.__version__)
faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 8,minSize=(30,30))
print(faces)
for (x, y, w, h) in faces:
    print(x,y,w,h)
    cv2.rectangle(re, (x, y), (x+w, y+h), (255, 0, 0), 2)
print('faces found:',len(faces))
cv2.imshow("real",re)


# plt.imshow(img)
# plt.show()
#---------------------------------------------------------------
# print("original size:",img.shape)
#scale=10
#width=int(img.shape[1]*scale/100)
#height=int(img.shape[0]*scale/100)
#dim=(width,height)
#resized=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
# print("resized dimension:",resized.shape)
#img2=cv2.cvtColor(resized,cv2.COLOR_BGR2RGB)
#cv2.imshow("resized",img2)
#--------------------------------------------------------------
cv2.waitKey(0)
cv2.destroyAllWindows()


