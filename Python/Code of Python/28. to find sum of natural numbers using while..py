#Sum of natural numbers.
num=int(input("Enter the upto what value you want the summation :"))
i=0
summation=0
while i<=num:
    summation=summation+i
    print("Sum at the positions :",i,":",summation)
    i+=1
    
