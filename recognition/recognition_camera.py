# face_recognition.py : test of face recognition
# thanks to https://qiita.com/opto-line/items/7ade854c26a50a485159
# thanks to https://chusotsu-program.com/opencv-frontalface/
import cv2
import sys
import os

# preparation for face face_recognition
# cascade_file = 'cascade.xml'
cascade_file = 'C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml'
if len(sys.argv) >= 2 and os.path.isfile(sys.argv[1]):
    cascade_file = sys.argv[1]

print("Cascade file : " + cascade_file)

cascade_face = cv2.CascadeClassifier(cascade_file)
border_color = (0, 0, 255)
border_size = 2

# get VideoCapture object
capture = cv2.VideoCapture(0)


while(True):
    ret, frame = capture.read()
    # resize the window
    windowsize = (800, 600)
    frame = cv2.resize(frame, windowsize)

    # find face
    face_list = cascade_face.detectMultiScale(frame, minSize=(20,20))
    for (x, y, w, h) in face_list:
        cv2.rectangle(frame, (x, y), (x+w, y+h), border_color, thickness=border_size)

    cv2.imshow('title', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
