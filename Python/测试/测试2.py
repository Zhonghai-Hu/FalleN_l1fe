a=("()[]{}")
i=0
def s(self,a):
    while a is not None:
        i+=1
        if a[i]!=a[i+1]:
            return False
        else:
            return True

