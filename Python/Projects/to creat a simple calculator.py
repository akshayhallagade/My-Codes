while True:
    print("What operation you want to perform.")
    operator=input("Enter the operation from +,-,*,/")
    print("Enter the values.")
    n1=float(input("Enter the 1st value."))
    n2=float(input("Enter the 2nd value."))
    if operator== "+":
        print("summation of the two number is",n1+n2)
    elif operator=="-":
        print("sub of the two number is",n1-n2) 
    elif operator=="*":
        print("mul. of the two number is",n1*n2)
    elif operator=="/":
        print("division of the two number is",n1/n2)
    else:
        print("Invalid input")       