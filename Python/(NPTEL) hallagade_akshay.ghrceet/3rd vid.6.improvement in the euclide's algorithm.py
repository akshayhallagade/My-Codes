def gcd(m,n):
    if m<n:  #assuming m>=n
        (m,n)=(n,m)
    while (m%n)!=0:
        diff =m-n
        #diff > n? possible!
        (m,n)=(max(n,diff),min(n,diff))
    return(n)
print(gcd(18,6))