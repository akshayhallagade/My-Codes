A = 2012

if A % 4 == 0:
    if A % 400 == 0:
        if A % 100 == 0:
            print("leap year")
        else:
            print("Not leap year")
    else:
        print("leap year")
else:
    print("Not leap year")
