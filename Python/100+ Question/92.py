# Question:
"""
With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose 
elements are intersection of the above given lists.
"""
# Hints:
"""
Use set() and "&=" to do set intersection operation.
"""
aa = [1, 3, 6, 78, 35, 55]
bb = [12, 24, 35, 24, 88, 120, 155]
aa = set(aa)
bb = set(bb)
aa &= bb
result = list(aa)
print(result)
