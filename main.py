import time
from threading import Timer
from capture_video import capture_video
def main():
    starttime = time.time()
    while(True):
        time.sleep(2.0 - ((time.time() - starttime) % 2.0))
        capture_video()
        print('wyskoczylem na maina')

if __name__ == "__main__":
    main()

