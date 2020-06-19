def gcd(m,n):
    #assuming m>=n
    if m<n:
        (m,n)=(n,m)
    if (m%n)==0:
        return(n)
    else:
        diff =m-n
        #diff > n? possible!
        return(gcd(max(n,diff),min(n,diff)))
print(gcd(6,18))