# Question:
"""
Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method 
which can compute the area. 
"""
# Hints:
"""
Use def methodName(self) to define a method.
"""


class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breath = b

    def methodName(self):
        self.area = self.length*self.breath
        return self.area


aRectangle = Rectangle(3, 4)
print(aRectangle.methodName())
