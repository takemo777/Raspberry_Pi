# 1.プログラムを起動して5 秒間もしくはESC キーを押すまでの間の動画をファイルに保存するプログラムを作成する
import cv2
import numpy as np
import time

def main():
    cap = cv2.VideoCapture(0)

    # 動画ファイルの形式設定
    fmt = cv2.VideoWriter_fourcc("m", "p", "4", "v")
    # フレームレートを設定
    fps = 20.0
    # サイズ設定
    size = (640, 360)
    writer = cv2.VideoWriter("test.mp4", fmt, fps, size)

    start_time = time.time()
    # 5秒間起動する
    while time.time() - start_time < 5:
        _, frame = cap.read()
      # ↑ブール値を無視するためらしい
        frame = cv2.resize(frame, size)
        writer.write(frame)

        cv2.imshow("frame", frame)
        # ESCキーで終了
        if cv2.waitKey(1) == 27:
            break

    writer.release()
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()