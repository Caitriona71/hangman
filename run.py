# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

from words import word_list

print("Let's play Hangman.")

# Select a random word


def get_a_word():

    word = random.choice(word_list)
    return word.upper()


def play():
    guesses = False
    guesses_letters = []
    guesses_words = []
    attempts = 6
















