# p120 类的赋值与浅拷贝
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk


cpu1=CPU()
cpu2=cpu1
print(cpu1,cpu2)
print('----------------------')
disk=Disk()
computer=Computer(cpu1,disk)

import copy
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)
print('----------------------')
computer3=copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)