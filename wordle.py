# Wordle python by uni
import sys
import random

def main():
    print("Welcome to Wordle!\n")

    word = gen()
    game(word)

def game(word):
    guesses = [list("_____"), list("_____"), list("_____"), list("_____"), list("_____"), list("_____")]

    turn = 0

    while True:
        # Print out guesses
        for i in range(6):
            print(" ".join(guesses[i]))

        # Get next guess
        guess = input_guess()
        difference = compare(word, guess)

        guesses[turn] = difference

        # Win condition
        if difference == list("22222"):
        
            # Print out guesses
            for i in range(6):
                print(" ".join(guesses[i]))
            
            print("\nYou win!")
            break

        turn += 1
        
        # Lose condition
        if turn == 6:

            # Print out guesses
            for i in range(6):
                print(" ".join(guesses[i]))

            print("\nYou lost!")
            print("The word was: " + word)
            break

def compare(word, guess):
    difference = list("_____")

    # Check if letters exist
    for i in range(5):
        if(guess[i] in word):
            #print("exist match")
            difference[i] = "1"

     # Check if letters are exact
    for i in range(5):
        if(word[i] == guess[i]):
            #print("exact match")
            difference[i] = "2"

    return difference

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
        
        print(word)
        return word
        

if __name__ == '__main__':
    sys.exit(main())