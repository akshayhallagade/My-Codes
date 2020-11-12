# Question:
"""
Define a function which can generate and print a list where the values are square of numbers between 1 and 20 
(both included).
"""
# Hints:
"""
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
"""


def funct(n1, n2):
    list = []
    for i in range(n1, n2+1):
        list.append(i**2)
    return list


print(funct(1, 20))
