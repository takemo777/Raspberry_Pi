# 1.プログラムを起動するとRaspberryPi400 に、カメラ映像を静止画として保存するだけの単純なプログラムを作成する
import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cv2.imwrite('test.jpg', frame)
cap.release()