n = int(input())


def numbertable(n1):
    sum = 0
    for i in range(1, 11):
        sum += (i*n1)
        print(i*n1, end=" ")

    print("\n")
    print(sum)


numbertable(n)
