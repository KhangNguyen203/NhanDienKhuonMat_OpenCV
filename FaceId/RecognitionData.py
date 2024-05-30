import cv2
import numpy as np
from PIL import Image
import queryDB as db
from time import sleep
from gtts import gTTS
import time
import os


class RecognitionData:
    def __init__(self):
        # Khởi tạo webcam và đặt độ phân giải của nó thành 732x720
        self.cam = cv2.VideoCapture(0)
        self.cam.set(3, 732)
        self.cam.set(4, 720)

        # khởi tạo một đối tượng CascadeClassifier trong thư viện OpenCV với tệp tin XML 
        # chứa thông tin về mô hình Cascade để phát hiện khuôn mặt trên hình ảnh đầu vào
        self.face_cascade = cv2.CascadeClassifier("libs/haarcascade_frontalface_default.xml")

        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read('recognizer/trainingData.yml')
        self.imgBackground = cv2.imread('image/background.png')
        self.modeType = 3
        self.last_time_checked = time.time()
        self.fontface = cv2.FONT_HERSHEY_SIMPLEX
        self.folderModePath = 'image'
        self.modePathList = os.listdir(self.folderModePath)
        self.imgModeList = []

        #Tạo 2 biến lưu giá trị của người quét khuôn mặt
        self.id = None
        self.name = None
        
        for path in self.modePathList:
            self.imgModeList.append(cv2.imread(os.path.join(self.folderModePath, path)))

    def run(self):
        start_time = time.time()
        while True:
            ret, frame = self.cam.read()
            frame_resized = cv2.resize(frame, (732, 720))
            self.imgBackground[0:0 + 720, 0:0 + 732] = frame_resized
            self.imgBackground[44:44 + 634, 800:800 + 414] = self.imgModeList[self.modeType]
            gray = cv2.cvtColor(self.imgBackground, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray)
            if len(faces) == 0:
                self.modeType = 3
            else:
                for (x, y, w, h) in faces:
                    cv2.rectangle(self.imgBackground, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    roi_gray = gray[y:y + h, x:x + w]
                    id, confidence = self.recognizer.predict(roi_gray)
                    if confidence < 40:
                        profile = db.getProfile(id)
                        if profile is not None:
                            cv2.putText(self.imgBackground, "" + str(profile[1]), (x + 10, y + h + 30), self.fontface, 1, (0, 255, 0), 2)
                            cv2.putText(self.imgBackground, "" + str(100 - round(confidence)) + " %", (x + 10, y - 10), self.fontface, 1, (0, 255, 0), 2)


                            # Chờ 3 giây trước khi chạy code còn lại
                            current_time = time.time()
                            elapsed_time = current_time - start_time
                            if elapsed_time < 5:
                                cv2.imshow("Nhận Diện Khuôn Mặt", frame)
                                if cv2.waitKey(1) == ord('q'):
                                    break
                                continue

                            #Gán ID và name và thoát chương trình khi nhận diện thành công
                            self.id = profile[0]
                            self.name = profile[1]
                            return

                            current_time = time.time()
                            if (current_time - self.last_time_checked) >= 3:
                                check = db.checkInAndCheckOut(profile[0])
                                if check:
                                    self.modeType = 1
                                else:
                                    self.modeType = 2
                                elapsed_time = current_time - self.last_time_checked
                                self.last_time_checked = current_time
                                minutes = int(elapsed_time // 60)
                                seconds = elapsed_time % 60
                    else:
                        cv2.putText(self.imgBackground, "Unknown:", (x + 10, y + h + 30), self.fontface, 1, (0, 0, 255), 2)
                        self.modeType = 4
            cv2.imshow("Nhận Diện Khuôn Mặt", self.imgBackground)
            if cv2.waitKey(1) == ord('q'):
                break

        self.cam.release()
        cv2.destroyAllWindows()
