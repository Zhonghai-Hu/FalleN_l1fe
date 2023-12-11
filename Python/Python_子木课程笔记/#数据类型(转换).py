#数据类型(转换)
print('8进制',0o1234567)

#integier
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

#bool
n1=False
n2=True
print(type(n1))
print(n1+n2)
print(n1+1)

#转换
birthday=2006
name='Harrison'
print(birthday)
print(name,type(name))
print('我是'+name+',生日是'+str(birthday)+('年'))

bir='-2006'
print(bir,int(bir))
s2=99.99
print(int(float(s2)))
