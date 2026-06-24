# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards"). 

 The first time I ran the game, it displayed a number-guessing interface with difficulty settings, a score, attempts, and optional developer information. On Normal difficulty, the sidebar said that I had eight attempts, but the game showed only seven attempts remaining before I had guessed because st.session_state.attempts was initialized to 1 instead of 0. The directional hints were backwards because check_guess() paired "Too High" with "Go HIGHER!" and "Too Low" with "Go LOWER!". I also noticed that an incorrect high guess could increase my score because update_score() added five points for a "Too High" result on an even-numbered attempt. The New Game button also failed to reset all session-state values because it changed only attempts and secret, leaving status, score, and history unchanged.

Written Game-Run Trace
Started Streamlit game on Normal difficulty.
Sidebar displayed: Range 1 to 100, Attempts allowed: 8.
Before entering a guess, the game displayed: Attempts left: 7.
Entered guess: 999.
Observed outcome: Too High.
Observed hint: Go HIGHER!
Observed score after the incorrect guess: 5.

Changed difficulty to Easy.
Sidebar displayed: Range 1 to 20.
Main instructions still displayed: Guess a number between 1 and 100.
Entered guess: 0.
Observed hint: Go LOWER!

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input                                      | Expected Behavior                                                                           | Actual Behavior                                                                | Console Output / Error |
| ------------------------------------------ | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ---------------------- |
| Started a game on Normal difficulty        | The game should begin with 8 attempts remaining                                             | It displayed only 7 attempts remaining                                         | none                   |
| Entered `999` on Normal difficulty         | The game should reject the out-of-range input or say “Too High” and instruct me to go lower | The game accepted the input and displayed “Go HIGHER!”                         | none                   |
| Entered `999` as the first submitted guess | An incorrect guess should not award points                                                  | The score increased from 0 to 5                                                | none                   |
| Selected Easy difficulty                   | The instructions should display the Easy range of 1–20                                      | The sidebar displayed 1–20, but the main instructions still said 1–100         | none                   |
| Entered `0`                                | The game should say the guess is too low and instruct me to go higher                       | The game displayed “Go LOWER!”                                                 | none                   |
| Clicked `New Game` after losing            | The status, attempts, score, history, and secret should reset for a playable new round      | The game remained in the previous lost state and retained old game information |none                   |

---

## 2. How did you use AI as a teammate?

I used Claude in VS Code to inspect the project, explain the bugs, propose focused repairs, and create pytest tests. One correct Claude suggestion was that the higher and lower hint messages were paired with the wrong outcomes inside `check_guess()`. I verified this by tracing a guess of `999`, reviewing the code change, running pytest, and confirming in the Streamlit game that a high guess now says to go lower. One misleading statement was that a correct guess on an even attempt would not be recognized as a win. After I asked Claude to trace a secret and guess of `42`, it clarified that the first equality check fails because the types differ, but the fallback equality check still returns `"Win"`; the actual bug was the unreliable string ordering used for incorrect guesses.

---

## 3. Debugging and testing your fixes

I considered a repair complete only after reviewing the code diff, running automated tests, and reproducing the corrected behavior in the live game. Claude helped create tests for winning guesses, high and low hints, numeric ordering, input parsing, score changes, and difficulty ranges. I ran `.venv/bin/python -m pytest -q`, and the final result showed ` 16 passed in .02 secs` with no failures. I also tested the Streamlit application manually and confirmed that attempts, score, history, hints, input validation, difficulty changes, and New Game resets behaved correctly.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the entire Python script from top to bottom whenever the user interacts with a widget. Regular variables can be recreated during each rerun, while `st.session_state` stores information such as the secret number, attempts, score, history, and game status across reruns. I also learned that source order affects what the user sees: values rendered before state updates can appear one interaction behind. Using session state carefully and rendering state-dependent information after processing the input keeps the interface synchronized.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse is fixing one bug at a time, writing a focused test for it, and reviewing the AI-generated diff before accepting any changes. Next time, I would give the AI narrower instructions earlier and ask it to preserve unrelated files and behavior explicitly. This project showed me that AI-generated code and explanations can be helpful but still contain incorrect assumptions or imprecise wording. I should treat AI output as a proposal that must be tested and reviewed, not as automatically correct code.

