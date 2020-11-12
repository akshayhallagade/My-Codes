# No Working # Question:
"""
Define a custom exception class which takes a string message as attribute.
"""
# Hints:
"""
To define a custom exception, we need to define a class inherited from Exception.
"""


class MyError(Exception):
    """My Own Exception class

    Args:
        Exception (msg): Explanation of the errors
    """

    def __init__(self, msg):
        self.msg = msg


error = MyError("something wrong")
