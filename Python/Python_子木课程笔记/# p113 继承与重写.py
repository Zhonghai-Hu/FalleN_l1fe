# p113 继承与重写
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def a(self):
        print(self.name,self.age)

class Students(Person):
    def __init__(self,name,age,b):
        super().__init__(name,age)
        self.b=b
    def a(self):
        super().a()
        print(self.b)    

d=Students('wo',100,1)
d.a()