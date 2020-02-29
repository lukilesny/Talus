import cv2
import numpy as np


def binarize_paddles(rgb_image):
    hsv = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2HSV)
    lower_range = np.array([0, 95, 95])
    upper_range = np.array([13, 255, 255])
    mask1 = cv2.inRange(hsv, lower_range, upper_range)
    lower_range = np.array([165, 95, 95])
    upper_range = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_range, upper_range)
    pre_bin = mask1+mask2
    median = cv2.medianBlur(pre_bin, 15)
    return median
