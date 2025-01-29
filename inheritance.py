# Person
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

# Employee
class Employee(Person):
    salary = 3000
    def __init__(self, first_name, last_name, position):
        super().__init__(first_name, last_name)
        # Person.__init__(self, first_name, last_name)
        self.position = position
        
    def job(self):
        return f"I am {self.first_name} {self.last_name}, {self.position}"

class Manager:
    def authority(self):
        return "can fire anyone"

# CTO
class CTO(Employee, Manager):
    salary = 6000
    def job(self):
        return f"I am {self.first_name} {self.last_name}, CTO of the compani"


# Intern
class Intern(Employee):
    salary = 1000
    def job(self):
        return f"I am {self.first_name} {self.last_name}, learning new things"

emp1 = Employee("Ali", "Tavallali", "backend developer")
emp2 = CTO("Ali", "Tavallali", "backend developer")
emp3 = Intern("Ali", "Tavallali", "backend develiper")
print(emp1.job())
print(emp1.salary)
print(emp2.job())
print(emp2.salary)
print(emp2.authority())
print(emp3.job())
print(emp3.salary)