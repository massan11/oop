class Employee:
    salary = 3000 #class variable

    def __init__(self, name, age):
        self.name = name #object variable
        self.age = age

    def work(self, project_name):
        return f"I am working on {project_name}"
    def introdoce(self):
        return f"my name is {self.name}"

emp1 = Employee("hassan", 32)
emp2 = Employee("ali", 43)

print(emp1.name, emp1.age, emp1.salary)
print(emp1.introdoce())


