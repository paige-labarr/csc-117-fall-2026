import random


def play_game():
    secret_number = random.randint(1, 1000)
    attempts = 0

    print("\nI'm thinking of a number between 1 and 1000.")
    print("Try to guess it!")

    while True:
        guess_text = input("Your guess: ").strip()

        if not guess_text.isdigit():
            print("Please enter a whole number.")
            continue

        guess = int(guess_text)
        if guess < 1 or guess > 1000:
            print("Your guess must be between 1 and 1000.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low. Try again!")
        elif guess > secret_number:
            print("Too high. Try again!")
        else:
            print(f"You got it! The number was {secret_number}.")
            print(f"It took you {attempts} guesses.")
            break


def main():
    print("Welcome to the Number Guessing Game!")
    play_game()

    play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
    while play_again == "y":
        play_game()
        play_again = input("\nWould you like to play again? (y/n): ").strip().lower()

    print("Thanks for playing!")


if __name__ == "__main__":
    main()