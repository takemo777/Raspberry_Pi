# 3.GUIを使って、保存ファイル名を指定でき、ボタンを押すとカメラの映像を指定したファイル名で保存するプログラムを作成する
import cv2
import tkinter as tk
from tkinter import simpledialog

def save_image():
    filename = simpledialog.askstring("Input", "画像ファイル名を入力してください（拡張子を含む）", parent=root)

    if filename:
        ret, frame = cap.read()
        cv2.imwrite(filename, frame)
        print(f"画像が {filename} として保存されました。")
        # ウェブカメラを解放
        cap.release()
        # tkinter を終了
        root.destroy()

# メインウィンドウを作成
root = tk.Tk()
root.withdraw()
# ウェブカメラを開く
cap = cv2.VideoCapture(0)

# プログラム開始時にファイル名を尋ねる
save_image()

# tkinter のメインループを開始
root.mainloop()