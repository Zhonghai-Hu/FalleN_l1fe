# p87 函数
def a(a,b,d):
    c=a+b
    return c
b=a(10,20,30)
print(b)


print("__________________________________")


def c(e,f):
    print('1',e)
    print('1',f)
    e=1
    f.append(99)
    print('2',e)
    print('2',f)
    return


h=100
i=['gg','87','78']
print('3',h)
print('3',i)

c(h,i)

print('4',h)
print('4',i)


print("__________________________________")


def j(k):
    l=[]
    m=[]
    for n in k:
        if n%2:
            l.append(n)
        else:
            m.append(n)
    return l,m

n=[10,33,25,88,99,46,78]
print(j(n))
