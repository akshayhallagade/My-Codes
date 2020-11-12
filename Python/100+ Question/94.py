# Question:
"""
Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can 
print "Male" for Male class and "Female" for Female class.
"""
# Hints:
"""
Use Subclass(Parentclass) to define a child class.
"""


class Person:
    def getGender(self):
        return "Unknown"


class Male(Person):
    def getGender(self):
        return "Male"


class Female(Person):
    def getGender(self):
        return "Female"


male1 = Male()
print(male1.getGender())
male2 = Female()
print(male2.getGender())
