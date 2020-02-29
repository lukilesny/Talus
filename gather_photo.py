import cv2
import time
cap = cv2.VideoCapture(0)
for i in range(1,1000):
    ret, rawframe = cap.read()
    cv2.imwrite(r'zdjecia_kuchnia/'+str(i)+r'.bmp', rawframe)
    cv2.imshow("binary", rawframe)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    print(i)