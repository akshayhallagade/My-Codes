# Question:
"""
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half
values in one line. 
"""
# Hints:
"""
Use [n1:n2] notation to get a slice from a tuple.
"""


def funct(n1, n2):
    list = []
    for i in range(n1, n2+1):
        list.append(i**2)
    print(tuple(list[:5]))
    print(tuple(list[5:]))


funct(1, 10)
