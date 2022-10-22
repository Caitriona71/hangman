import random
from words import word_list

print("Let's play Hangman.")

# Choose a secret word
secretWord = random.choice(word_list)

for x in secretWord:
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
  for char in secretWord:
    if (char in guessedLetters):
      print(secretWord[counter], end=" ")
      correctLetters += 1
    else:
      print(" ", end=" ")
    counter += 1
  return correctLetters


def printLines():
  print("\r")
  for char in secretWord:
    print("\u203E", end=" ")


length_guess_word = len(secretWord)
attempts_wrong = 0
guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while (attempts_wrong != 6 and current_letters_right != length_guess_word):
  print("\nLetters guessed so far: ")
  for letter in current_letters_guessed:
    print(letter, end=" ")
  # Prompt user for input
  letterGuessed = input("\nGuess a letter: ")
  # User is right
  if (secretWord[guess_index] == letterGuessed):
    print_hangman(attempts_wrong)
    # Print word
    guess_index += 1
    current_letters_guessed.append(letterGuessed)
    current_letters_right = printWord(current_letters_guessed)
    printLines()
  # User was wrong
  else:
    attempts_wrong += 1
    current_letters_guessed.append(letterGuessed)
    # Update the drawing
    print_hangman(attempts_wrong)
    # Print word
    current_letters_right = printWord(current_letters_guessed)
    printLines()
           
print("Game over! Thanks for playing :)")