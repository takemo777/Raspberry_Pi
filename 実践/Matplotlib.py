import matplotlib.pyplot as plt
import japanize_matplotlib
# pip install japanize_matplotlib

x = [1, 2, 3, 4, 5]
y = [1, 4, 8, 16, 25]

plt.plot(x, y, color='blue', markerfacecolor='yellow', marker='*', linestyle='--')
plt.xlabel('経過年数', fontsize=10)
plt.ylabel('売上高', fontsize=20)

plt.grid()
plt.title('タイトル')