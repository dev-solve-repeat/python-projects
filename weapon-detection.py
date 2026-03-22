import numpy as np
import cv2
import imutils
import datetime

gun_cascade = cv2.CascadeClassifier("cascade.xml")
camera = cv2.VideoCapture(0) #the camera will be on after this - giving access to your camera

firstFrame = None
gunDetected = None

while True:

    ret, frame = camera.read()

    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    weapon = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize = (100,100))

    if len(weapon) > 0:
        gunDetected = True
        
        for (x, y, w, h) in weapon:
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            roi_gray = gray[y: y + h, x: x + w]
            roi_color = frame[y: y + h, x: x + w]
        

        if firstFrame is None:
            firstFrame = gray
            continue

        cv2.imshow("Security Feed", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break

if gunDetected:
    print("Guns Detected")

else:
    print("No Guns Detected")

camera.release()
cv2.destroyAllWindows()


