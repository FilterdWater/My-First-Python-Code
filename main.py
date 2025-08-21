import random

lowest_number = 1
highest_num = 100

answer = random.randint(lowest_number, highest_num)

guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_number} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_number or guess > highest_num:
            print("That number is out of range")
            print(f"Select a number between {lowest_number} and {highest_num}")
        elif guess < answer:
            print("Too low, Try again.")
        elif guess > answer:
            print("Too high, try again.")
        else:
            print(f"Correct! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False

    else:
        print("Invalid guess")
        print(f"Select a number between {lowest_number} and {highest_num}")
