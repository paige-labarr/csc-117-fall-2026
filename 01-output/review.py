# ask the user for name
name = input("What is your name? ")

# greet user by name
print(f"Hello {name}")

# ask the user what year they were born
birth_year = int(input("What year were you born? "))

# give the user their approximate age in dog years
age = 2026 - birth_year
# print(f"You are {age} years old in human years. 🧑")
dog_age = age * 7
print(f"You are {dog_age} years old in dog years. 🐕")