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
import os
import json

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
    if output_json:
        addToInput = ""
        if wrong_letters != None:
            addToInput = " -w " + wrong_letters.lower()

        jsonOutput = {
            "possible-words": possibleWords,
            "input": {
                "user-input": user_input + addToInput,
                "correct-letters": [{"char": letter.letter, "pos": letter.position} for letter in correctLetters],
                "misplaced-letters": [{"char": letter.letter, "pos": letter.position} for letter in misplacedLetters],
                "excluded-letters": wrong_letters
            }
        }
        print(json.dumps(jsonOutput, indent=4))
    else:
        if len(possibleWords) == 0:
            print(TextColour.RED + "No words found with this combination" + TextColour.END)
            return
        
        termColumns = os.get_terminal_size().columns - 1
        WORD_SIZE = 8

        wordChunksperColumn = termColumns // WORD_SIZE
        #print(wordChunksperColumn)

        print("Possible words: ")
        wordCount = 1
        for word in possibleWords:
            if (wordCount) % wordChunksperColumn == 0:
                print(TextColour.PURPLE + " > " + TextColour.END + word.rstrip())
            else:
                print(TextColour.PURPLE + " > " + TextColour.END + word.rstrip(), end="")
            wordCount += 1

        if (wordCount) % wordChunksperColumn != 0:
            print() #For new line

parser = ap.ArgumentParser()

#Parser arguments
parser.add_argument("-i", "--input", help="Word you tried in wordle", type=str)
parser.add_argument("-w", "--wrong", help="All wrong letters", type=str)
parser.add_argument("-j", "--json-output", help="Output the results in json format", action="store_true")

args = parser.parse_args()

#Ask for user input
#user_input = input("Enter the word you tried in wordle: ")
user_input = args.input
wrong_letters = args.wrong
output_json = args.json_output

if len(user_input) != 5:
    if not output_json:
        print(TextColour.RED + "Input must be 5 characters long" + TextColour.END)
    exit(1)

buildString = ""
for letter in user_input:
    if letter.islower():
        buildString += TextColour.YELLOW + letter.upper() + TextColour.END
    elif letter.isupper():
        buildString += TextColour.GREEN + letter + TextColour.END
    elif letter == "_":
        buildString += TextColour.BLACK + TextColour.UNDERLINE + letter + TextColour.END
    else:
        if not output_json:
            print(TextColour.RED + "Invalid character in input: " + TextColour.CYAN + letter + TextColour.END)
        exit(2)

if not output_json:
    print("Input: " + buildString) #For new line

if wrong_letters != None:
    if not output_json:
        #print("Letters NOT in word: " + TextColour.RED + wrong_letters.upper().split(",") + TextColour.END)
        print("Letters NOT in word: ", end="")
        for letter in wrong_letters.upper():
            print(TextColour.RED + letter + " " + TextColour.END, end="")

        print() #For new line

#Parse the user input
correctLetters = []
misplacedLetters = []
emptySpaces = []
for i in range(len(user_input)):
    if user_input[i].isupper():
        correctLetters.append(Letter(user_input[i].lower(), i, True))
    elif user_input[i].islower():
        misplacedLetters.append(Letter(user_input[i], i, False))
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

    #Check misplaced letters
    #BUG This doesn't work if there are multiple of the same letter in the word
    misplacedCount = 0
    for misplacedLetter in misplacedLetters:
        for pos,letter in enumerate(word):
            if misplacedLetter.letter == letter and misplacedLetter.position != pos:
                misplacedCount += 1
                break

    if misplacedCount != len(misplacedLetters):
        #print("misplaced letters don't match")
        continue

    possibleWords.append(word)

printPossibleWords(possibleWords)
