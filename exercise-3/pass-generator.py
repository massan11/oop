from abc import ABC,abstractmethod
import random


class Generating(ABC):
    @abstractmethod
    def generate(self):
        pass

class GenerateStr(Generating):
    def generate(self):
        return "".join(random.choices("qwertyuiopasdfghjklzxcvbnm", k=20))
    
class GenerateNum(Generating):
    def generate(self):
        return "".join(random.choices("1234567890", k=20))
    
class GenerateMix(Generating):
    def generate(self):
        return "".join(random.choices("qwertyuiopasdfghjklzxcvbnm1234567890", k=20))
    
password = GenerateStr()
print(password.generate())

password = GenerateNum()
print(password.generate())

password = GenerateMix()
print(password.generate())