import random


def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

    return [random.choice(symbols) for _ in range(3)]
    # results = []
    # for symbol in range(3):
    #     results.append(random.choice(symbols))
    # return results


def print_row(row):
    print("-------------")
    print(" | ".join(row))
    print("-------------")


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 5
        elif row[0] == "🍉":
            return bet * 5
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
    return 0


def main():
    balance = 100

    print("-----------------------")
    print("Welcome to Python slots")
    print("Symbols: 🍒🍉🍋🔔⭐ ")
    print("-----------------------")

    while balance > 0:
        print("")
        print(f"Current balance: €{balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Input invalid, try again")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print("")
            print(f"You won €{payout}")
        else:
            print("")
            print("Sorry, you lost")

        balance += payout

        play_again = input("Play again? (y/N): ")

        print("")
        if play_again != "y":
            break

    print("------------------------------")
    print(f"  Final balance: €{balance}  ")
    print("------------------------------")


if __name__ == "__main__":
    main()
