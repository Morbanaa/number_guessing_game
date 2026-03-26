# Teddy Rodd
# Number Guessing Game

import random
import os
import platform

def main():
    number = create_number() # Creates random number
    clear_screan() # Cleans up the console
    
    # Runs while the random number and user guess do not match...
    while True:
        guess = get_user_input()
        win = check_match(guess,number)
        if win == True:
            print(f"You Win! The number was {number}")
            break
        else:
            print("Try again you")

# Creates random number 1-6
def create_number():
    number = random.randint(1,6)
    return number

# Asks user to guess a number
def get_user_input():
    while True:
        guess = input("What number am I thinking off? ")
        if guess.isdigit():
            guess = int(guess)
            break
        else:
            print("Must be a number")
            continue
    return guess

# Checks win state
def check_match(guess,number):
    if guess == number:
        win = True
        return win
    else:
        win = False
        return win

# Console formating
def clear_screan():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Program Entry point
if __name__ == "__main__":
    main()
    print("Have a great day!\n")