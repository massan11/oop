class Employee:
    salary = 3000 #class variable
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name #object variable
        self.last_name = last_name
        # self.fullname = "{} {}".format (self.first_name, self.last_name)

    @property
    def fullname(self):
        return "{} {}".format (self.first_name, self.last_name) 
    
    @fullname.setter
    def fullname(self, name):  
        self.first_name, self.last_name = name.split(" ")   

    @fullname.deleter
    def fullname(self):
        self.first_name = None
        self.last_name = None

emp1 = Employee("Hassan", "Zare") 
print(emp1.fullname)

emp1.fullname = "Shahrokh Estakhry"
print(emp1.fullname)

del emp1.fullname
print(emp1.fullname)