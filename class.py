# 封裝的變數或含式統稱為 類別的屬性
# 先 定義類別 > 使用

# 語法
# class 類別名稱:
# 定義封裝的變數
# 定義封裝的函式


# 定義類別、類別屬性(封裝在類別中的變數和含式)

class io:                               # 定義一個類別 io, 有兩個屬性 supportedscript 和 read
    supportedscript=["console","file"]
    def read(src):                         # src 為參數
        if src not in io.supportedscript:
            print("not supported")
        else:
            print("Read from",src)
            
# 使用類別
print(io.supportedscript)               # print(類別名稱.屬性名稱)  抓取資料並印出 

io.read("file")                         # 送進參數'file' 進 read, 並呼叫函式
io.read("internet")


# 範例
#定義 Test 類別
class Test:
   x=3                      # 定義變數 x=3
   def say():               # 定義函式 say   為Test類別的屬性
       print("hello")
#使用 Test類別
Test.x=3        #取得屬性x的資料 3          # 類別的名稱.類別名稱 (語法)
Test.say()      #呼叫屬性say 的函式

