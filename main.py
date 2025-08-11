foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    elif food == "":
        print("You forgot to enter a food")
        continue
    else:
        while True:
            try:
                price = float(input(f"Enter the price of the {food}: €"))
            except ValueError:
                print("Invalid input please enter a number")
                continue
            foods.append(food)
            prices.append(price)
            break

print("----- YOUR CART -----")

for food in foods:
    print(food, end=f" €{price}\n")

for price in prices:
    total += price

print()
print(f"Your total is: €{total}")
