import random
import time
from colorama import just_fix_windows_console
from colorama import Fore, Style

just_fix_windows_console()

from words import word_list

hangman = '''  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/                       '''

print(Style.BRIGHT + Fore.BLUE + "I know you're " + Style.BRIGHT + Fore.RED + "dying")
print(Style.BRIGHT + Fore.BLUE + "to play this game.")
print(Style.BRIGHT + Fore.BLUE + "So get in the " + Style.BRIGHT + Fore.GREEN + "swing")
print(Style.BRIGHT + Fore.BLUE + "and " + Style.BRIGHT + Fore.RED + "gibbet " + Style.BRIGHT + Fore.BLUE + "a try!")
print(Style.BRIGHT + Fore.BLUE + "Can you guess the mystery word?")
print(Style.BRIGHT + Fore.BLUE + "Or are you in for bad " + Style.BRIGHT + Fore.GREEN + "noose!")
print(Style.BRIGHT + Fore.BLUE + "Don't " + Style.BRIGHT + Fore.RED + "hang " + Style.BRIGHT + Fore.BLUE + "around.")
print(Style.BRIGHT + Fore.BLUE + "The " + Style.BRIGHT + Fore.GREEN + "neck's " + Style.BRIGHT + Fore.BLUE + "game awaits you!")
print(Style.BRIGHT + Fore.BLUE + "Sorry you got " + Style.BRIGHT + Fore.RED + "roped " + Style.BRIGHT + Fore.BLUE + "into this?!")
print("\r")
print(hangman)
print("\r")
print("\r")


print(Style.BRIGHT + Fore.YELLOW + "RULES:")
print(Style.BRIGHT + Fore.YELLOW + "1. " + Style.BRIGHT + Fore.BLUE + "Try to guess the mystery word by guessing the missing letters.")
print(Style.BRIGHT + Fore.YELLOW + "2. " + Style.BRIGHT + Fore.BLUE + "The blank lines displayed represent the mystery word.")
print(Style.BRIGHT + Fore.YELLOW + "3. " + Style.BRIGHT + Fore.BLUE + "You have 6 lives.")
print(Style.BRIGHT + Fore.YELLOW + "4. " + Style.BRIGHT + Fore.BLUE + "The hangman image shows how many lives you have remaining.")
print(Style.BRIGHT + Fore.YELLOW + "5. " + Style.BRIGHT + Fore.BLUE + "If you guess a wrong letter you lose a life.")
print(Style.BRIGHT + Fore.YELLOW + "6. " + Style.BRIGHT + Fore.BLUE + "The hangman image adds another body part.")
print(Style.BRIGHT + Fore.YELLOW + "7. " + Style.BRIGHT + Fore.BLUE + "If you guess a correct letter it will be added to the mystery word.")
print(Style.BRIGHT + Fore.YELLOW + "8. " + Style.BRIGHT + Fore.BLUE + "The game is over after you've used up all your lives.")
print(Style.BRIGHT + Fore.YELLOW + "9. " + Style.BRIGHT + Fore.BLUE + "Or you guess the mystery word.")
print("\r")

print("\r")
print(Style.BRIGHT + Fore.YELLOW + "Let's play")
print("\r")
# Choose a mystery word
randomWord = random.choice(word_list)

for x in randomWord:
    print("_", end=" ")


# This function prints the hangman image when the user guesses a wrong letter.
def print_hangman(wrong):
    if wrong == 0:
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("    |")
        print("=======\n\n")
    elif wrong == 1:
        print("\n+---+")
        print("O   |")
        print("    |")
        print("    |")
        print("    |")
        print("=======\n\n")
    elif wrong == 2:
        print("\n+---+")
        print("O   |")
        print("|   |")
        print("    |")
        print("    |")
        print("=======\n\n")
    elif wrong == 3:
        print("\n+---+")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("    |")
        print("=======\n\n")
    elif wrong == 4:
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("    |")
        print("    |")
        print("=======\n\n")
    elif wrong == 5:
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/   |")
        print("    |")
        print("=======\n\n")
    elif wrong == 6:
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/ \ |")
        print("    |")
        print("=======\n\n")


# This function prints the correct letter guessed in the random word
def printWord(guessedLetters):
    counter = 0
    correctLetters = 0
    for char in randomWord:
        if char in guessedLetters:
            print(randomWord[counter], end=" ")
            correctLetters += 1
        else:
            print(" ", end=" ")
        counter += 1
    return correctLetters


# This prints the dashes for the letters of the secret word
def printLines():
    print("\r")
    for char in randomWord:
        print("\u203E", end=" ")


splitWord = list(randomWord)
length_guess_word = len(randomWord)
attempts_wrong = 0
guess_index = 0
letters_already_guessed = []
letters_correct = 0

# # This prints the letters the user guessed so far
while (attempts_wrong != 6 and letters_correct != length_guess_word):
    print(Style.BRIGHT + Fore.GREEN + "\nLetters already guessed:")
    # print("\r")
    for letter in letters_already_guessed:
        print(letter, end=" ")
        # print("\r")

    print("\r")

    letterGuessed = None

    while True:
        letterGuessed = input(Style.BRIGHT + Fore.GREEN + "\nPlease guess a letter:\n")

        if not letterGuessed.isalpha() or len(letterGuessed) > 1:
            continue
        else:
            break
                
    print("\r")
    time.sleep(0.5)

    if letterGuessed not in letters_already_guessed:
        if letterGuessed in splitWord:
            splitWord = list(filter(lambda x: x != letterGuessed, splitWord))
            guess_index += 1
            letters_already_guessed.append(letterGuessed)
            letters_correct = printWord(letters_already_guessed)
            printLines()
            print(Style.BRIGHT + Fore.BLUE + "\nGood work, you guessed right!")
        else:
            attempts_wrong += 1
            letters_already_guessed.append(letterGuessed)
            # Update the drawing
            print_hangman(attempts_wrong)
            # Print word
            letters_correct = printWord(letters_already_guessed)
            printLines()
            print(Style.BRIGHT + Fore.RED + "\nThat letter isn't in the word!")
    else:
        print(Style.BRIGHT + Fore.WHITE + "You've already guessed that letter!")

cont_playing = input(Style.BRIGHT + Fore.YELLOW + "\nGame over! To play again click run program\n")
