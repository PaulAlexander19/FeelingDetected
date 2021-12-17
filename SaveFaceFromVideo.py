import cv2
import os

def safeFaceForVideo(frame, emotion):
	emotionLocation = "./data"


	faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
	countTotal = 0
	count = 0
	frame = cv2.flip(frame,1)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	auxFrame = frame.copy()

	faces = faceClassif.detectMultiScale(gray, 1.3, 4)

	countTotal = len(os.listdir(emotionLocation+"/"+emotion)) + 1
	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y),(x+w,y+h),(128,0,255),2)
		rostro = auxFrame[y:y+h,x:x+w]
		rostro = cv2.resize(rostro,(150,150), interpolation=cv2.INTER_CUBIC)
		cv2.imwrite( emotionLocation+"/"+emotion+"/"+emotion+'_{}.jpg'.format(countTotal),rostro)
		cv2.imshow('rostro',rostro)
		count = count +1
		countTotal += 1
	
	return frame
