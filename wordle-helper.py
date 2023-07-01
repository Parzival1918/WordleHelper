#!/opt/homebrew/bin/python3
#CHANGE FIRST LINE TO YOUR PYTHON PATH

#User input the word he tried in wordle. 
# - Capital letters indicate letter in correct position
# - Lowercase letters indicate letter in wrong position
# - Underscore indicates empty position

# Output:
# - List of words that match the user input

# Example:
# User input: _a__E
# Output: ['apple', 'angle', 'alive', 'alone', 'agile', 'ample', 'amaze', 'amuse', 'awake', 'aware', 'abate', 'abide', 'abuse']

#Imports
import argparse as ap

#Class that stores a letter and position and whether it is correct or not
class Letter:
    def __init__(self, letter: str, position: int, correct: bool):
        self.letter = letter
        self.position = position
        self.correct = correct

    def __repr__(self): #Printable representation of the object
        return f"{self.letter} - {self.position} - {self.correct}"
    
#Text colour class
class TextColour:
   PURPLE = '\033[1;35;48m'
   CYAN = '\033[1;36;48m'
   BOLD = '\033[1;37;48m'
   BLUE = '\033[1;34;48m'
   GREEN = '\033[1;32;48m'
   YELLOW = '\033[1;33;48m'
   RED = '\033[1;31;48m'
   BLACK = '\033[1;30;48m'
   UNDERLINE = '\033[4;37;48m'
   END = '\033[1;37;0m'
    
#Function to print possible words
def printPossibleWords(possibleWords: list):
    if len(possibleWords) == 0:
        print(TextColour.RED + "No words found with this combination" + TextColour.END)
        return

    for word in possibleWords:
        print(word)

parser = ap.ArgumentParser()

#Parser arguments
parser.add_argument("word", help="Word you tried in wordle", type=str)
parser.add_argument("-w", "--wrong", help="All wrong letters", type=str)

args = parser.parse_args()

#Ask for user input
#user_input = input("Enter the word you tried in wordle: ")
user_input = args.word
wrong_letters = args.wrong

#Parse the user input
correctLetters = []
missplacedLetters = []
emptySpaces = []
for i in range(len(user_input)):
    if user_input[i].isupper():
        correctLetters.append(Letter(user_input[i].lower(), i, True))
    elif user_input[i].islower():
        missplacedLetters.append(Letter(user_input[i], i, False))
    elif user_input[i] == "_":
        emptySpaces.append(Letter(None, i, False))

#Read the wordlist file and compare each word to the user input
with open("Words/words.txt", "r") as wordlist:
    #Eliminate words with letters in the wrong_letters string
    searchWords = []
    for line in wordlist:
        word = line.strip()
        if wrong_letters != None:
            for letter in wrong_letters.lower():
                if letter in word:
                    break
            else:
                searchWords.append(word)
        else:
            searchWords.append(word)

possibleWords = []
for word in searchWords:
    #word = line.strip()
    #Check correct letters
    correctCount = 0
    for pos,letter in enumerate(word):
        for correctLetter in correctLetters:
            if correctLetter.position == pos and correctLetter.letter == letter:
                correctCount += 1
                break
    
    if correctCount != len(correctLetters):
        #print("Correct letters don't match")
        continue

    #Check missplaced letters
    #BUG This doesn't work if there are multiple of the same letter in the word
    missplacedCount = 0
    for missplacedLetter in missplacedLetters:
        for pos,letter in enumerate(word):
            if missplacedLetter.letter == letter and missplacedLetter.position != pos:
                missplacedCount += 1
                break

    if missplacedCount != len(missplacedLetters):
        #print("Missplaced letters don't match")
        continue

    possibleWords.append(word)

printPossibleWords(possibleWords)
