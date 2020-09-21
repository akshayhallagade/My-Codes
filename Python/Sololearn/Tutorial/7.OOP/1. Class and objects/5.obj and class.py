class Number:
    def add(self,a,b):
        return a+b
    def multiply(self,a,b):
        return a*b

#Instantiating the objects.
n1=Number()

sum=n1.add(2,3)
print(sum)
multi=n1.multiply(2,5)
print(multi)