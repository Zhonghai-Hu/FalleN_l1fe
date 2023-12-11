# p119 new init 演示创建过程
class Person:

    def __init__(self,name,age):
        print('self的id值为{0}'.format(id(self)))
        self.name=name
        self.age=age

    def __new__(cls,*args,**kwargs):
        print('__new__被调用执行了,cls的值为{0}'.format(id(cls)))   
        a=super().__new__(cls)
        print('创建的对象id为:{0}'.format(id(a)))
        return a

c=Person('joker',20) 