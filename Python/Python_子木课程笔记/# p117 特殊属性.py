# p117 特殊属性
print(dir(object))
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age
class D(A):
    pass

x=C('joker',20)
print(x.__dict__)
print(C.__dict__)

print('------------------------------------')

print(x.__class__)
print(C.__bases__)  #C类的父类的元组 
print(C.__base__)
print(C.__mro__)    #类的层次
print(A.__subclasses__())