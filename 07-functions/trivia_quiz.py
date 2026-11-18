#TRIVIA GAME
#Paige LaBarr
#October 26, 2026
#Description: Ask the user 5 trivia questions, display results
#Correct answers are worth 10 points on the first try and 5 points on the second try
#Maximum possible score is 50 points

#greeting message - welcome & ask for player's name
def greeting():
    print("Welcome to trivia!")
    print("Today's quiz is about state capitals!")
    name = input("What's your name? \n> ")
    print(f"Welcome, {name}. Let's get started. You'll have 5 questions.")
    return name

#quiz function - where the trivia happens!
def quiz():
    states = ["New York", "Pennsylvania", "Vermont", "Ohio", "New Jersey"]
    capitals = ["Albany", "Harrisburg", "Montpelier", "Columbus", "Trenton"]

    score = 0
    i = 0
    for state in states:
        response = input(f"What is the capital of {state}?\n> ")
        if response == capitals[i]:
            score += 10
            print(f"Awesome. +10 points for you! Score: {score}")
        else:
            print("That's incorrect - guess again.")
            response = input(f"What is the capital of {state}? \n> ")
            if response == capitals[i]:
                score += 5
                print(f"Nice. +5 points for you! Score: {score}")
            else:
                print(f"Incorrect again. 0 points in this round. Score: {score}")
        i += 1
    return score

#say goodbye and include stats
def goodbye(final_score, name):
    if final_score == 50:
        print("\n\nAMAZING! 50 / 50")
    else:
        print(f"\n\nFinal score: {final_score} / 50")
    print(f"Thanks for playing, {name}!")

# RUN THE GAME
# call greeting and store the name to reuse it
name = greeting()
score = quiz() # run the quiz
again_response = input("Do you wish to play again? Y for yes.\n> ")
while again_response == "Y": # option to play again
    score = quiz()
    again_response = input("Do you wish to play again? Y for yes.\n> ")
goodbye(score, name) # display the score and say goodbye using user's name