# p118 特殊方法
a=20
b=100
c=a+b
d=a.__add__(b)


print(c)
print(d)

class Students:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __add__(self,other):
        return self.name+other.name
    def __len__(self):
        return len(self.name)

student1=Students('joker',20)
student2=Students('wang',20)
print(student1.__add__(student2))
print(len(student1))