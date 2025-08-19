import random

low = 1
high = 100
options = ("rock", "paper", "scissors")
numbers = ["1", "2", "3"]

# number = random.randint(low, high)
# number = random.random()
# option = random.choice(options)
random.shuffle(numbers)

print(numbers)
