import numpy as np
import cv2
from matplotlib import pyplot as plt
from random import seed
from random import randint
from threading import Timer
from paddles import binarize_paddles
from camera_configured import camera_configured
from training_begin import training_begin

def capture_video():
    cap = cv2.VideoCapture(0)
    tab = camera_configured(cap)
    # score = training_begin(cap)
    #print(x_min, y_min, x_max, y_max)340 240
    ret, rawframe = cap.read()
    cv2.rectangle(rawframe, (150, 100), (500, 400), (255, 0, 0), 2)
    #cv2.circle(rawframe, (human_core_x, human_core_y), 20, (0, 0, 255), 2)

    cv2.imshow("frame", rawframe)
    cv2.waitKey(0)
    score = training_begin(cap,tab)
    cap.release()
    cv2.destroyAllWindows()
