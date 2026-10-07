#range function
#for loop
#for n in range(100, 0, -1):
#    print(n, end=" ")

# for x in range(1, 11, 1):
#     for n in range(1, 11, 1):
#         print(n*x, end="\t")
#     print()

import time
# #countdown
# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)
# print("HAPPY OCTOBER")

# classes = ["CS Portal", "Python", "Writing", "Info Systems"]
# for course in classes:
#     print(f"I am taking {course} this semester!")

#count up from 1 to 10
# counter = 1
# while counter <= 10:
#     print(counter)
#     counter += 1

#count down from 10 to 1... 10, 9, 8, ... 1
# counter = 10
# while counter >= 1:
#     print(counter)
#     time.sleep(1)
#     counter -= 1

secret_number = 22
guess =int(input("Guess my secret number: "))
while guess != secret_number: # != means not equal
    guess = int(input("Guess again: "))
print("Yay! You guessed it!")