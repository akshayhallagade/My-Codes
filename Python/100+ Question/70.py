# Question:
"""
Please write assert statements to verify that every number in the list [2,4,6,8] is even.
"""
# Hints:
"""
Use "assert expression" to make assertion.
"""
# a = [2, 4, 6, 8]
# for i in a:
#     if a % 2 == 0:
#         print("yes, it is correct.")

li = [2, 4, 6, 8]
for i in li:
    # assert shows error if condition is false. If it is True nothing happens.
    assert i % 2 == 0
