#nested IF..ELSE statement. #Understanding with the Example.
#Taking that input is the positive number or not.

num=float(input("Enter a number: "))

if num>=0:
    if num==0:
        print("zero")
    else:
        print("positive number")
else:
    print("Negative number")

