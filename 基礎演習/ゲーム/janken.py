import random

hands = {1: "グー", 2: "チョキ", 3: "パー"}

# コンピュータの手をランダムに決定する
computer_num = random.randint(1, 3)
computer_hand = hands[computer_num]

# ユーザーに手を入力してもらう
user_hand = int(input("じゃんけん...グー(1), チョキ(2), パー(3) :"))
print(f"コンピューターの手は、{computer_hand}")

# 勝敗を判定する
if user_hand == computer_num:
    print("あいこです")
elif (user_hand == 1 and computer_num == 2) or (user_hand == 2 and computer_num == 3) or (user_hand == 3 and computer_num == 1):
    print("あなたの勝ちです")
else:
    print("あなたの負けです")
