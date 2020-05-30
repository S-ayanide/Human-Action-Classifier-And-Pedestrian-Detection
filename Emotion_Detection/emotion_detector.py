# -*- coding: utf-8 -*-

from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier('D:\Github\Human-Action-Classifier-And-Pedestrian-Detection\Emotion_Detection\haarcascade_frontalface_default.xml')
classifier =load_model('D:\Github\Human-Action-Classifier-And-Pedestrian-Detection\Emotion_Detection\Emotion_little_vgg.h5') # To predict

class_labels = ['Angry','Happy','Neutral','Sad','Surprise']

mean_store_rating = 50 #On a scale of 1-100, 50 being neutral store rating
frames = 1
    
cap = cv2.VideoCapture(0)

while True:
    # Grab a single frame of video
    ret, frame = cap.read()
    labels = []
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)
        # rect,face,image = face_detector(frame)


        if np.sum([roi_gray])!=0:
            roi = roi_gray.astype('float')/255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi,axis=0)

        # make a prediction on the ROI, then lookup the class

            preds = classifier.predict(roi)[0]            
            label=class_labels[preds.argmax()]            
            
            # Get average store rating
            
            if(label == None):
                pass
                
            if(label == 'Happy'):                 
                mean_store_rating += frames/100
                
            if(label == 'Neutral' or label == 'Surprised'):
                pass
                
            if(label == 'Angry' or label == 'Sad'):
                mean_store_rating -= frames/100    
            print(mean_store_rating)
            
            label_position = (x,y)
            cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
        else:
            cv2.putText(frame,'No Face Found',(20,60),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
    cv2.imshow('Emotion Detector',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()