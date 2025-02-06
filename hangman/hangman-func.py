import random

def pick_word_group():
    word_group = input("Pick a word group: 1. Animals 2. Fruits 3. Countries\n")
    if word_group == "1":
        return ["elephant", "giraffe", "hippopotamus", "kangaroo", "koala", "lion", "penguin", "rhinoceros", "tiger", "zebra"]
    elif word_group == "2":
        return ["apple", "banana", "cherry", "grape", "kiwi", "lemon", "mango", "orange", "peach", "strawberry"]
    elif word_group == "3":
        return ["australia", "brazil", "canada", "china", "egypt", "france", "germany", "india", "japan", "russia"]
    else:
        print("Invalid choice. Please try again.")
        return pick_word_group()
    
def pick_word(word_group):
    return random.choice(word_group)

def display_word(word, guessed_letters):
    return "".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word_group = pick_word_group()
    word = pick_word(word_group)
    guessed_letters = set()
    attempts = 6
    while attempts > 0:
        print(display_word(word, guessed_letters))
        guess = input("Guess a letter: ")
        guessed_letters.add(guess)
        if guess not in word:
            attempts -= 1
        if set(word) == guessed_letters:
            print("You won!")
            break
    else:
        print("You lost!")
        print(f"The word was {word}")
        
hangman()

    
    
    