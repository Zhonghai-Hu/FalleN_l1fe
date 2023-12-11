# p107 类别
class Games:
    #类属性
    favoutite_game='csgo'

    def __init__(self,game,round):
        self.game=game           #实体属性，进行了赋值操作
        self.round=round         #将局部变量的值转换成实体属性

    #实例函数
    def playing(self):
        print('我在玩csgo...')

    #静态方法
    @staticmethod
    def abcd():
        print('使用了staticmethod进行修饰,所以这是静态方法')
    
    #类方法
    @classmethod
    def b(cls):
        print('这是类方法,用cls以及classmethod修饰')

#创建games类的对象
c=Games(1200,300000)
c.playing()
print(c.game)
print(c.round)

'''Games.favoutite_game(c)
Games.abcd()
Games.b()'''



'''print('---------------------------------------------------------------------')
print(id(c))
print(type(c))
print(c)'''

     

'''print('---------------------------------------------------------------------')
print(id(Games))
print(type(Games))
print(Games)'''


print('---------------------------------------------------------------------')
#类属性的使用
print(Games.favoutite_game)
z=Games('Apex',1)
y=Games('minecraft',1)
print(z.favoutite_game)
print(y.favoutite_game)


print('------------------------------类方法使用---------------------------------------')
Games.b()
print('------------------------------静方法使用---------------------------------------')
Games.abcd()


