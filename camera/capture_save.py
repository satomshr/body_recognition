# capture_save.py : test of camera capture & image save
# thanks to https://qiita.com/opto-line/items/7ade854c26a50a485159
# thanks to https://note.nkmk.me/python-opencv-camera-to-still-image/
import cv2
import os

# current directory
dir = os.getcwd()
bname = os.path.join(dir, "file")
ext = ".jpg"
n = 0

# VideoCapture オブジェクトを取得します
capture = cv2.VideoCapture(0)

while(True):
    ret, frame = capture.read()
    # resize the window
    windowsize = (800, 600)
    frame = cv2.resize(frame, windowsize)

    cv2.imshow('title', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('c'):
        cv2.imwrite('{}_{}{}'.format(bname, n, ext), frame)
        n += 1
    elif key == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
