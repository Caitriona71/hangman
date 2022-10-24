## Hangman

Hangman is an old-fashioned word guessing game. It is traditionally played with pencil and paper. This version is played on a Python terminal.

This is the live site: ***[       ](https://caitriona71-             .gitpod.io)***

## How to play Hangman

* The game appears and the user is invited to play and asked to guess a letter.
* A secret word is displayed with dashes - the number of dashes represents how many letters are in the word.  
* On the display under the dashes for the secret word, there is a message listing all the letters the player has already guessed.
* Every time the user guesses a letter, it is added to this list.
* If the user guesses a wrong letter, the gallows image is displayed and an attachment is added to the hanging man. 
* If the user guesses a letter in the secret word, it will be displayed on the dash where it appears in the word.  
* The user has 6 attempts to guess the word.  
* The game ends when the 6 attempts are used up or if the user guesses the correct word before all attempts have been used.
* A message is displayed informing the user that the game is over and inviting them to play again.

## Features

* At the top of the terminal an amusing colorful play on words introduces the game of hangman. (Display the image here)

* ASCII font has been used to display Hangman as a banner. (Display the image here)

* The game begins with an invitation to the user to play the game. Blank dashes display the secret word to be guessed and underneath the dashes a message is displayed to the user listing all the letters they have guessed. (Display image here)

* If an incorrect letter is chosen the gallows image appears and an attachment is displayed for each incorrect guess. (Display image here)

* If a correct letter is guessed it is displayed on the dash where it appears in the word. (Display image here.)

* When all attempts are used up the user is asked if they would like to play again. (Display image here)

## Testing

* As Pep8 is down, we were advised to go through the problems that appear in the terminal to validate our code.  There were problems appearing in red - mainly indentation errors or if a line was too long.  These were corrected as they came up.  
* There were warnings also - yellow ones referred to the slash used on the hangman image.  It was suggested these might be missing an 'r' prefix.  I ignored these as I knew they weren't related to that. Blue errors were pylint errors and having checked on slack, the advice was that these were not concerning.

* Each stage of the game was tested.  If the user enters a letter for example, the letter appends to the right list. If the letter the user guesses is wrong, the hangman appears with another attachment.

## Deployment

* The game was deployed to Heroku.
* A new app was created.
* Under the settings tab the app was named and "Reveal Config Vars" was selected and given the key of `PORT`, and the value was set at `8000`.  
* "Add buildpack" was selected to add python and node js in that order.
* Under the Deploy tab, "Deployment Method" was selected then "GitHub" was clicked and "Connect to GitHub". 
* The relevant repository was selected by clicking "Connect".
* "Enable Automatic Deploys" was selected next so that Heroku would rebuild the app any time changes were pushed to GitHub.

## Credits

* Youtube tutorial - Sean Halverson - [https://www.youtube.com/watch?v=pFvSb7cb_Us&t=71s]
* [devhints.io/figlet] for ascii font at top of game.
* [codespeedy.com] for instructions on how to install pyfiglet as a library in Python and how to download a font.
* [ozzmaker.com/add-colour-to-text-in-python] for adding color to the text.
* [inventwithpython.com/chapter8.html] for hangman images.
* [online-python.com] IDE to check if code was working.
* [gitpod] Gitpod was used to code the project.
* [Heroku] for deploying the project.

## Acknowledgements

* Tutor support at Code Institute
   
