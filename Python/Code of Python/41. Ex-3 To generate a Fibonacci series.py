#to creat fibbonacci series.
#0,1,1,2,3,5,8,13,21,34....

up_to=int(input("how much huge fibbonacci series is needed."))
i=n1=0
n2=1
print(n1)
print(n2)
while i<=(up_to-3):
    i+=1
    nth=n1+n2
    print(nth)
    n1=n2
    n2=nth
    
    
