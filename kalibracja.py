import numpy as np

def detectPaddlesUp(frame):
    # {
    height= len(frame)
    width = len(frame[0])

    width_min = int(0.25*width)
    width_max = int(0.75*width)
    height_max = int(0.05*height)
    area = (width_max-width_min)*height_max

    table = frame[0:height_max,width_min:width_max]
    sum = int(np.sum(table)/255)

    if(sum>area/6):
        return 1
    else:
        return 0
	# }
