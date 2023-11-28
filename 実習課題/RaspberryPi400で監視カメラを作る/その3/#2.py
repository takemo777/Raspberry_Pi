import cv2
import tkinter as tk
import numpy as np
from tkinter import filedialog
from threading import Thread, Event
from PIL import Image, ImageTk
import threading, queue

# カメラの起動を監視するクラス
class VideoCaptureDaemon(threading.Thread):
    def __init__(self, video, result_queue):
        super().__init__()
        self.daemon = True
        self.video = video
        self.result_queue = result_queue

    def run(self):
        # カメラのキャプチャを結果キューに格納
        self.result_queue.put(cv2.VideoCapture(self.video))

# カメラの起動にタイムアウトを設定する関数
def get_video_capture(video, timeout=5):
    res_queue = queue.Queue()
    # カメラの起動監視スレッドを開始
    VideoCaptureDaemon(video, res_queue).start()
    try:
        # タイムアウト内にキャプチャが取得できれば返す
        return res_queue.get(block=True, timeout=timeout)
    except queue.Empty:
        print('cv2.VideoCapture: could not grab input ({}). Timeout occurred after {:.2f}s'.format(video, timeout))

class VideoRecorder:
    def __init__(self, root, cap, size):
        self.root = root
        self.cap = cap
        self.size = size
        self.recording = False
        self.stop_event = Event()
        self.photo = None

        # Canvasを作成して、フレームを表示するための変数を初期化
        self.canvas = tk.Canvas(root, width=size[0], height=size[1])
        self.canvas.pack()

        # レコードボタンを作成し、コマンドとしてtoggle_recordメソッドを指定
        self.record_button = tk.Button(root, text="録画", command=self.toggle_record)
        self.record_button.pack()

    def toggle_record(self):
        # レコーディングのトグルを実行
        if not self.recording:
            self.start_record()
        else:
            self.stop_record()

    def start_record(self):
        # レコーディングを開始
        self.recording = True
        self.record_button.config(text="停止")
        self.stop_event.clear()  # イベントをクリア
        self.record_thread = Thread(target=self.record)
        self.record_thread.start()

    def stop_record(self):
        # 録画を停止
        self.recording = False
        self.record_button.config(text="録画")
        self.stop_event.set()  # イベントをセット
        self.record_thread.join(timeout=5)  # スレッドが終了するまで待つ

        # 録画が終了したら、カメラのリソースを解放
        # self.cap.release()

    def record(self):
        # ビデオライターの設定
        fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        fps = 20.0
        writer = cv2.VideoWriter(self.get_save_path(), fmt, fps, self.size)

        def update_frame():
            # カメラからフレームを読み込んでリサイズし、ビデオに書き込む
            _, frame = self.cap.read()
            # フレームが空でないかどうかをチェック
            if frame is not None:
                # フレームの型がuint8であることを確認
                frame = frame.astype(np.uint8)
                frame = cv2.resize(frame, self.size)
                writer.write(frame)

                # フレームをTkinterのCanvasに表示
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
                self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
                self.root.update_idletasks()  # Tkinterのイベントを処理

                if not self.stop_event.is_set():
                    # 次のフレーム更新をスケジュール
                    self.root.after(1, update_frame)
                else:
                    # 録画を停止し、リソースを解放
                    writer.release()

        # 最初のフレーム更新を開始
        update_frame()

    def get_save_path(self):
        # 保存先のファイルパスを取得
        file_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")])
        return file_path

def main():
    # カメラを起動して、ウィンドウを表示
    # cap = cv2.VideoCapture(0) 
    cap = get_video_capture(0)  # タイムアウトを設定
    size = (640, 360)

    root = tk.Tk()
    root.title("Video Recorder")

    recorder = VideoRecorder(root, cap, size)

    # ウィンドウが閉じられる際には、適切にクリーンアップ
    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root, recorder))
    root.mainloop()

def on_closing(root, recorder):
    # 録画中にウィンドウが閉じられる場合、録画を停止
    if recorder.recording:
        recorder.stop_record()

    # ウィンドウを閉じる
    root.destroy()

if __name__ == "__main__":
    main()
