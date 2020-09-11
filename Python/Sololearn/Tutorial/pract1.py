# import cv2
# # this is comment.
# print("Hello World")
# print(5+8)
# ''' if (age < 18):
# #     print("Hello")'''


##################################################
# Fibonnaci series with def
##################################################
# def fibonnaci(no_to_do, n0, n1, n2):
#     for i in range(no_to_do-2):
#         n2 = n1+n0
#         print(n2)
#         n0 = n1
#         n1 = n2

# n0 = 0
# n1 = 1
# n2 = 0

# try:
#     no_to_do = int(input("Enter a no. upto. :"))
#     print(n0)
#     print(n1)
#     fibonnaci(no_to_do, n0, n1, n2)
# except:
#     print("Re run again")

##################################################
# fibonaci series without def.
##################################################
# A = int(input("Enter a number:"))
# n0 = 0
# n1 = 1
# n2 = 0
# print(n0)
# print(n1)
# for i in range(A-2):
#     n2 = n1+n0
#     print(n2)
#     n0 = n1
#     n1 = n2
##################################################
# def fibonnaci(n):
#     if n <= 1:
#         return n
#     else:
#         return(fibonnaci(n-1)+fibonnaci(n-2))


# intt = int(input("Enter a innu:"))
# # print(fibonnaci(intt))
# for i in range(intt):
#     print(fibonnaci(i))
# import math
# print(math.gcd(12, 18))
# A = '''
# snjsbdjabsj
# '''
# print(A)
# name = "   akshay    "
# name = "Akshay,shubham,alok"
# print(A:=name.strip())
# print(len(A))
# print(A.upper())
# print(A.replace("a", "r"))
# print(A.replace(",", "\n"))
# str = "This is a "
# name = "Akshay"
# name1 = "Aniket"
# print("This is a {1} and his brother is {0}.".format(name, name1))
# # print(f"This is a {name} and his brother is {name1}.")
# lst = [61, 1, 2, 3, 4, 41]
# print(alst[1])
# del lst[0]
# print(lst)

# alst = (61, 1, 2, 3, 4)
# A=alst.

# A = {12, 331, 12, 31, 31, 23, 6, 7, 8, 9}
# # set

# A = {
#     "Name": "Akshay",
#     "Marks": 37,
#     "Roll number": 67
# }

# for i in A:
#     print(i)

class Employee:
    def __init__(self, gname, gsalary):
        self.name = gname
        self.salary = gsalary


harry = Employee("Akshay", 34)
print(harry.name)
print(harry.salary)
