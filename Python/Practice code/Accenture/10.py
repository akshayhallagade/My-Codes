m = int(input())
n = int(input())


def calculate(m1, n1):
    summ = 0
    for i in range(m1, n1+1):
        if i % 3 == 0 and i % 5 == 0:
            summ += i
    return summ


print(calculate(m, n))
