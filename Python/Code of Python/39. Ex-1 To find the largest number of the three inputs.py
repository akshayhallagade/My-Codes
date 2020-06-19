#find the largest number of the following three.
num1=int(input("Enter the 1st number :"))
num2=int(input("Enter the 2nd number :"))
num3=int(input("Enter the 3rd number :"))

if (num1>=num3)and(num1>=num2):
    print("1st input is largest.")
elif (num2>=num3)and(num2>=num1):
    print("2nd input is largest.")
else:
    print("3rd input is largest.")
