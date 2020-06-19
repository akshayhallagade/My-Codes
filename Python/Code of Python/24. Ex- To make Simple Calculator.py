#to design a simple calculator.
print("..........Welcome To The Calculator..........")
while True:
    print("What Operation do you want to perform? Choose any of this. \n1.+ addition.\n2.-Subtraction.\n3.*Multiplication.\n4./Division.")
    choose=int(input("Choose: "))
    num1=float(input("Enter first number: "))
    num2=float(input("Enter Second number: "))
    if choose==1:
        result=num1+num2
        print(result)

    elif choose==2:
        result=num1-num2
        print(result)

    elif choose==3:
        result=num1*num2
        print(result)

    elif choose==4:
        result=num1/num2
        print(result)
    
    else:
        print("Invalid Input")
    print("..........Restarting Operation..........\n\n\n")    

