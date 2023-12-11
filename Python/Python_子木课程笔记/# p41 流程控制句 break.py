# p41 流程控制句 break
key=str(12345678)
for item in range(3):
    print('请输入密码')
    key1=input()
    if key==key1:
        print('输入正确')
        break
else:
    print('账户已经锁定')

'''a=0
while a<3:
    passward=input('请输入密码：')
    if passward==('000'):
        print('输入正确')
        break
    else:
        print('输入错误')
    a+=1'''
