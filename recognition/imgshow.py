# imgshow.py ; test of image show
# author ; sato.mshr@gmail.com

import cv2
import sys

img_file = sys.argv[1]
img = cv2.imread(img_file)
cv2.imshow(img_file, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
