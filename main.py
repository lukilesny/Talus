import time
from threading import Timer
from capture_video import capture_video
from questionbox import questionBox
from send_request import send_request
import socket
def main():
    starttime = time.time()
    while(True):
        time.sleep(2.0 - ((time.time() - starttime) % 2.0))
        if questionBox():
            capture_video()
        else:
            send_request(socket.gethostname(), 0)
if __name__ == "__main__":
    main()

