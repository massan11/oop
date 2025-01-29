class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        return f"{self.name}, {self.age}"
    
class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major
    def displayStudent(self):
        return f"{self.name}, {self.age}, {self.major}"
    
st1 = Student("Ali", 12, 3)
print(st1.displayStudent())
