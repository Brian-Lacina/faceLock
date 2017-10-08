import cv2
import numpy as mp
import os 
import sqlite3
cap = cv2.VideoCapture(1)


xmlPath = "/home/harambe/cs/faceLock/opencv-3.1.0/data/haarcascades/haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(str(xmlPath))
while True:
    ret, frame = cap.read();
    GRAY = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(GRAY,scaleFactor =1.2, minNeighbors=5)
    for (x, y, w, h) in faces:
   	 cv2.rectangle(GRAY, (x, y), (x+w, y+h), (0, 255, 0), 2) 
    cv2.imshow('GRAY', GRAY)
    if cv2.waitKey(1) & 0xff == ord('q'):
	 break

cap.release()
cv2.destroyAllWindows()
