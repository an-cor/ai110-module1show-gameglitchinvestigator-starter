import random
# FIX: Refactored core logic into logic_utils.py using Claude; verified pytest runs and app still launches.
import streamlit as st
from logic_utils import DIFFICULTY_CONFIG, get_range_for_difficulty, parse_guess, check_guess, update_score, get_hint_message, get_hot_cold_label

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

# FIX: Difficulty now drives range and attempt limit via DIFFICULTY_CONFIG
cfg = DIFFICULTY_CONFIG[difficulty]
low, high, attempt_limit = cfg["min_num"], cfg["max_num"], cfg["max_attempts"]

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")


# FIX: New Game resets all round state (secret, attempts, score, status, history) via helper
def reset_game_state():
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.difficulty = difficulty


# Initialize on first load
if "secret" not in st.session_state:
    reset_game_state()

# Reset when difficulty changes
if st.session_state.get("difficulty") != difficulty:
    reset_game_state()

st.subheader("Make a guess")

st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    reset_game_state()
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

# FIX: Attempts only increment on valid, in-range guesses; invalid input is never added to history
if submit:
    ok, guess_int, err = parse_guess(raw_guess, low, high)

    if not ok:
        st.error(err)
    else:
        st.session_state.attempts += 1

        secret = st.session_state.secret
        outcome = check_guess(guess_int, secret)
        message = get_hint_message(outcome)

        # FIX: Hot/cold proximity label added alongside directional hint
        proximity = get_hot_cold_label(guess_int, secret, low, high)

        # FIX: History now stores dicts so the session summary table can show result and proximity
        st.session_state.history.append(
            {"Guess": guess_int, "Result": outcome, "Proximity": proximity}
        )

        # FIX: Color-coded feedback — success for win, error for too high, info for too low
        if show_hint:
            if outcome == "Win":
                st.success(message)
            elif outcome == "Too High":
                st.error(f"{message}  {proximity}")
            else:
                st.info(f"{message}  {proximity}")

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.error(
                    f"Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                )

# FIX: Session summary table shows all guesses, results, and proximity for the current game
if st.session_state.history:
    st.subheader("📋 Guess History")
    st.table(st.session_state.history)

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
