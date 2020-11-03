num3 = input("Num1: ")
num4 = input("Num2: ")


def numberOfCarries(num1, num2):
    carry = 0
    count = 0
    a = min(len(num1), len(num2))
    count = 0
    for i in range(1, a+1):
        if (int(num1[i*-1])+int(num2[i*-1])+count) > 9:
            carry += 1
            count = 1

    print(carry)


numberOfCarries(num3, num4)

# def NumberOfCarries(n1, n2):

#     count = 0

#     carry = 0

#     if len(n1) <= len(n2):

#         l = len(n1)-1

#     else:

#         l = len(n2)-1

#     for i in range(l+1):

#         temp = int(n1[l-i])+int(n2[l-i])+carry

#         if len(str(temp)) > 1:

#             count += 1

#             carry = 1

#         else:

#             carry = 0

#     return count+carry


# n1 = input()
# n2 = input()
# print(NumberOfCarries(n1, n2))
