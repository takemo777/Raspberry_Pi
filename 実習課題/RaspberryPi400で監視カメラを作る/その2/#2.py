# 2.�v���O�������N�����閈�Ƀt�@�C�������ς��A�ߋ��̃t�@�C�����c�����Ƃ��ł���v���O�������쐬����
import cv2
import datetime

def main():
    # ���݂̓������擾
    now = datetime.datetime.now()

    # �t�@�C�������쐬
    filename = f"{now:%Y%m%d%H%M%S}.jpg"

    # �J��������擾
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    # �ۑ�
    cv2.imwrite(filename, frame)

    cap.release()

if __name__ == "__main__":
    main()