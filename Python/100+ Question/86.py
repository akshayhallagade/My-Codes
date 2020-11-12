# Question:
"""
Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].
"""
# Hints:
"""
Use list comprehension to delete a bunch of element from a list.
"""
aa = [5, 6, 77, 45, 22, 12, 24]
aa = [i for i in aa if i % 2 != 0]
print(aa)
