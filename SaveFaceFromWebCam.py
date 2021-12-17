import cv2
import os

def safeFaceForVideoWebcam(frame, emotion):
# location = "../DataVideos"
# if not os.path.exists('Rostros encontradosHap'):
# 	print('Carpeta creada: Rostros encontrados')
# 	os.makedirs('Rostros encontrados2')

	emotionLocation = "./data"

	faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
	countTotal = 0
	count = 0

	frame = cv2.flip(frame,1)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	auxFrame = frame.copy()

	faces = faceClassif.detectMultiScale(gray, 1.3, 4)
 
	# cv2.imshow('Video',frame)
	countTotal = len(os.listdir(emotionLocation+"/"+emotion)) + 1
	
	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
		rostro = auxFrame[y:y+h,x:x+w]
		rostro = cv2.resize(rostro,(150,150), interpolation=cv2.INTER_CUBIC)
		# if k == ord('s'):
		k = cv2.waitKey(1)
		if (k == ord('s')):
			print("Guardando rostro")
			cv2.imwrite( emotionLocation+"/"+emotion+"/"+emotion+'_{}.jpg'.format(countTotal),rostro)
			cv2.imshow('rostro',rostro)
			count = count +1
			countTotal += 1

	cv2.rectangle(frame,(10,5),(450,25),(255,255,255),-1)
	cv2.putText(frame,'Presione s, para almacenar los rostros encontrados',(10,20), 2, 0.5,(128,0,255),1,cv2.LINE_AA)	
  
	return frame