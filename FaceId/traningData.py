import cv2
import os
import numpy as np
from PIL import Image

class TrainingData:
    def __init__(self, path):
        self.path = path
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()

    def getImagesAndLabels(self):
        imagePaths = [os.path.join(self.path, f) for f in os.listdir(self.path)] 
        faces = []
        IDs = []
        for imagePath in imagePaths:
            faceImg = Image.open(imagePath).convert('L')
            faceNp = np.array(faceImg, 'uint8')
            ID = int(os.path.split(imagePath)[-1].split('.')[1])
            faces.append(faceNp)
            IDs.append(ID)
            cv2.waitKey(1)
        return IDs, faces

    def train(self):
        Ids, faces = self.getImagesAndLabels()
        self.recognizer.train(faces, np.array(Ids))
        self.recognizer.save('recognizer/trainingData.yml')
        print('Training success')

# Sử dụng lớp TrainingData
# training_data = TrainingData('dataSet')
# training_data.train()
# cv2.destroyAllWindows()