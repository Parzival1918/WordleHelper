#User input the word he tried in wordle. 
# - Capital letters indicate letter in correct position
# - Lowercase letters indicate letter in wrong position
# - Underscore indicates empty position

# Output:
# - List of words that match the user input

# Example:
# User input: _a__E
# Output: ['apple', 'angle', 'alive', 'alone', 'agile', 'ample', 'amaze', 'amuse', 'awake', 'aware', 'abate', 'abide', 'abuse']

#Class that stores a letter and position and whether it is correct or not
class Letter:
    def __init__(self, letter: str, position: int, correct: bool):
        self.letter = letter
        self.position = position
        self.correct = correct

    def __repr__(self): #Printable representation of the object
        return f"{self.letter} - {self.position} - {self.correct}"
    
#Function to print possible words
def printPossibleWords(possibleWords: list):
    if len(possibleWords) == 0:
        print("No words found with this combination")
        return

    for word in possibleWords:
        print(word)


#Ask for user input
user_input = input("Enter the word you tried in wordle: ")

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
possibleWords = []
with open("Words/words.txt", "r") as wordlist:
    for line in wordlist:
        word = line.strip()
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
