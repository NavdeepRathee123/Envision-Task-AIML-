import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def print_intro():
    print()
    print(Fore.CYAN + "🎯 Welcome to the Number Guessing Game!")
    print()
    print(Fore.YELLOW + "*" * 80)
    print("🤖 I've picked a secret number... Can you find it?")
    print("❌ Type 0 anytime if you'd like to exit the game.")
    print()
    print(Fore.GREEN + "📌 Here's how I'll guide you:")
    print(" 🔴 More than 75 away  : You're way off!")
    print(" 🟠 More than 50 away  : Still far, keep going!")
    print(" 🟡 More than 25 away  : Getting warmer!")
    print(" 🔵 More than 10 away  : Getting closer, push ahead!")
    print(" 🟢 Within 10          : So Close!")
    print(" ⭐ Within 5           : Almost there!")
    print("If You want to See this rules menu again , Please enter 'help' ")
    print(Fore.YELLOW + "*" * 80)
    print()


def give_hint(secret, guess):
    diff = abs(secret - guess)
    if diff >= 75:
        return Fore.RED + ("🔴 You're way off! (⬆️ Go Higher)" if guess < secret else "🔴 You're way off! (⬇️ Go Lower)")
    elif diff >= 50:
        return Fore.MAGENTA + ("🟠 Still far, keep going! (⬆️ Go Higher)" if guess < secret else "🟠 Still far, keep going! (⬇️ Go Lower)")
    elif diff >= 25:
        return Fore.YELLOW + ("🟡 Getting warmer! (⬆️ Aim Higher)" if guess < secret else "🟡 Getting warmer! (⬇️ Aim Lower)")
    elif diff >= 10:
        return Fore.BLUE + ("🔵 Getting closer, push ahead! (⬆️ Try higher)" if guess < secret else "🔵 Getting closer, push ahead! (⬇️ Try lower)")
    elif diff >= 5:
        return Fore.CYAN + ("🟢 So Close! (⬆️ Just a bit higher!)" if guess < secret else "🟢 So Close! (⬇️ Just a bit lower!)")
    else:
        return Fore.GREEN + ("⭐ Almost there! (⬆️ Tiny bit higher!)" if guess < secret else "⭐ Almost there! (⬇️ Tiny bit lower!)")


def play_game():
    secret = random.randint(1, 100)
    attempts = 0
    print(Fore.CYAN + "🚀 New Game Started! Let's see if you can crack the code!")

    while True:
        user_input = input("👉 Enter Your Guess : ").strip().lower()

        if user_input == "help":
            print_intro()
            continue

        if not user_input.isdigit():
            print(Fore.RED + "⚠️ Invalid input. Please enter a number or type 'help'.")
            continue

        guess = int(user_input)

        if guess == 0:
            print(Fore.RED + f"🏳️ You chose to quit. The secret number was {secret}.")
            return "lose"

        attempts += 1

        if guess == secret:
            print(Fore.GREEN + f"🎉 Congratulations! You guessed it in {attempts} tries!")
            print(Fore.YELLOW + "🏆 Well played, champion — you have conquered the game! 👑")
            return "win"
        else:
            print(give_hint(secret, guess))


def main():
    print_intro()
    wins, losses = 0, 0

    play_again = True
    while play_again:
        result = play_game()
        if result == "win":
            wins += 1
        else:
            losses += 1

        choice = input(Fore.CYAN + "🔁 Would you like to Play Again ? (y/n): ").strip().lower()
        if choice != "y":
            play_again = False
            print(Fore.MAGENTA + "👋 Thanks for playing! See you next time.")

    print(Fore.YELLOW + f"\n📊 Total Wins : {wins}")
    print(Fore.YELLOW + f"📊 Total Losses : {losses}")


import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def print_intro():
    print()
    print(Fore.CYAN + "🎯 Welcome to the Number Guessing Game!")
    print()
    print(Fore.YELLOW + "*" * 80)
    print("🤖 I've picked a secret number... Can you find it?")
    print("❌ Type 0 anytime if you'd like to exit the game.")
    print()
    print(Fore.GREEN + "📌 Here's how I'll guide you:")
    print(" 🔴 More than 75 away  : You're way off!")
    print(" 🟠 More than 50 away  : Still far, keep going!")
    print(" 🟡 More than 25 away  : Getting warmer!")
    print(" 🔵 More than 10 away  : Getting closer, push ahead!")
    print(" 🟢 Within 10          : So Close!")
    print(" ⭐ Within 5           : Almost there!")
    print("If You want to See this rules menu again , Please enter 'help' ")
    print(Fore.YELLOW + "*" * 80)
    print()


def give_hint(secret, guess):
    diff = abs(secret - guess)
    if diff >= 75:
        return Fore.RED + ("🔴 You're way off! (⬆️ Go Higher)" if guess < secret else "🔴 You're way off! (⬇️ Go Lower)")
    elif diff >= 50:
        return Fore.MAGENTA + ("🟠 Still far, keep going! (⬆️ Go Higher)" if guess < secret else "🟠 Still far, keep going! (⬇️ Go Lower)")
    elif diff >= 25:
        return Fore.YELLOW + ("🟡 Getting warmer! (⬆️ Aim Higher)" if guess < secret else "🟡 Getting warmer! (⬇️ Aim Lower)")
    elif diff >= 10:
        return Fore.BLUE + ("🔵 Getting closer, push ahead! (⬆️ Try higher)" if guess < secret else "🔵 Getting closer, push ahead! (⬇️ Try lower)")
    elif diff >= 5:
        return Fore.CYAN + ("🟢 So Close! (⬆️ Just a bit higher!)" if guess < secret else "🟢 So Close! (⬇️ Just a bit lower!)")
    else:
        return Fore.GREEN + ("⭐ Almost there! (⬆️ Tiny bit higher!)" if guess < secret else "⭐ Almost there! (⬇️ Tiny bit lower!)")


def play_game():
    secret = random.randint(1, 100)
    attempts = 0
    print(Fore.CYAN + "🚀 New Game Started! Let's see if you can crack the code!")

    while True:
        user_input = input("👉 Enter Your Guess : ").strip().lower()

        if user_input == "help":
            print_intro()
            continue

        if not user_input.isdigit():
            print(Fore.RED + "⚠️ Invalid input. Please enter a number or type 'help'.")
            continue

        guess = int(user_input)

        if guess == 0:
            print(Fore.RED + f"🏳️ You chose to quit. The secret number was {secret}.")
            return "lose"

        attempts += 1

        if guess == secret:
            print(Fore.GREEN + f"🎉 Congratulations! You guessed it in {attempts} tries!")
            print(Fore.YELLOW + "🏆 Well played, champion — you have conquered the game! 👑")
            return "win"
        else:
            print(give_hint(secret, guess))


def main():
    print_intro()
    wins, losses = 0, 0

    play_again = True
    while play_again:
        result = play_game()
        if result == "win":
            wins += 1
        else:
            losses += 1

        choice = input(Fore.CYAN + "🔁 Would you like to Play Again ? (y/n): ").strip().lower()
        if choice != "y":
            play_again = False
            print(Fore.MAGENTA + "👋 Thanks for playing! See you next time.")

    print(Fore.YELLOW + f"\n📊 Total Wins : {wins}")
    print(Fore.YELLOW + f"📊 Total Losses : {losses}")


if __name__ == "__main__":
    main()