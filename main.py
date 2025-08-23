import random

options = ("rock", "paper", "scissors")
running = True
victory_message = "You win!"

while running:
    computer = random.choice(options)
    player = None

    while player not in options:
        player = input("Enter a choice (rock, paper, scissor): ")

    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("Its a tie!")
    elif player == "rock" and computer == "scissors":
        print(victory_message)
    elif player == "paper" and computer == "rock":
        print(victory_message)
    elif player == "scissors" and computer == "paper":
        print(victory_message)
    else:
        print("You lose!")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing")
