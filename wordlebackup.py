# Wordle python by uni
import sys
import random

def main():
    print("Welcome to Wordle!\n")

    word = gen()
    game(word)

def game(word):
    for i in range(6):
        print("_ _ _ _ _")

    guess = guess()

def guess():
    guess = input("\nEnter your guess:\n")

    # Check if guess is valid
    if valid(guess):
        print("Valid")
        return guess
    else:
        print("Not a valid word")

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