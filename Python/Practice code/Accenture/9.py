n1 = int(input())
n2 = int(input())


def findnumber(num1, num2):
    for i in range(5):
        for j in range(num1, num2+1):
            if 2**i == j:
                print(j)


findnumber(n1, n2)
