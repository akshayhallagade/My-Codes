#to check the input is prime number or not.
num=int(input("Enter a  number : "))
ini=2
while ini<num:
    if (num%ini==0):
        print("This is not a prime number.")
        print(ini,"times",num/ini,"is",num)
        break
    else:
        ini+=1
else:
    print("this is the prime number.")
