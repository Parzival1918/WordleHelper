# WordleHelper

Input the correct letters and misplaced ones and program spits all words that comply with that.

### wordle-helper.py Args

#### *-h, --help* 

Show help message and exit

#### *-i INPUT, --input INPUT*

**Required argument**

Input the word that you have tried in Wordle with the format:

* CAPITAL letter for correct letters in correct positions
* lowercase letter for a correct letter but incorrect position
* "_" for positions with the wrong letter

Example input: -i pLE__

* "p" is a correct letter but in the wrong position
* "L" and "E" are both correct and in their correct positions

#### *-w WRONG, --wrong WRONG*

Input the letters to exclude from the results.

Example input: -w abc

#### *-j, --json-output*

Output the result in json format

#### *-s, -sorted*

Sort the possible words by their usage in the english language. Information taken from https://www.kaggle.com/datasets/rtatman/english-word-frequency

Word list taken from https://github.com/tabatkins/wordle-list.
