# p116 多态的实现
class Animal(object):
    def eat(self):
        print("动物会吃")
class Dog(Animal):
    def eat(self):
        print("狗吃骨头")
class Cat(Animal):
    def eat(self):
        print("猫吃鱼")
class Person:
    def eat(self):
        print("人都吃")


def a(Out):
    Out.eat()

a(Animal())
a(Dog())
a(Cat())
a(Person())