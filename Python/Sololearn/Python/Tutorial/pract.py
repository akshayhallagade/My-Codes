
# # We can also change the name of the function.


# def shout(word):
#     return word + "!"


# speak = shout
# output = speak("shout")
# print(output)

# def add(x, y):
#     return x+y


# def do_twice(func, x, y):
#     return func(func(x, y), func(x, y))


# print(do_twice(add, 5, 3))

# import random
# for i in range(1, 5):
#     value = random.randint(1, 6)
#     valu=random
#     print(value)

# def sum(a, b):
#     return a+b


# def operation(func, a, b):
#     return func(func(a, b), func(a, b))


# print(operation(sum, 4, 5))
# try:
#     num1 = 7
#     num2 = 0
#     print(num1/num2)
# except ZeroDivisionError:
#     print('wrong input')
# try:
#     variable = 10
#     print(variable)
#     print(variable/2)
# except ZeroDivisionError:
#     print("sdfnk")
# finally:
#     print("Error occured")

# print(1)
# raise ValueError  # adding error
# print(2)

try:
    print(1 / 0)
except ZeroDivisionError:
    print("Hello")
