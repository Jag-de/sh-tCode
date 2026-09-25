import string
import numpy as np

alphabet = [
    ['a','b','c','d'],
    ['e','f','g','h'],
    ['i','k','l','m'],
    ['n','o','p','q'],
    ['r','s','t','u'],
    ['v','w','x','y']]

flattened_ = np.array(alphabet).flatten()
np.random.shuffle(flattened_)
alphabets = set(string.ascii_lowercase)
alphabet = set(flattened_)
correct_guess = alphabets - alphabet
valid_characters = np.append(flattened_, list(correct_guess))


def call():
    print("You are missing?")

    while True:
        guess = input("Enter your guess: ").lower()

        if len(guess) != 1:
            print("Please enter only one character.")
            continue

        elif guess not in valid_characters:
            print("Invalid input! Please guess a character from the alphabet set.")
            continue

        elif guess in correct_guess:
            print(f"{guess} is definitively a normal variable.")
            break

        else:
            print(f"Keep guessing. {guess} is not correct!")


call()
