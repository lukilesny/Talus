import os
import cv2
import time
from paddles import detect_paddles

directory = '/home/michask/talus/zdjecia/'

for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        print(filename)
        img = cv2.imread(r'zdjecia/' + filename)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        cv2.imshow('a', img)
        cv2.imshow('H', detect_paddles(img))
        cv2.waitKey(1000)
