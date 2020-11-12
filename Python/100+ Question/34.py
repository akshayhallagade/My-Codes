# Question:
"""
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the 
values are square of keys.
"""
# Hints:
"""
Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
"""


def funct(n1, n2):
    dictt = dict()
    for i in range(n1, n2+1):
        dictt[i] = i**2
    return dictt


print(funct(1, 20))
