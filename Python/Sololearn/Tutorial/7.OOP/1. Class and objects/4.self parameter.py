class Myclass:
    def funct(self):
        return "Hello"

"""
we are calling 'funct()' method using 'ob.func()' without passing any arguments. 
However, the functions definition has 'self' as the parameter 'def func(self)'.

It worked because whenever the object calls its method, the object itself is passed as the first arguments.
So, 'ob.func' translates into 'MyClass.func(ob)'.

The first arguments of the function i  class must be the object itself. This is conventionally. called 'self'.
"""
ob=Myclass()
print(ob.funct())