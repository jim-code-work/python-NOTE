# 網路連線
import urllib.request as request
src = "https://www.ntu.edu.tw"
with request.urlopen(src) as response:
    data=response.read().decode("utf-8")     # 取得台灣大學網站原始碼 (HTML CSS)
print(data)