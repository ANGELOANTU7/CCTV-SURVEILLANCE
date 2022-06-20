import keras
from keras.models import Sequential
from keras.applications.vgg16 import VGG16
from keras.layers import Dense, InputLayer, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D, GlobalMaxPooling2D
from keras.preprocessing import image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import tensorflow as tf
import cv2
from glob import glob
import math,os
import statistics as s
import csv



stat=2
size=0
abuse=0
arrest=0
assault=0
burglary=0
explosion=0
fighting=0
normal=0
roadaccident=0
robbery=0
shooting=0
shoplifting=0
stealing=0
vandalism=0

from keras import models    
base_model = VGG16(weights='imagenet', include_top=False)
model = models.load_model('weight.hdf5')

# creating two lists to store predicted and actual tags
predict = []
with open("static/data/stream.csv",'w') as f:
    csv.writer(f).writerow([stat,size,abuse,arrest,assault,burglary,explosion,fighting,normal,roadaccident,robbery,shooting,shoplifting,stealing,vandalism])
    f.close()
cc=0
count=0
videof=glob("uploads/*.mp4")
cap= cv2.VideoCapture(videof[0])
i=0
count=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('temp/_frame'+str(i)+'.jpg',frame)
    count += 30 # i.e. at 30 fps, this advances one second
    cap.set(cv2.CAP_PROP_POS_FRAMES, count)
    i+=1

cap.release()
cv2.destroyAllWindows()

# reading all the frames from temp folder
images = glob("temp/*.jpg")

prediction_images = []
for i in range(len(images)):
    img = image.load_img(images[i], target_size=(224,224,3))
    img = image.img_to_array(img)
    img = img/255
    prediction_images.append(img)



# converting all the frames for a test video into numpy array
prediction_images = np.array(prediction_images)
# extracting features using pre-trained model

prediction_images = base_model.predict(prediction_images)

# converting features in one dimensional array
prediction_images = prediction_images.reshape(prediction_images.shape[0], 7*7*512)
# predicting tags for each array

pre=model.predict(prediction_images)
prediction = np.argmax(pre,axis=1)
print(prediction)
#print(s.mode(prediction))
# appending the mode of predictions in predict list to assign the tag to the video

# appending the actual tag of the video
#print(videoFile.split('_')[0].split('0')[0])

size=len(prediction)
for a in prediction:
    if a==0:
        abuse=abuse+1
    if a==1:
        arrest=arrest+1
    if a==2:
        assault=assault+1
    if a==3:
        burglary=burglary+1
    if a==4:
        explosion=explosion+1
    if a==5:
        fighting=fighting+1
    if a==6:
        normal=normal+1
    if a==7:
        roadaccident=roadaccident+1
    if a==8:
        robbery=robbery+1
    if a==9:
        shooting=shooting+1
    if a==10:
        shoplifting=shoplifting+1
    if a==11:
        stealing=stealing+1
    if a==12:
        vandalism=vandalism+1
        
        
if (abuse+arrest+assault+burglary+explosion+fighting+roadaccident+robbery+shooting+shoplifting+stealing+vandalism)>normal:
    print("suspicious")
    stat=1
    
else:
    print("normal")
    stat=0
    
with open("static/data/stream.csv",'w') as f:
    csv.writer(f).writerow([stat,size,abuse,arrest,assault,burglary,explosion,fighting,normal,roadaccident,robbery,shooting,shoplifting,stealing,vandalism])
    f.close()

