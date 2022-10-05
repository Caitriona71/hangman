# You can delete these comments, but do not change the name of this file

import random

from words import word_list

print("Let's play Hangman.")
print(show_hangman(attempts))

# Select a random word


def get_a_word():

    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_blanks = "_" * len(word)
    guesses = False
    guesses_letters = []
    guesses_words = []
    attempts = 6


def show_hangman(attempts):
    phases = [ """
                    +---+
                    |   |
                    |
                    |     
                    |      
                    |     
                  ========
                """,
                """
                    +---+
                    |   |
                    |   O
                    |     
                    |      
                    |     
                  ========
                """,
                """
                    +---+
                    |   |
                    |   O
                    |   |
                    |        
                    |    
                  ========
                """,
                """
                    +---+
                    |   |
                    |   O
                    |  /|
                    |
                    |     
                  ========
                """,
                """
                    +---+
                    |   |
                    |   O
                    |  /|\
                    |     
                    |     
                  ========
                """,
                """
                    +---+
                    |   |
                    |   O
                    |  /|\
                    |  /
                    |      
                  ========
                """,
                """
                    +---+
                    |   |
                    |   O
                    |  /|\
                    |  / \ 
                    |
                  ========
                """]
    return phases[attempts]













