questions = (
    "What's 9+10?: ",
    "What's the capital of France?: ",
    "How many hours are in a day?: ",
    "Which planet is known as the Red Planet?: ",
    "What's the largest mammal on Earth?: ",
)

options = (
    ("A. 19", "B. 21 (You stupid)"),
    ("A. Paris", "B. Amsterdam"),
    ("A. 24", "B. 48"),
    ("A. Saturn", "B. Mars"),
    ("A. Elephant", "B. Blue whale"),
)

answers = ("B", "A", "A", "B", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("--------------------")
print("      RESULTS       ")
print("--------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end="")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
