# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

The game had a board on the left side and the actual game taking up most of the screen space. It had a title, instructions to "make a guess", a box  to enter the guess and buttons to interact with the game. One of the buttons is a developer debug info dropdown that reveals information about the current game.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

1. Difficulty Button

- **Easy**
  - Range should be **1–50**, but the UI does not update to reflect this.
  - Attempts are set to **6**, but Easy mode should likely allow **more attempts than Normal**.
- **Normal**
  - Range: **1–100**
  - Attempts: **8**
- **Hard**
  - Range currently set to **1–50**, which is not harder than Normal.
  - Attempts: **5**

2. "Make a Guess" Input Box

- The input box does **not reflect the difficulty settings shown in the left panel**.
- For example, it may still show or behave as if the range is **1–100** even when a different difficulty is selected.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Claude to help me with this project. 

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

The ai suggested "Implement the functions in logic_utils.py by moving the real implementations from app.py into logic_utils.py." I asked it to change the code written in both files and manually see that the code in app.py was removed then in logic_utils.py code was added. I also chacked it was the same expected logic by running the streamlit app and seeing if things were working correctly.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

The ai suggested "Remove any logic that converts the secret number into a string during gameplay." After I asked it to do so, I noticed that when resetting the game, the secret wouldn't stay as an int and might change into a string. This was misleading until I figured it out by playing a few more times later.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I decided a bug was really fixed after I asked Claude to do something about it, I checked the code it told me it made changes on and looked understandable then I re-ran the game to make sure the bug worked as expected now.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

I manually checked that changing the difficulty of the game would actually change the amount of tries and the range for a new game. Also, after updating the page, the changes were still being tracked correctly. 

- Did AI help you design or understand any tests? How?



---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

The secret would be a randon int between a low and high variable number. 

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

A rerun is like refreshing a page online on your web browser. A session state is like drawing something or editing something but refreshing the page will bring you back to clean page.

- What change did you make that finally gave the game a stable secret number?

Changed the function call of check_guess(...) actually check the secret of the game. After a secret is created, it cannot be altered and the developer debug has to match what the secret is. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

A prompting strategy would be to use claude in planning mode and have it tell me everything that it understands from the codebase and if it can foretell or point out any obvious errors plus lay a roadmap to fixing anything that is wrong. This forced claude to check the state of the entirity of the code then make an evaluation on it before I any work has actually been done. This is also a bird's eye view of code that I might be unfamiliar with but cluade is better at understanding and can show me things I have potentially missed.

- What is one thing you would do differently next time you work with AI on a coding task?

I wouldn't worry so much on the literal implementation of every thing. I have gotten very fixated as an engineer on how things are done but there have been a lot of moments when it is too much attention to detail to actually get the task at hand done. It's a lot of time wasted on small granular problems that do not require so much attention to when things are working and no problems come up.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

AI generated code is very well structured but the infrastrucure is onlt as good as the engineer designing it. I think it can be very useful when a large enough problem is broken down enough so that there is no doubt how an AI can go about finishing a task.