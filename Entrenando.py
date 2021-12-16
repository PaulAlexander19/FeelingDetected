import cv2
import os
import numpy as np
import time

def obtenerModelo(facesData,labels, location, method="LBPH" ):
    # emotion_recognizer = None
    if(method == "EigenFaces"): 
        emotion_recognizer = cv2.face.EigenFaceRecognizer_create() ## ceamos el modelo
    
    elif(method == "FisherFaces"): 
        emotion_recognizer = cv2.face.FisherFaceRecognizer_create() ## ceamos el modelo
    
    elif(method == "LBPH"): 
        emotion_recognizer = cv2.face.LBPHFaceRecognizer_create() ## ceamos el modelo
    else:
        print("No encontrada la emción, trabajando con LBPH") 
        emotion_recognizer = cv2.face.LBPHFaceRecognizer_create() ## ceamos el modelo
    

	# Entrenando el reconocedor de emociones
    print("Entrenando ( "+method+" )...")
    inicio = time.time()
    emotion_recognizer.train(facesData, np.array(labels))
    tiempoEntrenamiento = time.time()-inicio
    print("Tiempo de entrenamiento ( "+method+" ): ", tiempoEntrenamiento)

	# Almacenando el modelo obtenido
    emotion_recognizer.write(location + "/modelo"+method+".xml")

dataPath = './data' 
emotionsList = os.listdir(dataPath)
print('Lista de emociones: ', emotionsList)

labels = []
facesData = []
label = 0

for nameDir in emotionsList:
	emotionsPath = dataPath + '/' + nameDir

	for fileName in os.listdir(emotionsPath):
		#print('Rostros: ', nameDir + '/' + fileName)
		labels.append(label) ## Wl codigo de la emocion
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
    
obtenerModelo(facesData,labels, location, method="LBPH")
# obtenerModelo(facesData,labels, location, method="FisherFaces")
# obtenerModelo(facesData,labels, location, method="EigenFaces")