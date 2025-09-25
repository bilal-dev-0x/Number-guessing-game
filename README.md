This is code is published under MIT License
![License](https://img.shields.io/badge/License-MIT-green.svg)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Status](https://img.shields.io/badge/Project-Active-brightgreen)

## 📘 README.md

```markdown
# 🎯 Number Guessing Game

This is a simple Python console game saved as `Number-guessing-game.py`. The goal is to guess a randomly generated number between 1 and 100. The game tracks your attempts and stores your best score in a file called `Hi-score.txt`.

## 📂 Files Required

- `Number-guessing-game.py` → Main game script.
- `Hi-score.txt` → Stores the best (lowest) number of attempts.

> ✅ Make sure `Hi-score.txt` exists in the same folder before running the game. You can create it manually as an empty file.

## 🚀 How to Run

1. Open your terminal or command prompt.
2. Navigate to the folder containing `Number-guessing-game.py`.
3. Run the game using:
   ```bash
   python Number-guessing-game.py
   ```

## 🧠 Game Rules

- The computer randomly selects a number between 1 and 100.
- You guess until you find the correct number.
- After each guess, the game tells you whether to guess higher or lower.
- It counts your total attempts.
- Based on your performance, it gives feedback.
- If your attempt count is better than the previous high score, it updates `Hi-score.txt`.

## 🏆 Feedback System

- **≤ 10 attempts** → "Incredible!"
- **11–19 attempts** → "Doing good, improve more."
- **≥ 20 attempts** → "Too many attempts, try to improve."

## 💾 High Score Logic

- If your score is better than the saved high score, it updates the file.
- If your score is worse, it encourages you to beat the record.
- If you match the high score, it acknowledges it.

## 📌 Example Output

```
Guess the number: 50
Higher number... Please.
Guess the number: 75
Lower number... Please.
Guess the number: 63
You guessed the correct number in 3 attempts.
You have done it in few attempts... this is incredible.
New high score: 3
```

