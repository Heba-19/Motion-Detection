import cv2
# using Haar Cascade Classifiers
face_rec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# in the '' post photo name
img = cv2.imread('image.jpg')
g = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_rec.detectMultiScale(g,1.1,5)
for (a, b, c, d) in faces:
    # (255, 153, 255) this code is for pink color and you can visit opencv color number to get mor
    cv2.rectangle(img, (a, b), (a + c, b + d), (255, 153, 255), 2)
cv2.imshow('img',img)
cv2.waitKey()