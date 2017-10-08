import cv2
import numpy as np
import sys
import os
import random
import time
cap = cv2.VideoCapture(1)
imgNum = 0 
dirr = str(random.randrange(0,200000))
os.system(str("mkdir -p /home/harambe/cs/faceLock/knownFaces/"+str(dirr)))
fileName= str( str(dir) +"/number"+ str(imgNum)+ ".png")
xmlPath = "/home/harambe/cs/faceLock/opencv-3.1.0/data/haarcascades/haarcascade_frontalface_default.xml"
face_cascade= cv2.CascadeClassifier(str(xmlPath))

while imgNum <10:
	faces = None
	ret, frame = cap.read()
	GRAY = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(GRAY,scaleFactor =1.2, minNeighbors=5)
	if len(faces) != 0:
	#	cv2.rectangle(GRAY, (x, y), (x+w, y+h), (0, 255, 0), 2)		
		fileName= str("./knownFaces/" + str(dirr) +"/number"+ str(imgNum)+ ".png")
		print fileName
		cv2.imwrite(str(fileName), frame)
		imgNum +=1	
		time.sleep(.25)
cap.release()
cv2.destroyAllWindows()






