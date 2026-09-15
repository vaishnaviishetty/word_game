# Word Guessing Game

A simple, interactive console-based word-guessing game written in Python.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

## Overview

Word Guessing Game is a beginner-friendly Python project in which the player tries to uncover a randomly selected fruit by guessing individual characters. Each round selects one word from a fixed list and displays a hint. The player has four lives and loses one each time an incorrect character is guessed.

## Features

- Random word selection each round
- Word-specific hints
- Four lives per game
- Character-based guessing with underscore placeholders for hidden letters
- Win and lose conditions
- Pure Python implementation with no external dependencies

## Demo

**Starting the game**

```text
Hint: A red fruit
_ _ _ _ _
Guess a character:
```

**Incorrect guess**

```text
Guess a character: z
_ _ _ _ _
Wrong! 3 lives left
```

**Winning**

```text
You won!
```

**Losing**

```text
You lost! The word was 'apple'
```

## How to Play

1. Run the Python program.
2. Read the displayed hint.
3. Enter one character when prompted.
4. Correct characters are revealed in their corresponding positions.
5. An incorrect character costs one life.
6. You have four lives in total.
7. Reveal the complete word before running out of lives to win.

## Word List

| Fruit  | Hint                                   |
|--------|-----------------------------------------|
| Apple  | A red fruit                             |
| Kiwi   | Green inside, brown outside             |
| Mango  | King of fruits                          |
| Orange | Its colour is the name of the fruit     |

## How It Works

```text
START
  │
  ▼
Select random word
  │
  ▼
Display its hint
  │
  ▼
Hide word with underscores
  │
  ▼
Player guesses a character
  │
  ├── Correct → Reveal character
  │
  └── Wrong   → Lose one life
  │
  ▼
Is the word fully guessed?
  ├── Yes → You win
  └── No  → Are lives at 0?
              ├── Yes → You lose
              └── No  → Continue guessing
```

## Getting Started

### Prerequisites

Python 3.x is required. Verify your installation:

```bash
python --version
```

### Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/word-guessing-game.git
cd word-guessing-game
```

### Usage

Run the game:

```bash
python word_game.py
```

## Project Structure

```text
word-guessing-game/
├── word_game.py
├── README.md
├── LICENSE
└── screenshots/
    ├── game-start.png
    ├── gameplay.png
    └── game-result.png
```

## Screenshots

Add screenshots to the `screenshots/` folder, or remove this section if none are available yet.

| Game Start | Gameplay | Result |
|---|---|---|
| ![Game Start](screenshots/game-start.png) | ![Gameplay](screenshots/gameplay.png) | ![Game Result](screenshots/game-result.png) |

## Roadmap

Planned or possible future improvements:

- [ ] Expand word list and add categories
- [ ] Prevent repeated guesses
- [ ] Add difficulty levels
- [ ] Add a scoring system
- [ ] Support multiple rounds
- [ ] Improve input validation
- [ ] Add a graphical user interface
- [ ] Add sound effects

## What This Project Demonstrates

- Working with Python lists and the `random` module
- Handling user input and validation
- `for` and `while` loop control flow
- Conditional logic and basic game-state management
- String manipulation for masking and revealing characters

## Technologies

- Python 3
- Python Standard Library (`random`)

No external packages are required.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Author

vaishnavi

If you found this project useful, consider starring the repository.
