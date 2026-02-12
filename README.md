#  Hangman Game (Python)

A simple **command-line Hangman game** written in Python.  
The game uses a predefined word list, allows the user to add a new word, and randomly selects a word for gameplay. The player has **6 chances** before the full stickman is drawn and the game ends.


##  Features

- Predefined word list included in the program  
- Option for the user to add a new word to the list  
- Random word selection using Python’s `random` module  
- Letter guessing system  
- Word guessing after a correct letter guess  
- Progressive Hangman stickman drawing  
- Game ends after:
  - Guessing the word correctly
  - Guessing the word incorrectly
  - Exhausting all 6 chances  
- Displays the word list repeatedly during the game  


## Game Logic Overview

1. The user enters their name.
2. A predefined word list is displayed.
3. The user may optionally add a new word.
4. The program randomly selects a word from the list.
5. The user guesses a letter:
   -  **If the letter is in the word**:
     - The user is prompted to guess the full word.
     - Correct guess → **Win**
     - Wrong guess → **Game Over**
   -  **If the letter is not in the word**:
     - A part of the hangman is drawn (`o`, `|`, `/`, `\`)
     - The user gets another chance
6. After 6 wrong guesses, the full stickman is displayed and the game ends.

**Note:**  
Even if the player finds a correct letter but fails to guess the full word correctly, the game ends.

