#To find the input is the leap year not.

#2017 is not leap year.
#1900 is not leap year.
#2000 is a leap year.
#2016 is a leap year.

year=int(input("Enter a year to check : "))

if year%4==0:
    if (year%100==0):
        if (year%400==0):
            print(year,"is a leap year.")  #1900 will fail, #2000 will pass
        else:
            print(year,"is not a leap year.")
    else:
        print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")
            
