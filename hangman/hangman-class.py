import random

class Hangman:
    def __init__(self):
        self.word_group = self.pick_word_group()
        self.word = self.pick_word()
        self.guessed_letters = set()
        self.attempts = 6
        
    def pick_word_group(self):
        word_group = input("Pick a word group: 1. Animals 2. Fruits 3. Countries\n")
        if word_group == "1":
            return ["elephant", "giraffe", "hippopotamus", "kangaroo", "koala", "lion", "penguin", "rhinoceros", "tiger", "zebra"]
        elif word_group == "2":
            return ["apple", "banana", "cherry", "grape", "kiwi", "lemon", "mango", "orange", "peach", "strawberry"]
        elif word_group == "3":
            return ["australia", "brazil", "canada", "china", "egypt", "france", "germany", "india", "japan", "russia"]
        else:
            print("Invalid choice. Please try again.")
            return self.pick_word_group()

    def pick_word(self):
        return random.choice(self.word_group)
    
    def display_word(self):
        return "".join([letter if letter in self.guessed_letters else "_" for letter in self.word])
    
class HangmanGame(Hangman):
    def __init__(self):
        super().__init__()
        
    def play(self):
        while self.attempts > 0:
            print(self.display_word())
            guess = input("Guess a letter: ")
            self.guessed_letters.add(guess)
            if guess not in self.word:
                self.attempts -= 1
            if set(self.word) == self.guessed_letters:
                print("You won!")
                break
        else:
            print("You lost!")
            print(f"The word was {self.word}")
            
game = HangmanGame()
game.play()
  