![wordle.py logo]()
# wordle.py

Wordle but in python!

Inspired by the [original](https://www.powerlanguage.co.uk/wordle/).

## Rules

The player has 6 turns to guess a five letter word.   The game gives hints by highlighting letters.  Green letters appear when the letter placed in the correct spot.  Yellow letters appear when the word contains them.  Grey letters are duds.

## Words

I generated a list of five letter words via `5letters.py`, which I wrote sloppily.  It takes in a text file of the english dictionary and filters out words based on the following conditions.  

* 5 letters long
* English letters only
* No apostrophes
* No proper nouns

`five.txt` is then generated for us to use!

## Game

`gen()` Simply generates and returns our mystery word from `five.txt`.  Afterwards, the main `game(word)` function takes the mystery word as a parameter and starts the game.  We make sure that each user's guess is a valid word before inserting it into our guesses list.  The `print_guesses(guesses, word)` function utilizes [Colorama](https://pypi.org/project/colorama/) to display the letter hints in the terminal.  Unlike the original Wordle game, you can play the python version more than once a day!

Example usage:
`python3 wordle.py`
