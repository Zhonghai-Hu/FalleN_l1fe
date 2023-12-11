#输入函数input
Math=input('请重新输入')
print(Math,type(Math))

if type(Math)==int:
    print("继续")
else:
    print("请重新输入")


a=input('一个整数')
b=input('再输一个')
print(int(a)+int(b))