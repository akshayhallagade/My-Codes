# Question:
"""
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
"""
# Hints:
"""
To override a method in super class, we can define a method with the same name in the super class.
"""


class shape:
    def __init__(self):
        self.length = 1

    def area(self):
        return 0


class square(shape):
    def __init__(self, l):
        self.length = l

    def area(self):
        self.area = self.length**2
        return self.area


asquare = square(3)
print(asquare.area())
