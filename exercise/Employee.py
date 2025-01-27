class Employee:
    salary = 3000 #class variable

    def __init__(self, name, age):
        self.name = name #object variable
        self.age = age

emp1 = Employee("hassan", 32)
emp2 = Employee("ali", 43)

print(emp1.name, emp1.age, emp1.salary)
print(emp2.name, emp2.age, emp2.salary)


