"""
Hangman - A Word Guessing Game
================================
A command-line word-guessing game demonstrating core Python concepts:
functions, classes, loops, conditionals, string manipulation, file I/O,
exception handling, and the `random` module.

Author: (your name here)
"""

import random
import json
import os
import sys

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

WORDS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "words.json")
SCORES_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scores.json")
MAX_ATTEMPTS = 6

HANGMAN_STAGES = [
    r"""
       ------
       |    |
       |
       |
       |
       |
    ---------
    """,
    r"""
       ------
       |    |
       |    O
       |
       |
       |
    ---------
    """,
    r"""
       ------
       |    |
       |    O
       |    |
       |
       |
    ---------
    """,
    r"""
       ------
       |    |
       |    O
       |   /|
       |
       |
    ---------
    """,
    r"""
       ------
       |    |
       |    O
       |   /|\
       |
       |
    ---------
    """,
    r"""
       ------
       |    |
       |    O
       |   /|\
       |   /
       |
    ---------
    """,
    r"""
       ------
       |    |
       |    O
       |   /|\
       |   / \
       |
    ---------
    """,
]


# ---------------------------------------------------------------------------
# Word Bank
# ---------------------------------------------------------------------------

class WordBank:
    """Loads and serves category-based words with difficulty-based hints."""

    DEFAULT_WORDS = {
        "easy": {
            "python": "A popular programming language",
            "coding": "The act of writing computer programs",
            "laptop": "A portable computer",
            "coffee": "A popular caffeinated drink",
            "guitar": "A stringed musical instrument",
        },
        "medium": {
            "function": "A reusable block of code",
            "variable": "A named container for data",
            "algorithm": "A step-by-step problem-solving procedure",
            "database": "An organized collection of data",
            "keyboard": "An input device with keys",
        },
        "hard": {
            "recursion": "A function calling itself",
            "encapsulation": "Bundling data with methods in OOP",
            "polymorphism": "Many forms, an OOP concept",
            "inheritance": "A class deriving from another class",
            "asynchronous": "Not occurring at the same time",
        },
    }

    def __init__(self, path=WORDS_FILE):
        self.path = path
        self.words = self._load_words()

    def _load_words(self):
        """Load words from a JSON file, creating it with defaults if missing."""
        if not os.path.exists(self.path):
            self._save_default_words()
            return self.DEFAULT_WORDS
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            print("Warning: could not read words.json, using built-in word list.")
            return self.DEFAULT_WORDS

    def _save_default_words(self):
        try:
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump(self.DEFAULT_WORDS, f, indent=2)
        except OSError:
            pass

    def get_word(self, difficulty):
        """Return a random (word, hint) tuple for the given difficulty."""
        pool = self.words.get(difficulty, self.DEFAULT_WORDS["medium"])
        word = random.choice(list(pool.keys()))
        return word.lower(), pool[word]


# ---------------------------------------------------------------------------
# Scoreboard
# ---------------------------------------------------------------------------

class Scoreboard:
    """Tracks wins, losses, and streaks across sessions using a JSON file."""

    def __init__(self, path=SCORES_FILE):
        self.path = path
        self.data = self._load()

    def _load(self):
        if os.path.exists(self.path):
            try:
                with open(self.path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, OSError):
                pass
        return {"wins": 0, "losses": 0, "games_played": 0, "current_streak": 0, "best_streak": 0}

    def save(self):
        try:
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=2)
        except OSError:
            print("Warning: could not save scoreboard.")

    def record_win(self):
        self.data["wins"] += 1
        self.data["games_played"] += 1
        self.data["current_streak"] += 1
        self.data["best_streak"] = max(self.data["best_streak"], self.data["current_streak"])
        self.save()

    def record_loss(self):
        self.data["losses"] += 1
        self.data["games_played"] += 1
        self.data["current_streak"] = 0
        self.save()

    def summary(self):
        d = self.data
        return (
            f"Games played: {d['games_played']} | "
            f"Wins: {d['wins']} | Losses: {d['losses']} | "
            f"Current streak: {d['current_streak']} | Best streak: {d['best_streak']}"
        )


# ---------------------------------------------------------------------------
# Core Game Logic
# ---------------------------------------------------------------------------

class HangmanGame:
    """Encapsulates a single round of Hangman."""

    def __init__(self, word, hint):
        self.word = word
        self.hint = hint
        self.guessed_letters = set()
        self.wrong_attempts = 0

    @property
    def display_word(self):
        return " ".join(letter if letter in self.guessed_letters else "_" for letter in self.word)

    @property
    def is_won(self):
        return all(letter in self.guessed_letters for letter in self.word)

    @property
    def is_lost(self):
        return self.wrong_attempts >= MAX_ATTEMPTS

    def guess(self, letter):
        """Process one guessed letter. Returns True if it was a correct guess."""
        letter = letter.lower()
        if letter in self.guessed_letters:
            return None  # Already guessed
        self.guessed_letters.add(letter)
        if letter in self.word:
            return True
        self.wrong_attempts += 1
        return False

    def render(self):
        print(HANGMAN_STAGES[self.wrong_attempts])
        print("Word: ", self.display_word)
        print(f"Wrong attempts: {self.wrong_attempts}/{MAX_ATTEMPTS}")
        wrong_letters = sorted(l for l in self.guessed_letters if l not in self.word)
        if wrong_letters:
            print("Incorrect guesses:", ", ".join(wrong_letters))
        print()


# ---------------------------------------------------------------------------
# CLI / Input Helpers
# ---------------------------------------------------------------------------

def get_valid_letter(prompt="Guess a letter: "):
    """Keep prompting until the user enters a single alphabetic character."""
    while True:
        guess = input(prompt).strip().lower()
        if len(guess) != 1:
            print("Please enter exactly one letter.")
            continue
        if not guess.isalpha():
            print("Please enter a letter (a-z).")
            continue
        return guess


def choose_difficulty():
    options = {"1": "easy", "2": "medium", "3": "hard"}
    print("\nSelect difficulty:")
    print("  1) Easy")
    print("  2) Medium")
    print("  3) Hard")
    while True:
        choice = input("Enter choice (1-3): ").strip()
        if choice in options:
            return options[choice]
        print("Invalid choice, try again.")


def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer 'y' or 'n'.")


# ---------------------------------------------------------------------------
# Main Game Loop
# ---------------------------------------------------------------------------

def play_round(word_bank, scoreboard):
    difficulty = choose_difficulty()
    word, hint = word_bank.get_word(difficulty)
    game = HangmanGame(word, hint)

    print(f"\nHint: {hint}")
    print(f"The word has {len(word)} letters.\n")

    while not game.is_won and not game.is_lost:
        game.render()
        letter = get_valid_letter()
        result = game.guess(letter)
        if result is None:
            print(f"You already guessed '{letter}'.\n")
        elif result:
            print(f"'{letter}' is in the word!\n")
        else:
            print(f"'{letter}' is not in the word.\n")

    game.render()
    if game.is_won:
        print(f"You won! The word was '{game.word}'.")
        scoreboard.record_win()
    else:
        print(f"You lost! The word was '{game.word}'.")
        scoreboard.record_loss()

    print(scoreboard.summary())


def main():
    print("=" * 50)
    print("        WELCOME TO HANGMAN - WORD GUESSING GAME")
    print("=" * 50)

    word_bank = WordBank()
    scoreboard = Scoreboard()

    try:
        while True:
            play_round(word_bank, scoreboard)
            if not ask_yes_no("\nPlay again? (y/n): "):
                print("\nThanks for playing! Final stats:")
                print(scoreboard.summary())
                break
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()
