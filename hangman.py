"""A simple terminal-based Hangman game."""

import random


WORDS = (
    "apple",
    "banana",
    "cherry",
    "grape",
    "lemon",
    "orange",
    "peach",
    "pineapple",
    "strawberry",
    "watermelon",
    "notebook",
    "rainbow",
    "sunflower",
    "treasure",
)

HANGMAN_STATES = (
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
)

MAX_WRONG_GUESSES = len(HANGMAN_STATES) - 1


def choose_word(words=WORDS):
    """Return a random word from the supplied collection."""
    return random.choice(words)


def display_word(word, guessed_letters):
    """Return the word with unknown letters represented by underscores."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def has_won(word, guessed_letters):
    """Return whether every letter in the word has been guessed."""
    return all(letter in guessed_letters for letter in word)


def get_letter(guessed_letters):
    """Ask until the player enters one letter that has not been guessed."""
    while True:
        try:
            guess = input("Guess a letter: ").strip().lower()
        except EOFError:
            print("\nInput ended. Thanks for playing!")
            raise SystemExit
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            return guess


def show_round(word, guessed_letters, wrong_guesses):
    """Print the current state of a round."""
    print(f"\nWord: {display_word(word, guessed_letters)}")
    letters = ", ".join(sorted(guessed_letters)) or "none"
    print(f"Guessed letters: {letters}")
    print(f"Wrong guesses: {wrong_guesses}/{MAX_WRONG_GUESSES}")
    print(HANGMAN_STATES[wrong_guesses])


def play_round(word=None):
    """Run one round and return True if the player wins."""
    word = (word or choose_word()).lower()
    guessed_letters = set()
    wrong_guesses = 0

    print("\nNew round!")
    while wrong_guesses < MAX_WRONG_GUESSES:
        show_round(word, guessed_letters, wrong_guesses)
        guess = get_letter(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print("Good guess! That letter is in the word.")
            if has_won(word, guessed_letters):
                show_round(word, guessed_letters, wrong_guesses)
                print(f"You won! The word was {word}.")
                return True
        else:
            wrong_guesses += 1
            print("Sorry, that letter is not in the word.")

    show_round(word, guessed_letters, wrong_guesses)
    print(f"Game over! The word was {word}.")
    return False


def play_again():
    """Return whether the player wants to start another round."""
    while True:
        choice = input("Play again? (y/n): ").strip().lower()
        if choice in {"y", "yes"}:
            return True
        if choice in {"n", "no"}:
            return False
        print("Please enter y or n.")


def main():
    """Start the game and manage replaying rounds."""
    print("\n    HANGMAN GAME\n")
    while True:
        play_round()
        if not play_again():
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
