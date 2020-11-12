# Question:
"""
Define a function that can accept two strings as input and print the string with maximum length in console. 
If two strings have the same length, then the function should print al l strings line by line.
"""
# Hints:
"""
Use len() function to get the length of a string
"""


def functi(n1, n2):
    if len(n1) > len(n2):
        return n1
    elif len(n2) > len(n1):
        return n2
    else:
        return n1+"\n"+n2


print(functi(input(), input()))
