import queue

def define_trace(borders): #borders to rogi x/y min/max
    x1 = borders[0]
    y1 = borders[1]
    x2 = borders[2]
    y2 = borders[3]
    points = []
    points = queue.Queue()
    a = y2-y1 #boki prostokata zasiegu
    b = x2-x1
    p=[None]*15
    
#zbior punktow
    p[0] = [0, 0]
    p[1] = [x1+0.4*b, y1+0*a]
    p[2] = [x1+0.6*b, y1+0*a]
    p[3] = [x1+0*b, y1+0.5*a]
    p[4] = [x1+1*b, y1+0.5*a]
    p[5] = [x1+0.4*b, y1+1*a]
    p[6] = [x1+0.6*b, y1+1*a]
    p[7] = [x1+0.1*b, y1+0.2*a]
    p[8] = [x1+0.2*b, y1+0.1*a]
    p[9] = [x1+0.8*b, y1+0.1*a]
    p[10] = [x1+0.9*b, y1+0.2*a]
    p[11] = [x1+0.2*b, y1+0.8*a]
    p[12] = [x1+0.8*b, y1+0.8*a]
    p[13] = [x1+0.4*b, y1+0.6*a]
    p[14] = [x1+0.6*b, y1+0.6*a]
    
#I
    points.put(p[3])
    points.put(p[4])

    points.put(p[1])
    points.put(p[2])

    points.put(p[5])
    points.put(p[6])

    points.put(p[3])
    points.put(p[4])

#II
    points.put(p[9])
    points.put(p[11])

    points.put(p[8])
    points.put(p[12])

    points.put(p[9])
    points.put(p[11])

    points.put(p[8])
    points.put(p[12])

#III
    points.put(p[1])
    points.put(p[2])

    points.put(p[7])
    points.put(p[10])

    points.put(p[11])
    points.put(p[12])

    points.put(p[5])
    points.put(p[6])

#IV
    points.put(p[6])
    points.put(p[12])

    points.put(p[2])
    points.put(p[10])

    points.put(p[7])
    points.put(p[1])

    points.put(p[11])
    points.put(p[5])

#V
    points.put(p[2])
    points.put(p[10])

    points.put(p[7])
    points.put(p[1])

    points.put(p[9])
    points.put(p[4])

    points.put(p[3])
    points.put(p[8])

#VI
    points.put(p[3])
    points.put(p[4])

    points.put(p[13])
    points.put(p[14])

    points.put(p[3])
    points.put(p[4])

    points.put(p[13])
    points.put(p[14])
    
    
    return points
