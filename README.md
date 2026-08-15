<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F172A,45:2563EB,100:22C55E&height=170&section=header&text=Number%20Guessing%20Game&fontSize=38&fontColor=ffffff&animation=fadeIn&fontAlignY=36&desc=A%20clean%20Python%20CLI%20game%20with%20hints%2C%20score%20tracking%2C%20and%20input%20validation&descSize=14&descAlignY=56" alt="Number Guessing Game banner" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Type-CLI%20Game-2563EB?style=for-the-badge" alt="CLI Game" />
  <img src="https://img.shields.io/badge/Focus-Logic%20%2B%20Files-7C3AED?style=for-the-badge" alt="Logic and files" />
  <img src="https://img.shields.io/badge/Level-Beginner-22C55E?style=for-the-badge" alt="Beginner" />
  <img src="https://img.shields.io/badge/License-MIT-F59E0B?style=for-the-badge" alt="MIT License" />
</p>

---

## Overview

Number Guessing Game is a beginner-friendly Python command-line project where the computer chooses a hidden number between `1` and `100`, and the player tries to guess it using higher/lower hints.

It also stores the best score in `Hi-score.txt`, making the game a small but useful practice project for logic, loops, validation, and file handling.

---

## Project Highlights

<table>
  <tr>
    <td><b>Random Challenge</b></td>
    <td>The secret number is generated with Python's `random` module.</td>
  </tr>
  <tr>
    <td><b>Smart Hints</b></td>
    <td>The game tells the player whether to guess higher or lower.</td>
  </tr>
  <tr>
    <td><b>Input Validation</b></td>
    <td>Invalid text and out-of-range numbers are handled cleanly.</td>
  </tr>
  <tr>
    <td><b>High Score</b></td>
    <td>The lowest attempt count is saved and reused across runs.</td>
  </tr>
</table>

---

## Project Structure

```text
Number-guessing-game/
|-- Number-guessing-game.py
|-- Hi-score.txt
|-- LICENSE
`-- README.md
```

---

## How To Run

```bash
git clone https://github.com/bilal-dev-0x/Number-guessing-game.git
cd Number-guessing-game
python Number-guessing-game.py
```

---

## Example Output

```text
Welcome to the Number Guessing Game!
I have selected a number between 1 and 100.
Guess the number (1-100): 50
Higher number, please.
Guess the number (1-100): 75
Lower number, please.
Guess the number (1-100): 63
You guessed the correct number in 3 attempts.
Incredible! You guessed it in very few attempts.
New high score: 3
```

---

## Concepts Practiced

| Concept | Practice |
|---|---|
| Random numbers | `random.randint()` |
| Loops | Repeating guesses until the answer is correct |
| Functions | Smaller reusable blocks for score, input, and feedback |
| Exceptions | Handling invalid input with `try` / `except` |
| Files | Reading and writing `Hi-score.txt` |
| Conditions | Comparing guesses and updating game state |

---

## Future Improvements

- Add difficulty levels.
- Add replay without restarting the script.
- Add a scoreboard with dates.
- Add tests for high-score logic.
- Convert the project into a small GUI game.

---

<p align="center">
  <b>A compact Python game built to practice logic, validation, and file-based state.</b>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:22C55E,50:2563EB,100:0F172A&height=95&section=footer" alt="Footer wave" />
</p>
