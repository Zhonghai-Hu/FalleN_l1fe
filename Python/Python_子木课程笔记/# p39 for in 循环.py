# p39 for in 循环
for a in 'python':
    print(a)

for i in range(1,100,1):
    print(i,end=',')

#print(sum(list(range(0,100,1))))

sum=0
for a in range(101):
    if a%2==0:
        sum+=a

print(sum)

