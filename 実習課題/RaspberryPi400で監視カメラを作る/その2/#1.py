# 1.�v���O�������N�������RaspberryPi400 �ɁA�J�����f����Î~��Ƃ��ĕۑ����邾���̒P���ȃv���O�������쐬����
import cv2

# ���s�o���Ȃ��Ƃ���(cd RaspberryPi400�ŊĎ��J���������)

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
# �p�X�̎w��𐳊m��
cv2.imwrite("img/test.jpg", frame)
cap.release()