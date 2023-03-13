import random
import time

from words import word_list

hangman = '''  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/                       '''


print("\033[1;34;40mI know you're \033[1;31;40mdying")
print("\033[1;34;40mto play this game.")
print("\033[1;34;40mSo get in the \033[1;32;40mswing")
print("\033[1;34;40mand \033[1;31;40mgibbet \033[1;34;40ma try!")
print("Can you guess the mystery word?")
print("\033[1;34;40mOr are you in for bad \033[1;32;40mnoose!")
print("\033[1;34;40mDon't \033[1;31;40mhang \033[1;34;40maround.")
print("\033[1;34;40mThe \033[1;32;40mneck's \033[1;34;40mgame awaits you!")
print("\033[1;34;40mSorry you got \033[1;31;40mroped \033[1;34;40minto this?!")
print("\r")
print(hangman)

print("\033[1;33;40mRULES:\033[1;32;40m")
print("1. Try to guess the mystery word by guessing the missing letters.")
print("2. The blank lines displayed represent the mystery word.")
print("3. You have 6 lives.")
print("4. The hangman image shows how many lives you have remaining.")
print("5. If you guess a wrong letter you lose a life.")
print("6. The hangman image adds another body part.")
print("7. If you guess a correct letter it will be added to the mystery word.")
print("8. The game is over after you've used up all your lives.")
print("9. Or you guess the mystery word.")
print("\r")

print("\r")
print("\033[1;33;40mLet's play!\033[1;32;40m")
print("\r")


        #"""
        #Try to guess the mystery word by guessing the missing letters.
        #The blank lines displayed represent the mystery word.
        #You have 6 lives.
        #The hangman image shows how many lives you have remaining.
        #If you guess a wrong letter you lose a life.
        #The hangman image adds another body part.
        #If you guess a correct letter it will be added to the mystery word.
        #The game is over after you've used up all your lives.
        #Or you guess the mystery word.
        #"""
    


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

# This prints the letters the user guessed so far
while (attempts_wrong != 6 and letters_correct != length_guess_word):
    print("\nLetters already guessed:")
    # print("\r")
    for letter in letters_already_guessed:
        print(letter, end=" ")
        # print("\r")

    # Prompt user for input
    # is_valid = False
    # while (is_valid == False):
    print("\r")
    letterGuessed = input("\nPlease guess a letter:\n")
       # if (len(letterGuessed) == 1):
           # is_valid == True
    print("\r")
    time.sleep(0.5)

    if letterGuessed in splitWord:
        splitWord = list(filter(lambda x: x != letterGuessed, splitWord))
        guess_index += 1
        letters_already_guessed.append(letterGuessed)
        letters_correct = printWord(letters_already_guessed)
        printLines()
        print("\n\033[1;34;40mGood work, you guessed right!\033[1;32;40m")
    else:
        attempts_wrong += 1
        letters_already_guessed.append(letterGuessed)
        # Update the drawing
        print_hangman(attempts_wrong)
        # Print word
        letters_correct = printWord(letters_already_guessed)
        printLines()
        print("\n\033[1;31;40mThat letter isn't in the word!\033[1;32;40m")

cont_playing = input("\n\033[1;33;40mGame over! To play again click run program\n")
