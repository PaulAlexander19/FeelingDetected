import cv2


img = cv2.imread('./data/faces/amigos.jpg')     ## Load the image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   ## Convert to grayscale

cv2.imshow('img', gray)      ## Show the image
cv2.waitKey(5000)           ## Wait for 5 seconds
cv2.destroyAllWindows()     ## Close all windows