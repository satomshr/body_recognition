# recognition_image.py : test of recognition
# thanks to https://qiita.com/opto-line/items/7ade854c26a50a485159
# thanks to https://chusotsu-program.com/opencv-frontalface/
import cv2
import sys
import os


# cascade_file = 'C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml'
if len(sys.argv) == 1:
    print("Usage : python recognition_image.py cascade_file.xml img1 img2..")
    sys.exit()

# read cascade file
cascade_file = sys.argv[1]
print("Cascade file : " + cascade_file)

cascade_face = cv2.CascadeClassifier(cascade_file)
border_color = (0, 0, 255)
border_size = 2

# check each image file
for img_file in sys.argv[2:]:
    img = cv2.imread(img_file)
    face_list = cascade_face.detectMultiScale(img, minSize=(20,20))
    for (x, y, w, h) in face_list:
        cv2.rectangle(img, (x, y), (x+w, y+h), border_color, thickness=border_size)
    cv2.imshow(sys.argv[0], img)
    cv2.waitKey(0)

cv2.destroyAllWindows()
