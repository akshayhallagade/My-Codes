#To change the class value of instance at a example. 
class employee:                             
    def __init__(self,Name,Surname,Salary):    #very important to write the __init__ as is it.
        self.Name=Name
        self.Surname=Surname
        self.Salary=Salary
        self.increment=1.4                     #to put the increment variable in instance class(self).
    def increase(self):
        self.Salary=self.Salary * self.increment

Ankit=employee("Ankit", "Dhongadi", 5000)
Akshay=employee("Akshay", "Hallagade", 2000)

Akshay.increase()
print(Akshay.Salary)