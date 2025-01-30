def decor(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper

# def greetings():
#     print("hello")

# hello = decor(greetings)
# hello()

@decor
def greetings():
    print("hello")

greetings()