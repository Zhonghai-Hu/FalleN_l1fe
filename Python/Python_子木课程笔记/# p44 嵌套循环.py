# p44 嵌套循环
'''
for a in range(1,4):
    for a in range(1,5):
        print('*',end='\t')
    print()
'''

for b in range(1,10):
    for j in range(1,b+1):
        print(j,'*',b,'=',b*j,end='\t')
    print(  )
