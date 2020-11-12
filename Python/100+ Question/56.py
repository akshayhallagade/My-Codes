# Question:
"""
Write a function to compute 5/0 and use try/except to catch the exceptions.
"""
# Hints:
"""
Use try/except to catch exceptions.
"""


def errror():
    try:
        print(5/0)
    except:
        print("Divison by zero")
    finally:
        print("caught for cleanup")


errror()
