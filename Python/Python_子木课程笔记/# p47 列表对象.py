# p47 列表对象
'''a=['666','hello']
lst=['hello','world',a]
print(lst)'''

#index=指数 找出列表中的值
#append=追加 把一个值加入列表 一个id
#extend=扩展 把每一个元素添加进列表

a=['1','2','3','4','5','6','python']
print(a[-1])
print(a.index('1'))
print(a[0:7:1])
print(a[::-1])
print('pyth' in a)
a.append(100)
print(a)
b=['gg','win','gl','hf']
a[3:]=b
print(a)

a.remove('1')
print(a)
b.pop(1)
print(b)
c=b[1:3]
print(c)
print('-------------------------------------------')
print(a)
a[1:3]=[]
print(a)
print(c)
c.clear()
print(c)
del c


print('-------------------------------------------------')
print(a)
a[1]=10
print(a)
a[1:3]=100,200,"hello"
print(a)


print('-------------------------------------------------')
d=[110,119,911,114514,]
print(d)
d.sort()

d.sort(reverse=True)
print(d)
d.sort(reverse=False)
print(d)

print('-------------------------------------------------')
e=sorted(d)
print(e)
print(id(e),id(d))

print('-------------------------------------------------')
lst=list(range(0,10))
print(lst)
f=[g*2 for g in range(1,6)]
print(f)
