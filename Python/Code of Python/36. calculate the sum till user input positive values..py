#calculate the sum till user input positive values.
summ=0
while True:
    A=int(input("Enter a value :"))
    if A>=0:
        summ+=A
    else:
        print(summ)
        break


