import cv2
import os

dataFinalPath = "data.procesado"
dataPath = "./data.new"
emotionsList = os.listdir(dataPath)

# Cambia a la ruta donde hayas almacenado la carpeta con las imágenes

if not os.path.exists(dataFinalPath):
    print('Carpeta creada: ' + dataFinalPath)
    os.makedirs(dataFinalPath)

faceClassif = cv2.CascadeClassifier(
    cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

count = 0
for nameDir in emotionsList:
    imagePath = dataPath + '/' + nameDir

    if not os.path.exists(dataFinalPath+'/'+nameDir):
        print('Carpeta creada:' + nameDir)
        os.makedirs(dataFinalPath+'/' + nameDir)

    for imageName in os.listdir(imagePath):
        image = cv2.imread(imagePath+'/'+imageName)
        # image2 = cv2.imread("./data/Angry/rostro_0.jpg")
        # print(imagePath+'/'+imageName)
        # print(dir(image))
        cv2.imshow('test',image)
        # # cv2.imshow('test',image2)
        
        # k = cv2.waitKey(0)
        # if k == ord('s'):
        #    break

        # -----------
        imageAux = image.copy()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = faceClassif.detectMultiScale(gray, 1.05, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (128, 0, 255), 2)
        cv2.rectangle(image, (10, 5), (450, 25), (255, 255, 255), -1)

        print(faces)
        # k = cv2.waitKey(0)
        # if k == ord('s'):
        #    continue

        # cv2.putText(image,'Presione s, para almacenar los rostros encontrados',(10,20), 2, 0.5,(128,0,255),1,cv2.LINE_AA)
        # k = cv2.waitKey(0)
        # if k == ord('s'):
        #     break
        # else:
        for (x, y, w, h) in faces:
            rostro = imageAux[y:y+h, x:x+w]
            print("dentro")
            rostro = cv2.resize(rostro, (150, 150),
                                interpolation=cv2.INTER_CUBIC)
            # cv2.imshow('test',rostro)
            # k = cv2.waitKey(0)
            # if k == ord('s'):
            #    break

            # cv2.imshow('rostro',rostro)
            # cv2.waitKey(0)
            print(nameDir)
            cv2.imwrite(dataFinalPath+"/"+nameDir +
                        "/rostro_{}.jpg".format(count), rostro)
            count = count + 1
            print("guardando en " + dataFinalPath+'/' + nameDir)

cv2.destroyAllWindows()
