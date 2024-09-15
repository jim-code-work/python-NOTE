#  實體方法  = 封裝在在實體物件中的函式

# 基本語法
# class 類別名稱:
#   def __init__(self):                      定義初始化函式
#   def 方法名稱(self, 更多自訂參數):          定義 實體方法
# x = 類別名稱(參數)
# x.方法名稱()                             呼叫實體方法


# 範例  

class point:
    def __init__(self, x, y):
        self.x=x                    # 定義實體屬性 x , y
        self.y=y
    def show(self):                  # 定義實體方法
        print(self.x, self.y)
    def distance(self, targetx, targety):
        return (((self.x-targetx)**2)+((self.y-targety)**2))**0.5
p=point(3,4)
p.show()                            # 呼叫實體方法(函式)
result = p.distance(0,0)                     # 計算座標 (3,4) 到座標 (0,0) 的距離
print(result)