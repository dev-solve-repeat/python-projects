#pip install opencv-python
#haarcascade_frontalface_deafult.xml
 
import cv2

file = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

camera = cv2.VideoCapture(0) # This will give access to our camera
print(camera)
while True:
    c_rect, d_image = camera.read()
    gray_scale = cv2.cvtColor(d_image, cv2.COLOR_BGR2GRAY)
    file_detection = file.detectMultiScale(gray_scale, 1.3, 6)

    for(x1, y1, w1, h1) in file_detection:
        cv2.rectangle(d_image, (x1, y1), (x1+w1, y1+h1), (255,0, 0), 5)
    
    cv2.imshow("image", d_image)
    h = cv2.waitKey(40) & 0xff
    if h==40:
        break

camera.release()
cv2.destroyAllWindows()




