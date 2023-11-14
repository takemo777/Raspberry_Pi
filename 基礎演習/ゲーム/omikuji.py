import tkinter as tk
import random

kuji = ["大吉", "吉", "凶", "大凶"]

# メインウィンドウの作成
root = tk.Tk()
root.title("おみくじ")
root.geometry("300x250")

def get_kuji():
    # ランダムにおみくじを引く
    global kuji_result
    kuji_result = random.choice(kuji)

    # ラベルのテキストを更新する
    label2.config(text=kuji_result)

    # 文字の色を設定
    if kuji_result == "大吉":
        label2.config(foreground = "red")
    elif kuji_result == "吉":
        label2.config(foreground = "orange")
    elif kuji_result == "凶":
        label2.config(foreground = "blue")
    else:
        label2.config(foreground = "purple")

# ボタンの作成
button = tk.Button(root, text = "おみくじを引く", command = get_kuji)
button.pack()

# ラベルの作成
label = tk.Label(root, text="運勢は...",font = (None, 10))
label2 = tk.Label(root, text = "", font=(None, 20))

label.pack()
label2.pack()

root.mainloop()
