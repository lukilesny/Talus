from random import seed
from random import randint
import cv2
import queue
from paddles import detect_paddles

def training_begin (cap, borders):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # odbicie lustrzane
    points = define_trace(borders)
    point = points.get()
    while (not points.empty()):
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)  # odbicie lustrzane
        bin = detect_paddles(frame)
        if point_reched(point,frame):
            point = points.get()
        bin = cv2.circle(bin, (point[0], point[1]), 2, (255, 0, 0), 2)
        cv2.imshow("img",bin)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
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

def point_reched(point,frame):
    bin = detect_paddles(frame)
    reached = False
    for x in range(-3,3):
        for y in range(-3,3):
            if bin[point[1]+x,point[0]+y] == 255:
                reached = True
    return reached
