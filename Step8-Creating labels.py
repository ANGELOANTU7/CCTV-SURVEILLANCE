import os
import cv2 as cv
import numpy as np
from PIL import Image
base = os.path.dirname(os.path.abspath(__file__))
imag_dir = os.path.join(base,"image_data")
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
y_labels = []
x_train = []
current_id=0
label_ids={}

for root,dirs,files in os.walk(imag_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg"):
            path=os.path.join(root,file)
            label=os.path.basename(root).replace(" ","-").lower()
            print(label,path)

            if not label in label_ids:
                label_ids[label]=current_id
                current_id+=1
            id=label_ids[label]
            print(label_ids)

            pil_image=Image.open(path).convert("L") #grayscale
            img_array= np.array(pil_image,"uint8")
            print(img_array)
            faces=face_cascade.detectMultiScale(img_array, scaleFactor=1.5,minNeighbors=4)

            for (x,y,w,h) in faces:
                roi=img_array[y:y+h,x:x+w]
                cv.imshow("Test",roi)
                cv.waitKey(1)
                x_train.append(roi)
                y_labels.append(id)
                print(y_labels)

