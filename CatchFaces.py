import cv2

faceClassif = cv2.CascadeClassifier('./Models/haarcascade_frontalface_default.xml')     ## Load the classifier
img = cv2.imread('./data/faces/amigos.jpg')     ## Load the image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   ## Convert to grayscale


faces = faceClassif.detectMultiScale(gray,
                                    scaleFactor=1.1,    ## Scale factor
                                    minNeighbors=5,     ## Minimum neighbors
                                    minSize=(30, 30),   ## Minimum size
                                    maxSize=(80, 80))   ## Maximum size


for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)      ## Draw rectangle around the face

cv2.imshow('img', img)      ## Show the image
cv2.waitKey(5000)           ## Wait for 5 seconds
cv2.destroyAllWindows()     ## Close all windows