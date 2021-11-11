import cv2


img = cv2.imread('./data/faces/amigos.jpg')     ## Load the image

cv2.imshow('img', img)      ## Show the image
cv2.waitKey(5000)           ## Wait for 5 seconds
cv2.destroyAllWindows()     ## Close all windows