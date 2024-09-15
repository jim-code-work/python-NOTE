# 儲存檔案
file = open("txt", mode="w", encoding="utf-8")  # 開啟
file.write("Hello 酷喔")          # 操作
file.close()                 # 關閉

with open("data.txt", mode="w", encoding="utf-8") as file:   # 儲存檔案 最佳實務
    file.write("測試\n")


# 讀取檔案
with open("data.txt", mode="r", encoding="utf-8") as file:
    data=file.read()
print(data)


