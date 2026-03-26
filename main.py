# Teddy Rodd
# Number Guessing Game

import random
import os
import platform

def main():
    number = create_number()


def create_number():
    number = random.randint(1,6)
    return number


def get_user_input():
    guess = input("What number am I thinking off? ")
    return guess


def check_match():
    pass


def clear_screan():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


if __name__ == "__main__":
    main()
    print("Have a great day!\n")