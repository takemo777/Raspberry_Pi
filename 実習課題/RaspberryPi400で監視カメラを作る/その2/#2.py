# 2.プログラムを起動する毎にファイル名が変わり、過去のファイルも残すことができるプログラムを作成する
import cv2
import datetime

def main():
    # 現在の日時を取得
    now = datetime.datetime.now()

    # ファイル名を作成
    filename = f"{now:%Y%m%d%H%M%S}.jpg"

    # カメラから取得
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    # 保存
    cv2.imwrite(filename, frame)

    cap.release()

if __name__ == "__main__":
    main()