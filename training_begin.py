import cv2
from paddles import detect_paddles
from define_traces import define_trace
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
        frame = cv2.circle(frame, (point[0], point[1]), 2, (255, 0, 0), 50)
        cv2.imshow("img",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    return 1

def point_reched(point,frame):
    bin = detect_paddles(frame)
    reached = False
    for x in range(-3,3):
        for y in range(-3,3):
            if bin[point[1]+x,point[0]+y] == 255:
                reached = True
    return reached
