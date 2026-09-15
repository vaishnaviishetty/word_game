# Hangman — Word Guessing Game (CLI)

A command-line word-guessing game built in pure Python (no external
dependencies). Guess the hidden word one letter at a time before the
hangman drawing is complete!

## Features

- **Three difficulty levels** (easy / medium / hard), each with its own word pool and hints
- **ASCII-art hangman** that progresses with each wrong guess
- **Hints** shown at the start of each round
- **Persistent scoreboard** (wins, losses, streaks) saved to `scores.json`
- **Custom word bank** — edit `words.json` to add your own words/categories
- **Input validation** and graceful handling of repeated guesses / interrupts (Ctrl+C)
- **Replay loop** — play as many rounds as you like in one session

## Requirements

- Python 3.7+
- No third-party packages required (standard library only)

## Getting Started

```bash
# Clone the repository
git clone https://github.com/<your-username>/word-guessing-game.git
cd word-guessing-game

# Run the game
python3 hangman.py
```

## How to Play

1. Choose a difficulty level (Easy, Medium, or Hard).
2. You'll see a hint and the number of letters in the word.
3. Guess one letter at a time.
4. Each incorrect guess adds a piece to the hangman drawing.
5. Guess all letters correctly before 6 wrong guesses to win!
6. Choose to play again — your stats persist across sessions.

## Project Structure

```
word-guessing-game/
├── hangman.py      # Main game (classes, game loop, CLI helpers)
├── words.json       # Word bank by difficulty (auto-created if missing)
├── scores.json       # Persistent scoreboard (auto-created; gitignored)
├── README.md
├── LICENSE
└── .gitignore
```

## Customizing the Word Bank

Edit `words.json` to add your own words and hints:

```json
{
  "easy": {
    "apple": "A common fruit"
  },
  "medium": { ... },
  "hard": { ... }
}
```

## Python Concepts Demonstrated

- Object-oriented design (classes: `WordBank`, `Scoreboard`, `HangmanGame`)
- File I/O and JSON serialization
- Exception handling (`try`/`except`, `KeyboardInterrupt`)
- Properties and encapsulation
- The `random` module
- String formatting and set operations
- Input validation loops

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
