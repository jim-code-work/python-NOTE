# 範例  實體物件的設計: 分開紀錄 姓 名

class Fullname:
    def __init__(self, first, last):
        self.first=first
        self.last=last
name1=Fullname("Lai", "jim")
print(name1.first, name1.last)

name2=Fullname("bb", "toto")
print(name2.first, name2.last)

