import random

# function to display a welcome message
def display_message():
    print("Welcome to my math game!")
    print("In this game, you can:\n\t➕ add\n\t➖ subtract\n\t✖️  multiply\n\t➗ divide")
    print("Get ready for some math! :) ")
    print("When you're done, type STOP")

# function to ask the user which operation they want to practice
def add_or_subtract_or_mult_or_div():
    response = input("Would you like to add or subtract or multiply or divide? ")
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    if response == "add" or response == "ADD" or response == "a":
        print(f"Add together {num1} and {num2}.")
        response_add = int(input("Type your answer here: "))
        if response_add == add(num1, num2):
            print("Yay! You are correct. :D ")
        else:
            print("That's not it. Sorry. :( ")
    if response == "subtract":
        print(f"Subtract: {num1} - {num2}")
        response_subtract = int(input("Type your answer here: "))
        if response_subtract == subtract(num1, num2):
            print("Yay! You are correct. :D ")
        else:
            print("That's not it. Sorry. :( ")
    if response == "multiply":
        print(f"Multiply: {num1} * {num2}")
        response_mult = int(input("Type your answer here: "))
        if response_mult == multiply(num1, num2):
            print("Yay! You are correct. :D ")
        else:
            print("That's not it. Sorry. :( ")
    if response == "divide":
        print("This practices floor division only.")
        print("... in other words, no decimals, just round down.")
        print(f"Divide: {num1} // {num2}")
        response_div = int(input("Type your answer here: "))
        if response_div == divide(num1, num2):
            print("Yay! You are correct. :D ")
        else:
            print("That's not it. Sorry. :( ")

# add function
def add(a, b):
    return a + b

# subtract function
def subtract(a, b):
    return a - b

# multiply function
def multiply(a, b):
    return a * b

# divide function
def divide(a, b):
    return a // b

display_message()


game_over = "not yet"
while game_over != "STOP":
    add_or_subtract_or_mult_or_div()
    game_over = input("Another question? (STOP if done): ")