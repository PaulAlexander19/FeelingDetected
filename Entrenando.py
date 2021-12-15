import cv2
import os
import numpy as np
import time

def obtenerModelo(facesData,labels, location):
    method = "LBPH"
    emotion_recognizer = cv2.face.LBPHFaceRecognizer_create() ## ceamos el modelo

	# Entrenando el reconocedor de emociones
    print("Entrenando ( "+method+" )...")
    inicio = time.time()
    emotion_recognizer.train(facesData, np.array(labels))
    tiempoEntrenamiento = time.time()-inicio
    print("Tiempo de entrenamiento ( "+method+" ): ", tiempoEntrenamiento)

	# Almacenando el modelo obtenido
    emotion_recognizer.write(location + "/fer2013modelo"+method+".xml")

dataPath = './data.fer2013' 
emotionsList = os.listdir(dataPath)
print('Lista de emociones: ', emotionsList)

labels = []
facesData = []
label = 0

for nameDir in emotionsList:
	emotionsPath = dataPath + '/' + nameDir

	for fileName in os.listdir(emotionsPath):
		#print('Rostros: ', nameDir + '/' + fileName)
		labels.append(label)
		facesData.append(cv2.imread(emotionsPath+'/'+fileName,0))
		#image = cv2.imread(emotionsPath+'/'+fileName,0)
		#cv2.imshow('image',image)
		#cv2.waitKey(10)
	label = label + 1

#obtenerModelo('EigenFaces',facesData,labels)
location = "modelEmotion"
if not os.path.exists(location):
    print('Carpeta creada: ' + location)
    os.makedirs(location)
    
obtenerModelo(facesData,labels, location)