import cv2
import os
import numpy as np

# def getEmotion_recognozer(method="LBPH"):
locationModel = "./modelEmotion"
method = "LBPH"

dataPath = './data' #Cambia a la ruta donde hayas almacenado Data
imagePaths = os.listdir(dataPath)

if(method == "EigenFaces"): 
	emotion_recognizer = cv2.face.EigenFaceRecognizer_create() ## ceamos el modelo

elif(method == "FisherFaces"): 
	emotion_recognizer = cv2.face.FisherFaceRecognizer_create() ## ceamos el modelo

elif(method == "LBPH"): 
	emotion_recognizer = cv2.face.LBPHFaceRecognizer_create() ## ceamos el modelo
else:
	print("No encontrada la emción, trabajando con LBPH") 
	emotion_recognizer = cv2.face.LBPHFaceRecognizer_create() ## ceamos el modelo

emotion_recognizer.read(locationModel +'/modelo'+method+'.xml')

	# return emotion_recognizer
## -----------------------------------

faceClassif = cv2.CascadeClassifier("Models/haarcascade_frontalface_default.xml")


## Metodo para procesar un frame
def detectionEmotion(frame , method="LBPH" ):

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	auxFrame = gray.copy()

	# nFrame = cv2.hconcat([frame, np.zeros((480,300,3),dtype=np.uint8)])

	faces = faceClassif.detectMultiScale(gray,1.2,5)

	for (x,y,w,h) in faces:
		rostro = auxFrame[y:y+h,x:x+w]
		rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
		result = emotion_recognizer.predict(rostro)

		cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)

		# EigenFaces
		if (method == 'EigenFaces'):
			if result[1] < 5700:
				cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
				cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
			else:
				cv2.putText(frame,'No identificado',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
				cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)

	  
		# LBPHFace
		if method == 'LBPH':
			if result[1] < 83:
				cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
				cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
			else:
				cv2.putText(frame,'No identificado',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
				cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)

		# FisherFace
		if method == 'FisherFaces':
			if result[1] < 500:
				cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
				cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
			else:
				cv2.putText(frame,'No identificado',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
				cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
        
	return frame
   
def main():
	# ----------- Métodos usados para el entrenamiento y lectura del modelo ----------
	method = 'LBPH'
	locationModel = "./modelEmotion"

	if(method == "EigenFaces"): 
		emotion_recognizer = cv2.face.EigenFaceRecognizer_create() ## ceamos el modelo

	elif(method == "FisherFaces"): 
		emotion_recognizer = cv2.face.FisherFaceRecognizer_create() ## ceamos el modelo

	elif(method == "LBPH"): 
		emotion_recognizer = cv2.face.LBPHFaceRecognizer_create() ## ceamos el modelo
	else:
		print("No encontrada la emción, trabajando con LBPH") 
		emotion_recognizer = cv2.face.LBPHFaceRecognizer_create() ## ceamos el modelo


	emotion_recognizer.read(locationModel +'/modelo'+method+'.xml')
	# --------------------------------------------------------------------------------

	dataPath = './data' #Cambia a la ruta donde hayas almacenado Data
	imagePaths = os.listdir(dataPath)
	print('emotionPaths=',imagePaths)

	cap = cv2.VideoCapture(1)

	faceClassif = cv2.CascadeClassifier('./Models/haarcascade_frontalface_default.xml') 

	while True:
		
		# print(cap)
		
		ret,frame = cap.read()
		# if ret == False: break ## OJO
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		auxFrame = gray.copy()

		# nFrame = cv2.hconcat([frame, np.zeros((480,300,3),dtype=np.uint8)])

		faces = faceClassif.detectMultiScale(gray,1.2,5)

		for (x,y,w,h) in faces:
			rostro = auxFrame[y:y+h,x:x+w]
			rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
			result = emotion_recognizer.predict(rostro)

			cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)

			# EigenFaces
			if (method == 'EigenFaces'):
				if result[1] < 5700:
					cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
					cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
				else:
					cv2.putText(frame,'No identificado',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
					cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)

		
			# LBPHFace
			if method == 'LBPH':
				if result[1] < 83:
					cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
					cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
				else:
					cv2.putText(frame,'No identificado',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
					cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)

			# FisherFace
			if method == 'FisherFaces':
				if result[1] < 500:
					cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
					cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
				else:
					cv2.putText(frame,'No identificado',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
					cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
			
		cv2.imshow('Frande',frame)
		k = cv2.waitKey(1)
		if k == 27:
			break

	cap.release()
	cv2.destroyAllWindows()

if __name__ == "__main__":
    main()