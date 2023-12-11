# p58 字典
a={'开局':'glhf','中间':'gh','最后':'gg'}
print(a)
print(type(a))
b=dict(开局='glhf',中间='gh',最后='gg')
print(b)
c={}
print(c)


print('------------------------------------')
print(b)
print(b['开局'])
print(a.get('中间'))
print(a.get('gg'))
print(a.get('中间',100))


print('------------------------------------')
print(a)
print('最后' in a)
del b['中间']
print(b)
b.clear()
print(b)


a['骂人']='wdnmd'
print(a)
a['骂人']='nmmdw'
print(a)


print('------------------------------------')
print(a)
c=a.keys()
print(c)
print(type(c))
print(list(c))
d=a.values()
print(d)
print(list(d))
print('+++++++++++++')
e=a.items()
print(e)
print(list(e))


print('------------------------------------')
print(a)
for f in a:
    print(f,a.get(f))


print('------------------------------------')
print(a)
a=[0,1,2,3,4,5,6,7,8,9]
b=[00,11,22,33,44,55,66,77,88,99]
e={c:d for c,d in zip(a,b)}
print(e)