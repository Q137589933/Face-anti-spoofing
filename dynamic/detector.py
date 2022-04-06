import cv2
from imutils import face_utils
from scipy.spatial import distance as dist
import dynamic.inter_config as inter_cfg


class detector():
    def __init__(self, detector, face_pos_detector):
        # cargar modelo para detection de puntos de ojos
        self.detector = detector
        self.face_pos_detector = face_pos_detector

    def mouth_open(self, img,rect, COUNTER, TOTAL):
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        shape = self.detector(gray, rect)
        shape = face_utils.shape_to_np(shape)
        (mStart, mEnd) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]
        mouth = shape[mStart:mEnd]
        inside_MAR, outside_MAR = self.mouse_aspect_ratio(mouth)
        if (inside_MAR > 0.7) or (outside_MAR > 0.3):
            COUNTER += 1
        else:
            if COUNTER >= cfg.EYE_AR_CONSEC_FRAMES:
                TOTAL += 1
        return COUNTER, TOTAL

    def eye_blink(self, img,rect, COUNTER, TOTAL):
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # determine the facial landmarks for the face region, then
        # convert the facial landmark (x, y)-coordinates to a NumPy
        # array
        shape = self.detector(gray, rect)
        shape = face_utils.shape_to_np(shape)
        (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
        (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        leftEAR = self.eye_aspect_ratio(leftEye)
        rightEAR = self.eye_aspect_ratio(rightEye)
        EAR = (leftEAR + rightEAR) / 2.0
        if EAR < inter_cfg.EYE_AR_THRESH:  # 如果ear大于thresh 就表示该帧在眨眼
            COUNTER += 1
        else:  # 如果该帧没在眨眼 统计之前有多少帧在眨眼 如果帧数够多 就记为眨眼一次 眨眼次数够多即可认定为真人
            # if the eyes were closed for a sufficient number of
            # then increment the total number of blinks
            if COUNTER >= inter_cfg.EYE_AR_CONSEC_FRAMES:
                TOTAL += 1
            # reset the eye frame counter
            COUNTER = 0
        return COUNTER, TOTAL

    def eye_aspect_ratio(self, eye):
        # compute the euclidean distances between the two sets of
        # vertical eye landmarks (x, y)-coordinates
        A = dist.euclidean(eye[1], eye[5])
        B = dist.euclidean(eye[2], eye[4])
        # compute the euclidean distance between the horizontal
        # eye landmark (x, y)-coordinates
        C = dist.euclidean(eye[0], eye[3])
        # compute the eye aspect ratio
        ear = (A + B) / (2.0 * C)
        # return the eye aspect ratio
        return ear

    def mouse_aspect_ratio(self, mouth):
        # ("mouth", (48, 68)), 49~68 <==> 0~\
        # (52 - 58) / (49 - 55)
        A = dist.euclidean(mouth[3], mouth[9])
        B = dist.euclidean(mouth[0], mouth[6])
        inside_ratio = A / B

        # (63 - 67) / (61 - 65)
        C = dist.euclidean(mouth[14], mouth[18])
        D = dist.euclidean(mouth[12], mouth[16])
        outside_ratio = C / D

        return inside_ratio, outside_ratio
