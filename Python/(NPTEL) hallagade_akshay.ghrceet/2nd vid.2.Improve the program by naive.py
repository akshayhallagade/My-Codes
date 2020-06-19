def gcd(m,n):
    cf=[]
    for i in range(1,min(m,n)+1):   #using one time for loop.
        if (m%i)==0 and (n%i)==0:
            cf.append(i)
    print(cf[-1])
gcd(14,63)          