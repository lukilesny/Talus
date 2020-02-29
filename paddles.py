import cv2
import numpy as np


def detect_paddles(rgb_image):
    hsv = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2HSV)
    lower_range = np.array([0, 100, 100])
    upper_range = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_range, upper_range)
    lower_range = np.array([170, 100, 100])
    upper_range = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_range, upper_range)

    lower_range = np.array([0, 0, 250])
    upper_range = np.array([255, 255, 255])
    mask3 = cv2.inRange(rgb_image, lower_range, upper_range)
    mask = cv2.bitwise_and(mask1 + mask2, mask3)
    return mask1+mask2
