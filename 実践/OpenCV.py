import matplotlib.pyplot as plt
import cv2
#  pip install opencv-python 

img = cv2.imread("input.jpg")

# 画像をグレースケールに変換
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# グレースケール画像を表示する
plt.imshow(gray_img, cmap="gray")
plt.show()
