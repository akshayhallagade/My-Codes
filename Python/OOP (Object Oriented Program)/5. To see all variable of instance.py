#TO see all variables of instance. 
#use of __dict__.
class employee:                             
    def __init__(self,Name,Surname,Salary):    #very important to write the __init__ as is it.
        self.Name=Name
        self.Surname=Surname
        self.Salary=Salary

Ankit=employee("Ankit", "Dhongadi", 5000)
Akshay=employee("Akshay", "Hallagade", 2000)

print(Akshay.__dict__)