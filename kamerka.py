import numpy as np
import cv2
from matplotlib import pyplot as plt
from random import seed
from random import randint
from threading import Timer
from paddles import detect_paddles

def show_point(img,x,y):
    img = cv2.line(img, (x - 5, y - 5), (x - 5, y + 5), (255, 0, 0), 2)
    img = cv2.line(img, (x - 5, y - 5), (x + 5, y - 5), (255, 0, 0), 2)
    img = cv2.line(img, (x + 5, y + 5), (x - 5, y + 5), (255, 0, 0), 2)
    img = cv2.line(img, (x + 5, y + 5), (x + 5, y - 5), (255, 0, 0), 2)
    return img

def hello():
    cap = cv2.VideoCapture(0)
    seed(2)
    cnt=0
    ret, rawframe = cap.read()
    frame = cv2.flip(rawframe,1) #odbicie lustrzane
    x_offset = 5
    y_offset = 65
    cv2.imshow("frame",frame)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    x = randint(x_offset, width - x_offset)
    y = randint(y_offset, height - y_offset)
    while(True):
        #cv2.waitKey(1000)
        ret, rawframe = cap.read()
        frame = cv2.flip(rawframe,1) #odbicie lustrzane
        pixel = frame[x, y, :]
        # Get R, G, B values (This are int from 0 to 255)
        red = pixel[2]
        green = pixel[1]
        blue = pixel[0]
        print(red,green,blue)
        if red>200:
            x = randint(x_offset, width - x_offset)
            y = randint(y_offset, height - y_offset)
            print("wchodzę",x,y)
        frame = show_point(frame,x,y)
        cv2.namedWindow("frame", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("frame",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.imshow("frame",detect_paddles(frame))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        cnt += 1
    cap.release()
    cv2.destroyAllWindows()

t = Timer(0, hello)
t.start() # after 5 seconds, "hello, world" will be printed
