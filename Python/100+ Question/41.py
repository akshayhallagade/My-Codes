# Question:
"""
Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included). 
"""
# Hints:
"""
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use tuple() to get a tuple from a list.
"""


def funct(n1, n2):
    list = []
    for i in range(n1, n2+1):
        list.append(i**2)
    return tuple(list[5:])


print(funct(1, 20))
