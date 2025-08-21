# define function

def say_hello():
    print("Hello, world")
    return 100

value = say_hello()  # Call function
print(f"{value = }")

def greet(whom="world"):
    print(f"Hello, {whom}")

greet('Mom')
greet('world')
greet()

def greet_many(*whom):
    for who in whom:
        print(f"Hello, {who}")

greet_many('Lucy', 'Ricky', 'Fred', 'Ethel')
greet_many()

