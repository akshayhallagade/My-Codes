n1 = int(input("c: "))
n2 = int(input("a: "))
n3 = int(input("b: "))


def OperationChoices(c, a, b):
    if c == 1:
        return a+b
    elif c == 2:
        return a-b
    elif c == 3:
        return a*b
    elif c == 4:
        return a/b


print(OperationChoices(n1, n2, n3))
