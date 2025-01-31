from abc import ABC,abstractmethod

class Person(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    @abstractmethod
    def fullname(self):
        pass


class Employee(Person):
    salary = 3000
       
    def fullname(self):
        return "{} {}".format (self.first_name, self.last_name)
  
    
class Employer(Person):
    salary = 4000
    
    @property
    def fullname(self):
        return "{} {}".format (self.first_name, self.last_name)


emp1 = Employee("Ahmad", "Mostofi")
print(emp1.fullname())

emp2 = Employer("Mahmood", "Ranjbar")
print(emp2.fullname)