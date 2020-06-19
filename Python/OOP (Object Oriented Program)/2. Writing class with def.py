#writing class data with def function.
class employee:
    def __init__(self,Name,Surname,Salary):    #very important to write the __init__ as is it.
        self.Name=Name
        self.Surname=Surname
        self.Salary=Salary

Ankit=employee("Ankit", "Dhongadi", 5000)
Akshay=employee("Akshay", "Hallagade", 2000)

print(Akshay.Salary)
print(Akshay.Name)
print(Akshay.Surname,"\n")
print(Ankit.Salary)
print(Ankit.Name)
print(Ankit.Surname)