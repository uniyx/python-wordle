import sys
#cum
def main():
    with open('american-english.txt', 'r') as dictionary, open('five.txt', 'w') as five:
        for line in dictionary:
            if len(line) == 6 and line.strip().isalpha() and line[0].islower() and "'" not in line:
                print(line.strip())
                five.writelines(line)

if __name__ == '__main__':
    sys.exit(main())