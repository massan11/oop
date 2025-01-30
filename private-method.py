class Computer:
    def __init__(self):
        self.a = 10
        self._b = 20
        self.__c = 30

    def public_process(self):
        print("public")

    def __private_method(self):
        print("private")

pc = Computer()
pc.public_process()
# pc.__private_method()  ERROR  
