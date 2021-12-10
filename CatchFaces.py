import cv2
import os
import imutils

#emotionName = "Happy"   # Nombre de la emocion 
#emotionName = "Angry"   # Nombre de la emocion
#emotionName = "Sad"     # Nombre de la emocion
#emotionName = "Surprised"   # Nombre de la emocion
emotionName = "Serius"   # Nombre de la emocion

dataPath = "./data"     # Ruta de la carpeta donde se guardaran las imagenes
emotionPath = dataPath + "/" + emotionName
## Crear el directorio
if not os.path.exists(emotionPath):
    print("Carpeta creada")
    os.makedirs(emotionPath)
    
cap = cv2.VideoCapture(0)       ## 0 for default camera

faceClassif = cv2.CascadeClassifier('./Models/haarcascade_frontalface_default.xml')     ## Load the classifier


count = 0
countName = len(os.listdir(emotionPath))
print(count)
maxImageCount = 300

while True:     ### While loop to keep the camera on
    ret, frame = cap.read()     ## Read the frame    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   ## Convert to grayscale
    
    auxFrame = frame.copy()    

    faces = faceClassif.detectMultiScale(gray, 1.18, 5)     ## Detect faces
  
    
    for (x, y, w, h) in faces:   ## For each face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)      ## Draw rectangle around the face
        rostro = auxFrame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
        
        # if k == ord('s'):
        cv2.imwrite( emotionPath+ "/rostro_{}.jpg".format(countName), rostro)
        cv2.imshow("rostro", rostro)
        count += 1
        countName += 1
        
    k = cv2.waitKey(1)
    if k == 27 or count >= maxImageCount:
        break
        
    cv2.imshow('CamaraWeb', frame)      ## Show the image
    
   
    
cv2.waitKey(5000)           ## Wait for 5 seconds
cv2.destroyAllWindows()     ## Close all windows