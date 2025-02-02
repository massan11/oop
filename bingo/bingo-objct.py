import random

class BingoGame:
    player_list = []
    def __init__(self):
        self.name = input("Inter your name: ")
        self.__rand_num = random.randint(0, 10)
        self.__health = 3
        self.__win_state = False
        self.player_list.append(self)
        
    def chech_num(self):
        num = int (input(f"{self.name}, Enter a number: "))
        if num > self.__rand_num:
            print("chose lower number")
        elif num < self.__rand_num:
            print("chose higher number")
        else:
            print("Bingo!")
            self.__win_state = True
        self.minus_health()
        print(f"you have {self.__health} health")
            
    def minus_health(self):
        self.__health -= 1
        
    def has_user_live(self):
        if self.__health > 0:
            return True
        return False
        
    def has_won(self):
        return self.__win_state
    
    @classmethod
    def get_player_list(cls):
        if any(player.has_won() is True for player in cls.player_list):
            return True
        return False
    
class GameController:
    def __init__(selj):
        while True:
            for player in BingoGame.player_list:
                if player.has_user_live():
                    player.chech_num()
            if BingoGame.get_player_list():
                print("end of game!")
                break
                    

        
if __name__ == "__main__":
    while True:
        order = input ("what do you want to do? ")
        if order == "add":
            BingoGame()
        elif order == "start":
            GameController()
        elif order == "exit":
            break
        