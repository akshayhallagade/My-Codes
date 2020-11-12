# Question:
"""
Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) 
and the values are square of keys.
"""
# Hints:
"""
Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
"""


def funct(n1, n2):
    dicti = dict()
    for i in range(n1, n2+1):
        dicti[i] = i**2
    return dicti


print(funct(1, 3))
