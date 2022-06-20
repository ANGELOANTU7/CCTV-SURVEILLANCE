
# CCTV-SURVEILLANCE

This software can automatically detect an anomaly in CCTV live footage , and store the face ids and number-plate of vehicles


In control rooms, there are multiple CCTV footage shown together, this method is not very effective as giving individual attention to each live footage at a time is very difficult. Despite so much surveillance, the crime rates are increasing. The problem is that inspecting several hundreds and thousands of videos is a very laborious and time-intensive task. Typically, they are only examined after a crime has occurred to find crime scene evidence, which is extremely inefficient considering the amount of footage. This manual task provides evidence in court but is rarely used to prevent crime or react to it in real-time. To solve this problem, we have created a CCTV monitoring system, which individually checks all footage for suspicious activity and stores face IDs and number plates present in the footage. 
## Demo

[YOUTUBE LINK](https://youtu.be/pt0ZVQ-Dxkw)


## Features

![alt text](https://drive.google.com/file/d/12zSSx6Ww-E1Og6wbzaWXuF7jITk4rnF0/view?usp=sharing)
- Detects any suspicious activity
- Stores all the faces detected
- Recognize criminal faces
- Stores number-plate


## Deployment

1.Download the model via Google Drive:
[weight.hdf5](https://drive.google.com/file/d/1er2SP2aAfNzomZ3AvnEjsBdxfdHYSjYY/view?usp=sharing)
[model.weights](https://drive.google.com/file/d/1qBFdDdv-gU7KKeqcCElDkwIszVttm8TW/view?usp=sharing)

2.To deploy this project run these four program simultaneously

**before uploading......**
app.py

**after uploading.....**
AANeuralNetwork.py
AAnumberplate_detection.py --video=uploads/video.mp4
AAFacedetection_recognition.py



## Model

#### Base Model - VGG16



| Epoch | Labels    | Accuracy(to exactly tell what is happening)| Accuracy(Suspious/Normal)                |
| :-------- | :------- | :------------------------- | :--------------------
| 50 | 12 | 31.111 | 63.33 |


## Labels

| Serial No.| Labels    |
| :-------- | :------- 
| 1 | Abuse | 
| 2 | Arrest |
| 3 | Assault | 
| 4 | Burglary | 
| 5 | Explosion | 
| 6 | Fighting | 
| 7 | Normal | 
| 8 | RoadAccident | 
| 9 | Robbery | 
| 10 | Shooting | 
| 11 | Shoplifting | 
| 12 | Stealing | 
| 13 | Vandalism | 


## DATASET USED

 - [UCF crminal database](https://www.crcv.ucf.edu/projects/real-world/)


## Tech Stack

TensorFlow,OpenCV,Neural Network,Deep Learning,HTML/CSS,Bootstrap,Keras,Object Detection,JavaScript

## Challenges we ran into

The first hurdle we faced was finding a good database to make a deep learning model which would serve the purpose of detecting suspicious activity in the footage, we finally found a criminal database by UCF, and we had to make the model from scratch.

The second hurdle we faced was making the model using such a huge amount of database, as it required more and more system requirements, finally, we decided to go with the best prototype possible with the current system

the third hurdle we faced was not having a criminal faceID database to identify the criminals, still, we created the face recognition software using OpenCV and pre-build ML, in which we have trained famous criminal faces to show its working

As we are first years understanding ML and its implementation took time, therefore we had to make the UI and Video Demo in a short span of time.



