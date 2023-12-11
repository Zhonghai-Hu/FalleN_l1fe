# p40 for in 练习

for a in range(100,1000,1):
    if (a//100)**3+(a//10-a//100*10)**3+(a-a//10*10)**3==a:
        print(a)