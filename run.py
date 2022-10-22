import random
import time
# pip install pyfiglet
from pyfiglet import Figlet
from words import word_list                               

print("\033[1;34;40mI know you're \033[1;31;40mdying")
print("\033[1;34;40mto play this game.")
print("\033[1;34;40mSo get in the \033[1;32;40mswing")
print("\033[1;34;40mand give it a try!")
print("Can you guess the secret word?")
print("\033[1;34;40mOr are you in for bad \033[1;31;40mnoose!")
print("\033[1;34;40mDon't \033[1;32;40mhang \033[1;34;40maround.")
print("\033[1;34;40mThe \033[1;31;40mneck's \033[1;34;40mgame awaits you!")
print("\033[1;34;40mSorry you got \033[1;32;40mroped \033[1;34;40minto this?!") 
print("\r")
f = Figlet (font='doom')
print(f.renderText('Hangman'))
print("\r")
print("\033[1;32;40mLet's play!")
print("\r")

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
    print("=======\n\n")
  elif (wrong == 1):
    print("\n+---+")
    print("O   |")
    print("    |")
    print("    |")
    print("    |")
    print("=======\n\n")
  elif (wrong == 2):
    print("\n+---+")
    print("O   |")
    print("|   |")
    print("    |")
    print("    |")
    print("=======\n\n")
  elif (wrong == 3):
    print("\n+---+")
    print(" O  |")
    print("/|  |")
    print("    |")
    print("    |")
    print("=======\n\n")
  elif (wrong == 4):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("    |")
    print("    |")
    print("=======\n\n")
  elif (wrong == 5):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("/   |")
    print("    |")
    print("=======\n\n")
  elif (wrong == 6):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("/ \ |")
    print("    |")
    print("=======\n\n")


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
  print("\r")
  for letter in letters_already_guessed:
    print(letter, end=" ")
  # Prompt user for input
  letterGuessed = input("\nPlease guess a letter: ")
  print("\r")
  time.sleep(0.5)
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
           
# print("Game over! Thanks for playing :)")


continue_playing = input("\nWould you like to play again? (y/n) ")
if (continue_playing == 'y'):
    randomWord = random.choice(word_list)
elif (continue_playing == 'n'):
    print("\nThanks for playing :)")
while continue_playing != 'y' and 'n':
    print()