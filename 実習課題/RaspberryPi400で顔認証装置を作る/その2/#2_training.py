import cv2
import numpy as np
from PIL import Image
import os

# 顔画像データベースのパス
path = "dataset"

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# 画像とラベルデータを取得するための関数
def getImagesAndLabels(path):

    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []

    for imagePath in imagePaths:

        PIL_img = Image.open(imagePath).convert("L")  # グレースケールに変換
        img_numpy = np.array(PIL_img, "uint8")

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)

        for (x, y, w, h) in faces:
            faceSamples.append(img_numpy[y:y+h, x:x+w])
            ids.append(id)

    return faceSamples, ids

print("\n 顔のトレーニング中です。")
faces, ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))

# モデルをtrainer/trainer.ymlに保存
recognizer.write("trainer/trainer.yml")

# トレーニングされた顔の数を表示し、プログラムを終了
print("\n {0} 顔がトレーニングされました。".format(len(np.unique(ids))))
