# Teddy Rodd
# Number Guessing Game

import random
import os
import platform

def main():
    number = create_number()
    while True:
        guess = get_user_input()
        win = check_match(guess,number)
        if win == True:
            print(f"You Win! The number was {number}")
            break
        else:
            print("Try again")


def create_number():
    number = random.randint(1,6)
    return number


def get_user_input():
    guess = int(input("What number am I thinking off? "))
    return guess


def check_match(guess,number):
    if guess == number:
        win = True
        return win
    else:
        win = False
        return win


def clear_screan():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


if __name__ == "__main__":
    main()
    print("Have a great day!\n")