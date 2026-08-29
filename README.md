# Hangman Game

A simple terminal-based Hangman game written in Python. The computer chooses a word, and you guess it one letter at a time before the Hangman drawing is complete.

## Features

- Randomly selects a word from an offline word list
- Reveals every occurrence of correctly guessed letters
- Tracks guessed letters and incorrect guesses
- Shows a Hangman drawing for each mistake
- Validates empty, repeated, numeric, punctuation, and multi-character input
- Supports uppercase and lowercase letter guesses
- Reveals the answer after a loss
- Allows multiple rounds without restarting the program

## How to Run

Make sure Python 3 is installed, then run:

```bash
python hangman.py
```

On some systems, use `python3 hangman.py` instead.

## How to Play

1. Start the program.
2. Enter one letter when prompted.
3. Correct guesses reveal letters in the word.
4. Wrong guesses add a part to the Hangman drawing.
5. Guess the complete word before six wrong guesses.
6. Choose `y` to play another round or `n` to quit.

## Example

```text
Word: _ _ _ _ _ _
Guessed letters: a, e
Wrong guesses: 2/6

Guess a letter: r
Good guess! That letter is in the word.
```

The exact word and drawing depend on the random round.

## Concepts Practiced

This project practices variables, strings, lists and tuples, sets, loops, conditionals, functions, random selection, input validation, and basic exception-free error handling.
