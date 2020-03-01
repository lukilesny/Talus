from detect_face import weighted_center_of_face
import cv2
import math
from paddles import binarize_paddles
from kalibracja import detectPaddlesUp


def camera_configured(cap):
    training_should_start = False
    debug = False
    while (not training_should_start):
        ret, rawframe = cap.read()
        bin = binarize_paddles(rawframe)
        paddles_up = detectPaddlesUp(bin)
        if paddles_up:
            face_x, face_y = weighted_center_of_face(rawframe)
            print(face_x, face_y)
            if face_x != -1 and face_y != 0:
                human_core_y = face_y + int(round(0.5 * face_y))
                human_core_x = face_x
                height = len(rawframe)
                width = len(rawframe[0])
                scale_x = int(1.6 * face_y)
                left_point_x = max(human_core_x - scale_x, 0)+5
                left_point_y = 5
                right_point_x = min(human_core_x + scale_x, width - 1)-5
                right_point_y = height - 6
                if debug:
                    rawframe = cv2.circle(rawframe, (face_x, face_y), 15, (255, 0, 0), 2)
                    rawframe = cv2.circle(rawframe, (human_core_x, human_core_y), 15, (255, 255, 0), 2)
                    rawframe = cv2.rectangle(rawframe, (left_point_x, left_point_y), (right_point_x, right_point_y),
                                             (255, 0, 0), 2)
                    cv2.imshow("window", rawframe)
                    cv2.waitKey(0)
                cv2.destroyAllWindows()
                return [int(round(left_point_x)),int(round( left_point_y)), int(round(right_point_x)), int(round(right_point_y))]

        cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("window", rawframe)
        cv2.imshow("binary", bin)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
