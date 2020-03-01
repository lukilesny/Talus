import numpy as np
import cv2
from matplotlib import pyplot as plt
from random import seed
from random import randint
from threading import Timer
from paddles import binarize_paddles
from camera_configured import camera_configured
from training_begin import training_begin
import socket
from send_request import send_request
def capture_video():
    cap = cv2.VideoCapture(0)
    tab = camera_configured(cap)
    score = training_begin(cap,tab)
    send_request(socket.gethostname(), score)
    cap.release()
    cv2.destroyAllWindows()
