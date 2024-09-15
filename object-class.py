# 類別的兩種用法
# 1. 類別與類別屬性
# 2. 類別與 實體物件，實體屬性

# 2. 語法
# class 類別名稱:
#   def _init_(self):           #定義初始化函式
#   obj=類別名稱()             #建立實體物件，放入變數 obj 中  並 呼叫初始化函式



# 2. 實體物件,實體屬性 範例       # 實體物件的設計，平面座標上的點
class Point:            
    def __init__(self, x, y):   # x , y 稱為實體屬性
        self.x=3
        self.y=4
        
# 建立第一個實體物件      
p1=Point(3,4)
print(p1.x,p1.y)
# 建立第二個
p2=Point(5,6)
print(p2.x, p2.y)