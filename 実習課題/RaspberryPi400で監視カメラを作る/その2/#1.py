# 1.�v���O�������N�������RaspberryPi400 �ɁA�J�����f����Î~��Ƃ��ĕۑ����邾���̒P���ȃv���O�������쐬����
import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cv2.imwrite('test.jpg', frame)
cap.release()