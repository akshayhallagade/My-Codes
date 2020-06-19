#To change the value of salary as we required.
class employee:                             
    def __init__(self,Name,Surname,Salary):    #very important to write the __init__ as is it.
        self.Name=Name
        self.Surname=Surname
        self.Salary=Salary
    def increase(self):
        self.Salary=int(self.Salary * self.increment)
    @classmethod
    def change_increment(cls,amount):
        cls.increment=amount
            
Ankit=employee("Ankit", "Dhongadi", 5000)
Akshay=employee("Akshay", "Hallagade", 2000)

print(Akshay.Salary)
employee.change_increment(3)
Akshay.increase()
print(Akshay.Salary)