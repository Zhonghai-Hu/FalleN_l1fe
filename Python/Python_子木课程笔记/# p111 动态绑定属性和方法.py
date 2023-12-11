# p111 动态绑定属性和方法
class Students:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name+"在吃饭")

a=Students("邱邱",16)
b=Students('我',16)

print('---------------------------------------------------------------------')
a.gender='men'
print(a.name,a.age,a.gender)
a.eat()
b.eat()

def show():
    print('之外')
a.show=show
a.show()