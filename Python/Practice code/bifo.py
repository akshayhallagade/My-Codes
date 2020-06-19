def mov(i):
    n1=0
    n2=1
    n3=1
    if i<0:
        print("incorrect input")
    elif i==0:
        return n1
    elif i==1:
        return n2     
    else:
        for i in range(2,i):
            n1=n2
            n2=n3
            n3=n2+n1
            return n3
print(mov(5))