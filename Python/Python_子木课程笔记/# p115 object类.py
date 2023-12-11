# p115 object类
class Students(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '我是{0},你们等死吧'.format(self.name)
a=Students('joker',20)
print(a)

