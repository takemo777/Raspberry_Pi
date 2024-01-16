import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

# LBPHフェイスリコグナイザーを作成して訓練済みモデルを読み込む
recognizer = cv2.face_LBPHFaceRecognizer.create()
recognizer.read("trainer/trainer.yml")

# 顔検出用のカスケード分類器を読み込む
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX

# IDの初期化
id = 0

# IDに関連付けられた名前のリスト
# 自分で設定したID(添字)に手動で名前を入れる
names = ["None", "takemo", "kishida", "suga", "obama", ""]

class FaceRecognitionApp:
    def __init__(self, root, window_title):
        # Tkinterウィンドウの初期化
        self.root = root
        self.root.title(window_title)
        self.video_source = 0  # カメラのデフォルトのビデオソース

        # OpenCVのビデオキャプチャの初期化
        self.vid = cv2.VideoCapture(self.video_source)

        # TkinterのCanvasを初期化してビデオフレームを表示
        self.canvas = tk.Canvas(root, width=self.vid.get(3), height=self.vid.get(4))
        self.canvas.pack()

        # 終了ボタンの初期化
        self.btn_exit = tk.Button(root, text="終了", width=10, command=self.exit_app)
        self.btn_exit.pack(padx=20, pady=10)

        # タイマーイベントのIDを保持する変数
        self.after_id = None

        # ビデオフレームの更新メソッドを呼び出す
        self.update()

        # ウィンドウが閉じられたときの処理を設定
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def update(self):
        # カメラからフレームを読み込む
        ret, frame = self.vid.read()
        if ret:
            # OpenCVのBGR形式をRGB形式に変換
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # 顔を検出
            faces = faceCascade.detectMultiScale(
                cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY),
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(int(0.1 * self.vid.get(3)), int(0.1 * self.vid.get(4))),
            )

            # 検出された顔に予測結果を描画
            for (x, y, w, h) in faces:
                # 顔の領域を切り取り、予測を行う
                id, confidence = recognizer.predict(
                    cv2.cvtColor(frame[y : y + h, x : x + w], cv2.COLOR_BGR2GRAY)
                )

                # 信頼度が60未満の場合は正確な一致
                if confidence < 60:
                    id = names[id]
                    confidence = "  {0}%".format(round(100 - confidence))
                    # 予測結果を描画
                    cv2.putText(
                        frame,
                        str(id),
                        (x + 5, y - 5),
                        font,
                        1,
                        (255, 255, 255),
                        2,
                    )
                    cv2.putText(
                        frame,
                        str(confidence),
                        (x + 5, y + h - 5),
                        font,
                        1,
                        (255, 255, 0),
                        1,
                    )
                else:
                    id = "unknown"
                    confidence = ""

                if id != "unknown":  # "unknown"の場合は枠を描画しない
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # PIL ImageTkに変換してCanvasに表示
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        # 10ミリ秒後にupdateメソッドを再帰的に呼び出す
        self.after_id = self.root.after(10, self.update)

    def exit_app(self):
        # アプリケーションを終了する
        self.root.quit()

    def on_closing(self):
        # ウィンドウが閉じられたときの処理
        if self.after_id:
            # タイマーイベントがあればキャンセル
            self.root.after_cancel(self.after_id)
        # カメラを解放してウィンドウを破棄
        self.vid.release()
        self.root.destroy()

# Tkinterアプリケーションの開始
root = tk.Tk()
app = FaceRecognitionApp(root, "顔認証装置")
root.mainloop()
