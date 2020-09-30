# Question:
"""
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 
and n.
"""
# Hints:
"""
Consider use yield.
"""


def putnumber(n):
    i = 1
    empty = []
    while i <= n:
        if i % 7 == 0:
            empty.append(i)
            i += 1
    print(empty)


putnumber(100)
