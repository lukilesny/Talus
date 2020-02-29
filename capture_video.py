import numpy as np
import cv2
from matplotlib import pyplot as plt
from random import seed
from random import randint
from threading import Timer
from paddles import detect_paddles
from training_begin import training_begin

def capture_video():
    camera_configured = False
    cap = cv2.VideoCapture(0)
    #camera_configured(cap)
    tab = [100,100,400,400]
    score = training_begin(cap,tab)
    cap.release()
    cv2.destroyAllWindows()