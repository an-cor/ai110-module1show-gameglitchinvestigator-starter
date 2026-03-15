# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.

The game's purpose is to find glitches happening from AI generated code including UI and logic. While playing the game, there are a few things that are buggy and the whole point is to find these to then try and fix them. The actual game is played by having a random number generated and guessing this number. There are easy, medium and hard levels that affect the range the number is to be guessed and the amount of guesses a player has.

- [x] Detail which bugs you found.

I found that the difficulty button under settings, the easy setting would have an unresponsive UI that wouldn't reflect the range. The hard difficulty has bad logic in which the range of 1-50 was actually easier than normal difficulty of 1-100.

The new game button did not fully reset the game state since the page does not reload cleanly with fresh variables (secret number, attempts, score, history, etc.). A new game would load the previous game's data.

The input (the guess) was also buggy where a game would accept numbers outside the expected range like -1 or 1,000,000. These values should be rejected based on the current difficulty range and should be within the bounds of the range. Strings (like words) would also be allowed as guesses when only digits should be accepted.

- [x] Explain what fixes you applied.

I made sure to have a UI that was responsive to what is being selected in the settings when it came to the difficulty levels. The developer debug info, the settings, and what is being showed to the player all had to match and make sense while playing the game. I also had the amount of attempts and ranges per difficulty changed to match something that scaled relative to the difficulty. 

I made sure to change the logic for the "new game" button to reset the variables of the previous game (completed or not) to restart fresh based on the settings. 

I added validation to the input (the guess) to make sure that it was a digit, not a string, and within bounds of the range for the guess. 


## 📸 Demo

- [x] [Insert a screenshot of your fixed, winning game here]

![game-ui.png](game UI)

## 🚀 Stretch Features

- [x] [Challenge 1: Advanced Edge-Case Testing]

![pytest-screenshot.png](pytest picture)

- [x] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]

![enhanced-game-ui.png](history UI)