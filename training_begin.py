import cv2
from paddles import binarize_paddles
from define_traces import define_trace
from random import seed
from random import randint
import time
def training_begin (cap, borders):
    seed(5)
    start_time = time.time()
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # odbicie lustrzane
    points = define_trace(borders)
    point1 = points.get()
    point2 = points.get()
    points.put([10000,10000])
    points.put([10000,10000])
    while (not points.empty()):
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)  # odbicie lustrzane
        bin = binarize_paddles(frame)
        if point_reched(point1,frame) and point_reched(point2,frame) and not points.empty():
            point1 = points.get()
            point2 = points.get()
        if point1[0] < 2000:
            frame = cv2.circle(frame, (point1[0], point1[1]), 2, (0, 255, 255), 20)
            frame = cv2.circle(frame, (point2[0], point2[1]), 2, (0, 255, 255), 20)

        cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("window",frame)
        if cv2.waitKey(1) & 0xFF == ord('e'):
            end_time = time.time()
            return count_score(start_time, end_time)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    end_time = time.time()
    return count_score(start_time, end_time)

def point_reched(point,frame):
    bin = binarize_paddles(frame)
    reached = False
    for x in range(-3,3):
        for y in range(-3,3):
            if bin[point[1]+x,point[0]+y] == 255:
                reached = True
    return reached
def count_score(start_time, end_time):
    score = 100 - (end_time - start_time)
    if score < 0:
        score = randint(0, 100)
    print(int(score))
    return int(score)
