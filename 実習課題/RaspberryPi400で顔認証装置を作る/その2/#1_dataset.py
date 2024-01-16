"""カメラ映像からリアルタイムで自分の顔を探し出して、四角で囲むプログラム
を作成してください。他人の顔を囲んではいけません"""
# #1→#2→#3の順番に実行
# カメラが固まったら顔を動かしてみる
import cv2
import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk

# カメラの初期化
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # ビデオの幅を設定
cam.set(4, 480)  # ビデオの高さを設定

# 顔検出器の初期化
face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# tkinterウィンドウの初期化
root = tk.Tk()
root.title("顔認証装置")

# ユーザーID入力用のダイアログボックス
user_id = simpledialog.askstring("ユーザーID", "ユーザーID(数字、1以上)を入力してください:")

# 写真の枚数入力用のダイアログボックス
num_photos = simpledialog.askinteger("写真の枚数", "撮影する写真の枚数を入力してください:")

print(f"\n {num_photos}枚の顔キャプチャの初期化中。カメラに向かって待ってください...")

# キャプチャ映像表示用のラベル
video_label = tk.Label(root)
video_label.pack()

# 各個人のサンプリングされた顔の数の初期化
count = 0

def exit_program():
    root.destroy()

# 終了ボタン
exit_button = tk.Button(root, text="終了", command=exit_program)
exit_button.pack()

def update_frame():
    global count
    ret, img = cam.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 顔の検出
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # 顔の周りを囲む
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        count += 1

        # 検出された顔画像をデータセットフォルダに保存
        cv2.imwrite("dataset/User." + str(user_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])

        # 画像を表示
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        video_label.img = img
        video_label.configure(image=img)

    if count < num_photos:
        root.after(100, update_frame)  # 100ミリ秒ごとにupdate_frameを呼び出す
    else:
        # 指定した枚数の写真を撮影したらTkinterウィンドウを閉じる
        root.destroy()

# 最初のフレームを表示
update_frame()

# tkinterウィンドウを表示
root.mainloop()

# 後片付け
print("\n 終了しました")
cam.release()
cv2.destroyAllWindows()
