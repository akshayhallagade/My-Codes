def mov(h):
    n1=0
    n2=1
    if h<0:
        print("incorrect input")
    elif h==0:
        return n1
    elif h==1:
        return n2     
    else:
        for j in range(2,h):
            n3=n2+n1
            n1=n2
            n2=n3
            return n2
print(mov(5))