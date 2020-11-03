# n1 = int(input())
# n2 = int(input())


# def palindromsfind(num1, num2):
#     empty = []
#     for i in range(num1, num2+1):
#         if str(i) == reversed(str(i)):
#             empty.append(i)
#     return empty


# print(palindromsfind(n1, n2))

emptyy = []
for i in range(10, 80):
    a = str(i)
    if a[1:] == a[::-1]:
        emptyy.append(i)
print(emptyy)
