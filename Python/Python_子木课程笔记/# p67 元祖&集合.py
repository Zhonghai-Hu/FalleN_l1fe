# p67 元祖&集合



# add,remove,apdate,discard,pop:随件删除一个,clear
# ==, !=,issubset:一个集合是否在另一个里，issuperset:一个集合是否是另一个集合的超集
# isdisjoint:两个集合是否有交集, &:求交集（a & b), union==|:并集 去掉重复元素(a.union(b))/(a | b)
# difference== - :差集 去掉不同的（a.difference(b))（a-b)
# symmetric_difference==^:只留下不同的(a.symmetric_difference(b)) (a^b)




'''a=['a','b','c','d','e','f','g']
a.append(1)
print(a)'''
b=dict(abc='abc',bcd='bcd')


print('------------------------------------------------')


c=('hello','world',119,911)
print(c)

e='ff','fw','hhh',''
print(e)

f='gg',
print(f,type(f))

d=tuple(('python','nb','wdnmd','素质'))
print(d)

g=()
h=tuple()
print(g,h)


print('------------------------------------------------')


i=('dd','gl','hf',[98,99,100,'hfhf'])
print(i,type(i))
print(i[0],i[1],i[3])
i[3].append(101)
print(i)


print('------------------------------------------------')


print(i)
for j in i:
    print(j)
    

print('------------------------------------------------')


k={'a','b','c','d','e','f','g','b','c',12345}
print(k)
l=set(range(10))
print(l,type(l))
m=set(['hello','world',119,911])
print(m,type(m))
n=set(('dd','gl','hf'))
print(n,type(n))
o=set()
print(o,type(o))
    

print('------------------------------------------------')


print(k,type(k))
print('a' in k)
k.add(10086)
print(k)
k.update({200,300,400})
print(k)
k.update((100,500,600))
print(k)

k.remove('a')
print(k)
k.discard('gg')
print(k)
k.pop()
print(k)
k.clear()
print(k)


print('------------------------------------------------')


p={12,13,77,15}
q={11,12,15,91}
print(p==q,p!=q)
r={12,13,14,15}
s={12,13,14,15,17,18,19,20}
t={12,13,14,15,30,40,10,55}
print(r.issubset(s))
print(s.issuperset(r))
print(s.isdisjoint(t))


print('------------------------------------------------')


print(p)
print(q)
print(r)
print(s)
print(p & r)
print(p.union(r))
print(p|s)
print(s.difference(p))

print(p.symmetric_difference(q))
print(p^q)


print('------------------------------------------------')


u={i*i for i in range(10)}
print(u)