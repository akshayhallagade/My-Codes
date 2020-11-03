n = int(input())
m = int(input())


def differenceofSum(n, m):
    sumdivisible = 0
    sumnotdivisible = 0
    for i in range(m+1):
        if i % n == 0:
            sumdivisible += i
        elif i % n != 0:
            sumnotdivisible += i
    return sumnotdivisible - sumdivisible


print(differenceofSum(n, m))
