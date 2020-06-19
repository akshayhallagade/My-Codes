n_terms=int(input("Enter a input :"))
n1=0
n2=1
a=0
print("fibanacci sequence upto",n_terms,":")
print(n1)
print(n2)
while a<=n_terms:
    n3=n2+n1
    print(n3)
    n1=n2
    n2=n3
    a=a+1