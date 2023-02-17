"""Bagels, by AI Sweigart ai@inventwithpython.com
A deductive logic game where you must guess a number based on clues.
View this code at https://nostarch.com/big-book-small-python-projects
"""

import random

NUM_DIGITS = 3 #(!)Try setting this to 1 or 10.
MAX_GUESSES = 10 #(!)Try setting this to 1 0r 100.


def main():
    print(f"""Bagels, a deductive logic game.
    
    I am thinking of a {NUM_DIGITS}- digit number with no repeated digits.
    Try to guess what  it is. Here are some glues:
    When I say:      That means:
    Pico             One digit is correct but in the wrong position.
    Fermi            One digit is correct and is in the right position.
    Bagels           No digits is correct.
    
    For example, if the secret number was 248 and your guess was 843, the clues would be fermi pico.""")