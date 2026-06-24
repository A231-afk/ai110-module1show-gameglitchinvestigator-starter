import random
import streamlit as st

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    # FIX: Claude helped correct attempt counting — start at 0 since no guesses
    # have been made when the game begins.
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

if "difficulty" not in st.session_state:
    # FIX: Claude helped repair the incomplete session-state reset — remember the
    # active difficulty so we can detect when the user switches it.
    st.session_state.difficulty = difficulty

# FIX: Claude helped repair the incomplete session-state reset — changing difficulty
# now resets every game-state value and redraws the secret inside the new range.
if difficulty != st.session_state.difficulty:
    st.session_state.difficulty = difficulty
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.secret = random.randint(low, high)

st.subheader("Make a guess")

# FIX: Claude helped fix the lost confirmation — show the New Game message once
# after the rerun, then clear the flag so it doesn't persist.
if st.session_state.pop("new_game_message", False):
    st.success("New game started.")

# FIX: Claude helped move state-dependent displays after game processing so the UI no longer lags one interaction behind.
status_panel = st.empty()


def render_status_panel():
    with status_panel.container():
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
    # FIX: Claude helped repair the incomplete session-state reset — New Game now
    # clears every game-state value and draws the secret from the selected range.
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.secret = random.randint(low, high)
    # FIX: Claude helped fix the lost confirmation — st.rerun() discarded the
    # immediate st.success(), so stash a flash flag and render it after the rerun.
    st.session_state.new_game_message = True
    st.rerun()

if st.session_state.status != "playing":
    render_status_panel()
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.error(err)
    elif guess_int < low or guess_int > high:
        # FIX: Claude helped correct attempt counting — out-of-range input must not
        # consume an attempt, change the score, or enter valid history.
        st.error(f"Enter a number between {low} and {high}.")
    else:
        # FIX: Claude helped correct attempt counting — increment only for a parsed,
        # in-range guess.
        st.session_state.attempts += 1
        st.session_state.history.append(guess_int)

        # Keep both values numeric so comparisons in check_guess stay numeric (int vs int).
        outcome, message = check_guess(guess_int, st.session_state.secret)

        if show_hint:
            st.warning(message)

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

render_status_panel()

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
