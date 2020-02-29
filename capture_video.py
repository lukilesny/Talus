import numpy as np
import cv2
from matplotlib import pyplot as plt
from random import seed
from random import randint
from threading import Timer
from paddles import detect_paddles

def capture_video():
    camera_configured = False
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    camera_configured(cap)
    score = training_begin(cap)
    cap.release()
    cv2.destroyAllWindows()