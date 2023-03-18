# **Hangman**

Hangman is a popular word guessing game. It is traditionally played with pencil and paper. This version is played on a Python terminal.

This is the live site: **[https://hangmancb.herokuapp.com/]** <br><br>

## **How to play Hangman**

**1.** The game appears and the user is invited to play and asked to guess a letter.<br>
**2.** A mystery word is displayed with dashes - the number of dashes represents how many letters are in the word.<br> 
**3.** On the display under the dashes for the mystery word, there is a message listing all the letters the player has already guessed.<br>
**4.**  Every time the user guesses a correct letter, it is added to this list and it will be displayed on the dash where it appears in the word.<br>
**5.** If the user guesses a wrong letter, they get feedback informing them the letter isn't in the word and another body part is added to the hanging man in the gallows image.<br> 
**6.** The hangman image is only displayed when the user chooses a wrong letter.<br> 
**7.** The user has 6 attempts to guess the word.<br> 
**8.** The game ends when the 6 attempts are used up or if the user guesses the correct word before all attempts have been used.<br>
**9.** A message is displayed informing the user that the game is over and inviting them to play again.<br><br>

## **Features**

*  At the top of the terminal an amusing colorful play on words introduces the game of hangman.<br><br>
![Colored word play text](/screenshots/hangman_play_on_words.png)

* ASCII font has been used to display Hangman as a banner.<br><br>
![Ascii Banner](/screenshots/hangman_ascii.png)<br><br>

* The rules are displayed underneath the hangman banner.<br><br>
![Rules](/screenshots/hangman_rules.png)

* The game begins with an invitation to the user to play the game. Blank dashes display the secret word to be guessed.<br><br>
![Invitation to play](/screenshots/let's-play-hangman.png) 

* Underneath the dashes a message is displayed to the user listing all the letters they have guessed.<br><br>
![Letters already guessed](/screenshots/letters_already_guessed.png)

* If an incorrect letter is chosen the user gets feedback informing them that that letter isn't in the word and the gallows image shows another body part added to the hanging man for each incorrect guess.<br><br>
![Hangman image](/screenshots/incorrect_letter.png)

* If a correct letter is guessed it is displayed on the dash where it appears in the word and a message is shown informing the user that they guessed right.<br><br>
![Correct letter](/screenshots/letter_guessed_right.png)

* If a letter is guessed twice in error the user gets a feedback message telling them that they have already guessed that letter.<br><br>
![Same letter guessed twice](/screenshots/same_letter_guessed_twice.png)

* When all attempts are used up the game is over and the user is asked if they would like to play again.<br><br>
![Game over](/screenshots/hangman_game_over.png)<br><br>


## **Technologies Used**

* Python was the coding language used for the project.
* Gitpod was used to code, commit and push the project.
* Heroku was used to deploy the project.
* GitHub was used to store the project after pushing.<br><br>


## **Testing**

* Pep8CI was used to validate the code.  There were problems appearing in red - mainly indentation errors or if a line was too long.  These were corrected as they came up.

* There were warnings also - "invalid escape sequence '\' referred to the slash used on the hangman image.  I ignored these. Other warnings were referring to trailing white space on a few lines of code in the Hangman ascii banner. These were unavoidable<br><br>
![Pep8CI](screenshots/pep8CI_test.png)<br>

* Each stage of the game was tested.  If the user enters a letter for example, the letter appends to the right list. If the letter the user guesses is wrong, the hangman appears with another attachment.<br><br>

## **Deployment**

* The game was deployed to Heroku.
* A new app was created.
* Under the settings tab the app was named and "Reveal Config Vars" was selected and given the key of `PORT`, and the value was set at `8000`.  
* "Add buildpack" was selected to add python and node js in that order.
* Under the Deploy tab, "Deployment Method" was selected then "GitHub" was clicked and "Connect to GitHub". 
* The relevant repository was selected by clicking "Connect".
* "Enable Automatic Deploys" was selected next so that Heroku would rebuild the app any time changes were pushed to GitHub.<br><br>

## **Credits**

* Youtube tutorial - Sean Halverson - [https://www.youtube.com/watch?v=pFvSb7cb_Us&t=71s]
* [TextKool.com](https://www.textkool.com) for ascii font at top of game.
* [colorama/add-colour-to-text-in-python](https://pypi.org/project/colorama/) for adding color to the text.
* [inventwithpython.com/chapter8.html](https://inventwithpython.com) for hangman images.
* [online-python.com](https://online-python.com) IDE to check if code was working.<br><br>

## **Acknowledgements**

* Tutor support at Code Institute.
* My course Facilitator.
* My mentor for his guidance and support.
   
