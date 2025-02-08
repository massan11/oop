from abc import ABC, abstractmethod
import requests
import random

class Joke(ABC):    
    @abstractmethod
    def get_random_joke(self):
        pass

class A (Joke):
    def get_random_joke(self):
        response = requests.get("https://api.chucknorris.io/jokes/random")
        return response.json()["value"]
        


class B (Joke):
    def get_random_joke(self):
        response = requests.get("https://geek-jokes.sameerkumar.website/api?format=json")
        return response.json()["joke"]
    


class C (Joke):
    def get_random_joke(self):
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        return response.json()["setup"] + "\n" + response.json()["punchline"]
    
def get_joke():
    joke = random.choice([A(), B(), C()])
    return joke.get_random_joke()

print(get_joke())   
