import cv2
import time



cam = 0
camera_0 = cv2.VideoCapture(cam)

time.sleep(2)
s0, img = camera_0.read()
cv2.imwrite('maltis.png', img)
