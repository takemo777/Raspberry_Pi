# 1.プログラムを起動するとRaspberryPi400 に、カメラ映像を静止画として保存するだけの単純なプログラムを作成する
import cv2

# 実行出来ないときは(cd RaspberryPi400で監視カメラを作る)

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
# パスの指定を正確に
cv2.imwrite("img/test.jpg", frame)
cap.release()