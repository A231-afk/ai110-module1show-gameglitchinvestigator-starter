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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
