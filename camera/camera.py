import numpy as np
import cv2
# importing os module   
import os 

cap = cv2.VideoCapture(0)
path = r'C:\Users\Administrator\Documents\Beemo\camera\image'
cascPath = "haarcascade_frontalface_default.xml"
img_counter = 0

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
        #flags = cv2.CV_HAAR_SCALE_IMAGE
    )

    #print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    
    k = cv2.waitKey(1)
    if k & 0xFF == ord('q'):
        break
    elif k & 0xFF == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(os.path.join(path , img_name), frame)
        print("{} written!".format(img_name))
        img_counter += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()