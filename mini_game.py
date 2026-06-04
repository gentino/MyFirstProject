"""
Mini Interactive Number Guessing Game
Run: python mini_game.py
"""

import random

def main():
    print("🎯 Guess the Number (1-20)")
    secret = random.randint(1, 20)

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print("🎉 Correct! You win.")
            break

if __name__ == "__main__":
    main()
