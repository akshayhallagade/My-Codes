while True:
    print("options:")
    print("Enter '1.add' to add two numbers")
    print("Enter '2.subtract' to subtract two numbers")
    print("Enter '3.multiply' to multiply two numbers")
    print("Enter '4.divide' to divide two numbers")
    print("Enter '0.quit' to end the program")
    user_input = input(": ")

    if user_input == "0":
        break
    elif user_input == "1":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        print(num1+num2)
    elif user_input == "2":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        print(num1-num2)
    elif user_input == "3":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        print(num1*num2)
    elif user_input == "4":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        print(num1/num2)
    else:
        print("unknow input")
