import cv2
import os
import numpy as np
from PIL import Image

path = 'dataset'

recognizer = cv2.face.LBPHFaceRecognizer_create()

faces = []
ids = []

for imagePath in os.listdir(path):

    img = Image.open(
        os.path.join(path, imagePath)
    ).convert('L')

    img_numpy = np.array(img, 'uint8')

    id = int(imagePath.split(".")[1])

    faces.append(img_numpy)
    ids.append(id)

recognizer.train(faces, np.array(ids))

if not os.path.exists("trainer"):
    os.makedirs("trainer")

recognizer.write("trainer/trainer.yml")

print("Training Complete")