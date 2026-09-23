import random 

#randint will generate a random integer between 1st and 2nd value
#1 and 6 are included
name = input("What's your name? ") 
roll1 = random.randint(1, 6) 
roll2 = random.randint(1, 6)
total = roll1 + roll2

print(f"{name}, your 1st roll is {roll1} and your 2nd roll is {roll2}.")
print(f"The total is {total}.")

if roll1 == roll2:
    print("YOU ROLLED DOUBLES!")

if roll1 == 1 and roll2 == 1:
    print("YOU ROLLED SNAKE EYES!")