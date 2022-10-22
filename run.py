import random
from words import word_list

print("I know your're dying to play this game. So get in the swing and give it a try!")
print("Can you guess the secret word or are you in for the bad noose! Don't hang around.")
print("The neck's game awaits you. Didn't you know, I got roped into this?!")
print("Let's play hangman!")

# Choose a secret word
randomWord = random.choice(word_list)

for x in randomWord:
  print("_", end=" ")


def print_hangman(wrong):
  if (wrong == 0):
    print("\n+---+")
    print("    |")
    print("    |")
    print("    |")
    print("    |")
    print("=======")
  elif (wrong == 1):
    print("\n+---+")
    print("O   |")
    print("    |")
    print("    |")
    print("    |")
    print("=======")
  elif (wrong == 2):
    print("\n+---+")
    print("O   |")
    print("|   |")
    print("    |")
    print("    |")
    print("=======")
  elif (wrong == 3):
    print("\n+---+")
    print(" O  |")
    print("/|  |")
    print("    |")
    print("    |")
    print("=======")
  elif (wrong == 4):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("    |")
    print("    |")
    print("=======")
  elif (wrong == 5):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("/   |")
    print("    |")
    print("=======")
  elif (wrong == 6):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("/ \ |")
    print("    |")
    print("=======")


def printWord(guessedLetters):
  counter = 0
  correctLetters = 0
  for char in randomWord:
    if (char in guessedLetters):
      print(randomWord[counter], end=" ")
      correctLetters += 1
    else:
      print(" ", end=" ")
    counter += 1
  return correctLetters


def printLines():
  print("\r")
  for char in randomWord:
    print("\u203E", end=" ")


length_guess_word = len(randomWord)
attempts_wrong = 0
guess_index = 0
letters_already_guessed = []
letters_correct = 0

while (attempts_wrong != 6 and letters_correct != length_guess_word):
  print("\nLetters already guessed: ")
  for letter in letters_already_guessed:
    print(letter, end=" ")
  # Prompt user for input
  letterGuessed = input("\nGuess a letter: ")
  # User is right
  if (randomWord[guess_index] == letterGuessed):
    print_hangman(attempts_wrong)
    # Print word
    guess_index += 1
    letters_already_guessed.append(letterGuessed)
    letters_correct = printWord(letters_already_guessed)
    printLines()
  # User was wrong
  else:
    attempts_wrong += 1
    letters_already_guessed.append(letterGuessed)
    # Update the drawing
    print_hangman(attempts_wrong)
    # Print word
    letters_correct = printWord(letters_already_guessed)
    printLines()
           
print("Game over! Thanks for playing :)")