import random
import streamlit as st

st.title("🧠 Don't Be Dumb")

# Initialize session state
if "true_number" not in st.session_state:
    st.session_state.true_number = random.randint(1, 100)
    st.session_state.dumb_response = ""
    st.session_state.asked_dumb = False
    st.session_state.game_over = False
    st.session_state.message = ""

# Step 1: Are you dumb?
if not st.session_state.asked_dumb:
    answer = st.text_input("Are you dumb?").lower().strip()
    if st.button("Submit"):
        if answer == "yes":
            st.session_state.dumb_response = "Obviously."
        elif answer == "no":
            st.session_state.dumb_response = "Let's see about that."
        else:
            st.session_state.dumb_response = "I'm thinking you probably are."
        st.session_state.asked_dumb = True
        st.rerun()

# Step 2: Guessing game
elif not st.session_state.game_over:
    st.write(st.session_state.dumb_response)
    if st.session_state.message:
        st.write(st.session_state.message)

    guess = st.text_input("Pick a number between 1 and 100:")

    if st.button("Submit Guess"):
        try:
            guess = int(guess)
            if guess < 1 or guess > 100:
                st.session_state.message = "Input a positive whole number between 1 and 100, genius."
            elif guess == st.session_state.true_number:
                st.session_state.message = f"You are right. The number is {st.session_state.true_number}. Pure luck. Don't be dumb."
                st.session_state.game_over = True
            elif guess < st.session_state.true_number:
                st.session_state.message = "You are dumb. Your guess is LOW. Try again."
            else:
                st.session_state.message = "You are dumb. Your guess is HIGH. Try again."
        except ValueError:
            st.session_state.message = "Input a positive whole number between 1 and 100, genius."
        st.rerun()

# Step 3: Game over
else:
    st.write(st.session_state.dumb_response)
    st.success(st.session_state.message)
    if st.button("Play Again"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
