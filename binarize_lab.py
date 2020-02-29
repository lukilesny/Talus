import os
import cv2
import time
from paddles import binarize_paddles
from kalibracja import detectPaddlesUp
from detect_face import weighted_center_of_face
directory = 'zdjecia_kuchnia/'
import math
for filename in os.listdir(directory):
    if filename.endswith(".bmp"):
        print(filename)
        img = cv2.imread(r'zdjecia_kuchnia/' + filename)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        bin = binarize_paddles(img)

        is_paddles_up = detectPaddlesUp(bin)
        print(is_paddles_up)
        if is_paddles_up:
            face_x, face_y = weighted_center_of_face(img)
            print(face_x,face_y)
            if face_x!=-1 and face_y!=0:
                human_core_y = face_y+int(round(0.5*face_y))
                human_core_x = face_x
                height = len(img)
                width = len(img[0])
                scale_x = int(1.6 * face_y)
                left_point_x=max(human_core_x - scale_x,0)
                left_point_y=0
                right_point_x = min(human_core_x + scale_x,width-1)
                right_point_y = height-1
                img = cv2.circle(img, (face_x, face_y), 15, (255, 0, 0), 2)
                img = cv2.circle(img, (human_core_x, human_core_y), 15, (255, 255, 0), 2)
                img = cv2.rectangle(img, (left_point_x,left_point_y), (right_point_x,right_point_y), (255, 0, 0), 2)
                cv2.imshow('imb', img)
                cv2.waitKey(0)

        cv2.waitKey(200)