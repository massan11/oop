import random

rand_num = random.randint(0, 10)
health = 3

def chech_num(num):
    if num > rand_num:
        return (False, "chose lower number")
    elif num < rand_num:
        return (False, "chose higher number")
    else:
        return (True, "Bingo!")
     
name = (input("what is your name? "))
while True:
    if health == 0:
        print(f"you lose! the number was {rand_num}")
        break
    num = int(input(f"{name}, Enter a number: "))
    result = chech_num(num)
    if result[0] == False:
        print(result[1])
    else:
        print(result[1])
        break
    health -= 1
print("end of game!") 
    