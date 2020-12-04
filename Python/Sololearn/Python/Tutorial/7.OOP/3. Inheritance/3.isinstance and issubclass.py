class Polygon:
    pass
class Triangle(Polygon):
    pass
t=Triangle()

#checking subclass and instance of the class.
print(isinstance(t, Triangle))
print(isinstance(t, Polygon))
print(isinstance(t, int))
print(isinstance(t, object))
print(issubclass(Polygon, Triangle))
print(issubclass(Triangle, Polygon))