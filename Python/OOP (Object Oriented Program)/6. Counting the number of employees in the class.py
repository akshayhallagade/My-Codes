#use of __dict__.
class employee: 
    no_of_employee=0                            
    def __init__(self,Name,Surname,Salary):    #very important to write the __init__ as is it.
        self.Name=Name
        self.Surname=Surname
        self.Salary=Salary
        employee.no_of_employee+=1

print(employee.no_of_employee)                  #printing total number of the employers data enterd. 
Ankit=employee("Ankit", "Dhongadi", 5000)
print(employee.no_of_employee)                  #printing total number of the employers data enterd.
Akshay=employee("Akshay", "Hallagade", 2000)
print(employee.no_of_employee)                  #printing total number of the employers data enterd.