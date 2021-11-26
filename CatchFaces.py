import cv2

cap = cv2.VideoCapture(1)       ## 0 for default camera

faceClassif = cv2.CascadeClassifier('./Models/haarcascade_frontalface_default.xml')     ## Load the classifier


while True:     ### While loop to keep the camera on
    ret, frame = cap.read()     ## Read the frame    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   ## Convert to grayscale


    faces = faceClassif.detectMultiScale(gray, 1.1, 5)     ## Detect faces


    for (x, y, w, h) in faces:   ## For each face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)      ## Draw rectangle around the face

    cv2.imshow('img', frame)      ## Show the image
    
    if cv2.waitKey(1) & 0xFF == ord('q'):     ## Wait for 'q' to quit
        break
    
cv2.waitKey(5000)           ## Wait for 5 seconds
cv2.destroyAllWindows()     ## Close all windows