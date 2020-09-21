class Myclass:
    a=10
    def func(self):
        return "Akshay"
obj1=Myclass()  
obj2=Myclass()

print(obj1.a)
print(obj2.a)
print("..................")

obj1.a=0
obj2.a=100

print(obj1.a)
print(obj2.a)