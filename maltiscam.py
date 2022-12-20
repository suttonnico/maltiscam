import cv2
import time

def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

cam = 0
camera_0 = cv2.VideoCapture(cam)

time.sleep(2)
s0, img = camera_0.read()
img = increase_brightness(img,value=20)
cv2.imwrite('maltis.png', img)
