num=int(input("Enter a number: "))
for i in range(2,num):
    if num%i==0:
        print(num,"num is not a prime number")
        break
else:
    print(num,"num is a prime number.")    