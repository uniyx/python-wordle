# Wordle python by uni
import sys
import random

from colorama import Fore, Back, Style, init

init(autoreset=True)

def main():
    print("Welcome to Wordle!\n")

    word = gen()
    game(word)

def game(word):
    guesses = [list("_____"), list("_____"), list("_____"), list("_____"), list("_____"), list("_____")]

    turn = 0

    print_guesses(guesses, word)

    while True:
        # Get next guess
        guess = input_guess()

        guesses[turn] = guess

        # Print out guesses
        print_guesses(guesses, word)

        # Win condition
        if guess == word:            
            print("\nYou win!")
            break

        turn += 1
        
        # Lose condition
        if turn == 6:
            print("\nYou lost!")
            print("The word was: " + word)
            break

def print_guesses(guesses, word):
    print("")
    for i in range(6):

        for j in range(5):
            # Check if letters are exact
            if(guesses[i][j] == word[j]):
                print(Back.GREEN + Fore.BLACK + guesses[i][j], end = " ")

            # Check if letters exist
            elif(guesses[i][j] in word):
                print(Back.YELLOW + Fore.BLACK + guesses[i][j], end = " ")

            else:
                print(guesses[i][j], end = " ")
        
        Style.RESET_ALL
        print("")

def input_guess():
    while True:
        guess = input("\nEnter your guess:\n")

        # Check if guess is valid
        if valid(guess):
            break
        else:
            print("Not valid")

    return guess

def valid(guess):
    if(len(guess) < 5):
        print("Too short of a word")

    if(len(guess) > 5):
        print("Too long of a word")

    # Check if in dictionary
    with open('five.txt', 'r') as words:
        for line in words:
            if guess == line.strip():
                return True

def gen():
    # Count lines from five.txt
    wordcount = 0

    with open('five.txt', 'r') as words:
        for line in words:
            wordcount += 1

        # Pick random word from five.txt
        linenum = random.randint(0, wordcount)

        print("Five.txt has " + str(wordcount) + " words")
        print("Random word is number " + str(linenum))

    # print generated word
    with open('five.txt', 'r') as words:
        lines = words.readlines()
        
        word = lines[linenum].strip()
        
        #print(word)
        return word
        
if __name__ == '__main__':
    sys.exit(main())