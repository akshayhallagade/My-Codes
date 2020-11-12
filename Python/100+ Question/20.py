# Question:
"""
Define a class with a generator which can iterate the numbers, which are divisible by 7, 
between a given range 0 and n.
"""
# Hints:
"""
Consider use yield.
"""


def putnumber(n):
    i = 0
    while i <= n:
        i += 1
        if i % 7 == 0:
            yield i


for i in putnumber(100):
    print(i)
