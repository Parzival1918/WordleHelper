# WordleHelper

![](docs/wordle-helper-vid.gif)

Input the correct letters and misplaced ones and program spits all words that comply with that.

Word list taken from https://github.com/tabatkins/wordle-list.

## Installation

* `pipx install wordle-helper-uc`. You must install `pipx` first if you don't have it already.
* Run with `wordle-helper` in your terminal.

### Dependencies

* argparse
* json
* os

## wordle-helper.py Args

### *-h, --help* 

Show help message and exit

### *-i INPUT, --input INPUT*

**Required argument**

Input the words that you have tried in Wordle with the format:

* CAPITAL letter for correct letters in correct positions
* lowercase letter for a correct letter but incorrect position
* "_" for positions with the wrong letter

Example input: -i pLE__ _LEE_P

* "p" is a correct letter but in the wrong position
* "L" and "E" are both correct and in their correct positions

### *-w WRONG, --wrong WRONG*

Input the letters to exclude from the results.

Example input: -w abc

### *-j, --json-output*

Output the result in json format

### *-s, -sorted*

Sort the possible words by their usage in the english language. Information taken from https://www.kaggle.com/datasets/rtatman/english-word-frequency

## To-Do

* Add -v, --version.
* Add -n, --next to propose a word to try next.
* When there is only one matching word, show its definition from https://www.datamuse.com/api/.