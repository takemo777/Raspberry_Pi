import imutils
import numpy as np
import cv2
import tkinter as tk
from PIL import Image, ImageTk

"""カレントディレクトリ: cd 実習課題\RaspberryPi400で顔認証装置を作る"""

# 顔検出ループを停止する関数
def stop_detection():
    cap.release()
    cv2.destroyAllWindows()
    root.destroy()

# メインウィンドウを作成
root = tk.Tk()
root.title("Face Detection")

# ビデオフィードを表示するためのラベルを作成
label = tk.Label(root)
label.pack(padx=10, pady=10)

# 「停止」ボタンを作成
stop_button = tk.Button(root, text="停止", command=stop_detection)
stop_button.pack(pady=10)

# ビデオキャプチャを開く
cap = cv2.VideoCapture(0)

# モデルを読み込む
prototxt = "deploy.prototxt"
model = "res10_300x300_ssd_iter_140000.caffemodel"
net = cv2.dnn.readNetFromCaffe(prototxt, model)

# 顔検出ループ
def detect_faces():
    ret, frame = cap.read()
    img = imutils.resize(frame, width=400)
    (h, w) = img.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))

    net.setInput(blob)
    detections = net.forward()

    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            text = "{:.2f}%".format(confidence * 100)
            y = startY - 10 if startY - 10 > 10 else startY + 10
            cv2.rectangle(img, (startX, startY), (endX, endY), (0, 0, 255), 2)
            cv2.putText(img, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

    # tkinterで表示するために画像をRGB形式に変換
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_tk = ImageTk.PhotoImage(Image.fromarray(img_rgb))
    label.img_tk = img_tk
    label.config(image=img_tk)
    label.after(10, detect_faces)  # 10ミリ秒後に関数を呼び出す

# 顔検出ループを開始
detect_faces()

root.mainloop()
