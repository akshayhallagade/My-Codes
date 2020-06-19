#To change the class value of instance at a example. 
class employee:
    increment=1.5                              #to put the increment variable in employee class.
    def __init__(self,Name,Surname,Salary):    #very important to write the __init__ as is it.
        self.Name=Name
        self.Surname=Surname
        self.Salary=Salary

    def increase(self):
        self.Salary=self.Salary * employee.increment

Ankit=employee("Ankit", "Dhongadi", 5000)
Akshay=employee("Akshay", "Hallagade", 2000)

Akshay.increase()
print(Akshay.Salary)