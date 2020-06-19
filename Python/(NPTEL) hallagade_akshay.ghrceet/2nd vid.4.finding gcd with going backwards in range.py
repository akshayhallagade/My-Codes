def gcd(m,n):
    i=min(m,n)
    while i>0: #removing that for loop and using while.
        if (m%i)==0 and (n%i)==0:
            return(i)
        else:
            i=i-1
print(gcd(14,21))                