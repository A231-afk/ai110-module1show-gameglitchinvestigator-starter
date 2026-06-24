## 🎮 Game Purpose

Game Glitch Investigator is a Streamlit number-guessing game in which the player selects a difficulty and attempts to find a randomly generated secret number. The game provides higher or lower hints, tracks attempts and score, stores guess history, and ends when the player wins or runs out of attempts.

## 🐛 Bugs Found

The original game contained several reproducible issues:

* Higher and lower hint directions were reversed.
* The secret was converted into a string on alternating attempts, causing unreliable comparisons.
* The attempt counter started at the wrong value.
* Some incorrect guesses increased the score.
* Decimal input was silently converted into an integer.
* Invalid and out-of-range input could consume attempts.
* Score, attempts, and history appeared one interaction behind.
* New Game did not fully reset the game.
* Changing difficulty did not fully reset state.
* The displayed range was hardcoded instead of matching the selected difficulty.

## 🛠️ Fixes Applied

Core functions were moved from `app.py` into `logic_utils.py` so they could be tested independently. The comparison logic now uses integers consistently, and higher or lower hints point in the correct direction. Input parsing rejects invalid and decimal input, wrong guesses consistently subtract points, and attempts increase only for valid in-range guesses. Streamlit session state now resets correctly for New Game and difficulty changes, and state-dependent information is rendered after processing so it updates immediately.

## 📸 Demo Walkthrough

1. The user selects Normal difficulty, which displays the range 1–100 and the allowed number of attempts.
2. The user enters `40`, which is lower than the secret number.
3. The game returns `"Too Low"` and tells the user to go higher.
4. The score decreases by five points, and the attempt count and history update immediately.
5. The user enters `70`, which is higher than the secret number.
6. The game returns `"Too High"` and tells the user to go lower.
7. The user enters the exact secret number.
8. The game displays the winning message, awards the correct score, and prevents additional guesses until a new game begins.
9. The user clicks New Game, and the attempts, score, history, status, and secret number reset.

## 🧪 Test Results

```
16 passed in 0.02s
```

The automated tests cover winning, higher and lower hints, numeric comparisons, input parsing, incorrect-score behavior, and difficulty ranges.

## 🚀 Stretch Features

* [x] Added additional edge-case tests for numeric ordering, invalid input, whitespace, decimals, score behavior, and difficulty ranges.
