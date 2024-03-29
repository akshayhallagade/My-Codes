# Question:
"""
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
Then the function needs to print the last 5 elements in the list.
"""
# Hints:
"""
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list
"""


def funct(n1, n2):
    list = []
    for i in range(n1, n2+1):
        list.append(i**2)
    return list[-5:]


print(funct(1, 20))
