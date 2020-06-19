def gcd(m,n):
    for i in range(1,min(m,n)+1):    #directly assigning the value to the number not 
        if (m%i)==0 and (n%i)==0:    #required to creat list.
            mrcf=i
    print(mrcf)
gcd(21,63)          