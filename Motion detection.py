import cv2
cap = cv2.VideoCapture(0)# 0 is a defualt value to access your cam ,you can post video name
success, frame_1 = cap.read()
success, frame_2 = cap.read()

while True:
    diffrence =cv2.absdiff(frame_1,frame_2)
    g = cv2.cvtColor(diffrence, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(g,(5,5),0)
    _, threesh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(threesh, None,iterations=1)
    contours, _ =cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cont in contours:
        (x, y, w, h) = cv2.boundingRect(cont)
        if cv2.contourArea(cont) >1000:
            continue
        cv2.rectangle(frame_1,(x,y),(x+w,y+h),(0, 255, 0),3)
        cv2.putText(frame_1,"Status: {}".format("Movement"),(10,20),cv2.FONT_HERSHEY_SIMPLEX,
                    2,(255,0,0),2)
    cv2.drawContours(frame_1, contours, -1, (0, 255, 0), 2)#-1 apply all contours
    cv2.imshow("Video",frame_1)
    frame_1 = frame_2
    success, frame_2 = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break