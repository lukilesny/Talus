import cv2
import numpy as np


def detect_paddles(rgb_image):
    hsv = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2HSV)
    lower_range = np.array([0, 105, 105])
    upper_range = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_range, upper_range)
    lower_range = np.array([170, 105, 105])
    upper_range = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_range, upper_range)

    return mask1+mask2
