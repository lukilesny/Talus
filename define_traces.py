from random import seed
from random import randint
import queue
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