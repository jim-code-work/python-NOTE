# File 實體物件設計: 包裝檔案讀取的程式
class File:
    def __init__(self, name):
        self.name=name
        self.file=None          # 尚未開啟檔案, 初期是 None
        
    def open(self):             # 定義實體方法open
        self.file=open(self.name, mode="r", encoding="utf-8")
    def read(self):             # 定義實體方法read
        return self.file.read()
    
f1=File('object-class-3-1.txt')      # 建立實體物件f1         # 讀取第一個檔案
f1.open()
text=f1.read()
print(text)

f2=File('object-class-3-.txt')    # 建立實體物件 f2                        # 讀取第二個檔案
f2.open()
text=f2.read()
print(text)
    