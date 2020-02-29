from random import seed
from random import randint
import cv2
import queue

def training_begin(cap,borders):
    ret, frame = cap.read()
    points = define_trace(borders)
    while (not points.empty()):
        point = points.get()
        ret, frame = cap.read()
        frame = cv2.circle(frame, (point[0], point[1]), 2, (255, 0, 0), 2)
        cv2.imshow("img",frame)
        cv2.waitKey(1000)
    return 1
def define_trace(borders):
    x_min = borders[0]
    y_min = borders[1]
    x_max = borders[2]
    y_max = borders[3]
    points = []
    seed(2)
    points = queue.Queue()
    for i in range(0,50):
        x = randint(x_min,x_max)
        y = randint(y_min,y_max)
        points.put([x, y])
    return points