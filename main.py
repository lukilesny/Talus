import time
from threading import Timer
from capture_video import capture_video
from questionbox import questionBox
def main():
    starttime = time.time()
    while(True):
        time.sleep(2.0 - ((time.time() - starttime) % 2.0))
        if questionBox():
            capture_video()

if __name__ == "__main__":
    main()

