class Car:
    def __init__ (self):
        self.color = "red"
        self.speed = 100

    def set_speed(self, new_speed): # setter
        self.speed = new_speed

    def get_speed(self):  #getter
        return self.speed



praid = Car()
print(praid.color)
print(praid.speed)
praid.set_speed(200)


# praid.speed = 200
print(praid.get_speed())