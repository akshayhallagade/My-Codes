# Question:
"""
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes",
otherwise print "No".
"""
# Hints:
"""
Use if statement to judge condition.
"""


def func(strr):
    if strr == "yes" or strr == "YES" or strr == "Yes":
        print("Yes")
    else:
        print("No")


func("Yes")
