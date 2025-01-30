class Employee:
    salary = 3000 #class variable
    total_employee = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name #object variable
        self.last_name = last_name
        Employee.total_employee += 1

    def fullname(self):
        return "{} {}".format (self.first_name, self.last_name) 
    
    @classmethod
    def raise_salary(cls, new_salary):
        if type(new_salary) == int: 
            cls.salary = new_salary
        else:
            raise ValueError
        
    @classmethod
    def creat_from_sring(cls, string):
        first_name, last_name = string.split("-")
        return cls(first_name, last_name)

    @staticmethod
    def is_work_day(date):
        if date.weekday() == 5 or date.weekday() == 6:
            return False
        return True
    

    


# emp1 = Employee("hassan", "kazemi")
# emp2 = Employee("ali", "tavallali")


import datetime

date = datetime.date(2024, 1, 30)

emp3 = Employee.creat_from_sring("ali-tavallali")
print(emp3.fullname())
print(emp3.is_work_day(date))
# print("before")
# print(emp1.salary)
# print(emp2.salary)

# Employee.raise_salary("3444")

# print("after")
# print(emp1.salary)
# print(emp2.salary)


