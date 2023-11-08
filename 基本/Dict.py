country =  {"Japan": "Tokyo", "USA": "Washington D.C.", "France": "Paris"}

# 1. 新たにキーと値（'China': ' Beijing'）を追加して、辞書をコンソールへ出力する
country["China"] = "Beijing"
print(country)

# 2. 辞書から"USA"を削除して、辞書をコンソールへ出力する
del country["USA"]
print(country)

# 3. キー"Japan"に紐ついた値をコンソールへ出力する
print(country["Japan"])