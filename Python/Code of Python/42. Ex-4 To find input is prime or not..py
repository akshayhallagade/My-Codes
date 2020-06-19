#to check the input is prime number or not.
num=int(input("Enter a  number : "))
flag=1
for i in range(2,num):
    if (num%i)==0:
        print("This numbers is not a prime number")
        A=int(num/i)
        print(i,"times",A,"is",num)
        flag=0
        break
if flag==1:
    print("This is the prime number.")
        
