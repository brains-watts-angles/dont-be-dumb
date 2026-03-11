import random
import streamlit as st

st.title("🧠 Don't Be Dumb")

# Initialize session state
if "true_number" not in st.session_state:
    st.session_state.true_number = random.randint(1, 100)
    st.session_state.asked_dumb = False
    st.session_state.game_over = False
    st.session_state.message = ""

# Step 1: Are you dumb?
if not st.session_state.asked_dumb:
    answer = st.radio("Are you dumb?", ["", "Yes", "No"], index=0)
    if answer == "Yes":
        st.write("Obviously.")
        st.session_state.asked_dumb = True
        st.rerun()
    elif answer == "No":
        st.write("Let's see about that.")
        st.session_state.asked_dumb = True
        st.rerun()

# Step 2: Guessing game
elif not st.session_state.game_over:
    if st.session_state.message:
        st.write(st.session_state.message)

    guess = st.number_input("Pick a number between 1 and 100:", min_value=1, max_value=100, step=1)

    if st.button("Submit Guess"):
        true_number = st.session_state.true_number
        try:
            guess = int(guess)
            if guess < 1 or guess > 100:
                st.session_state.message = "Input a positive whole number between 1 and 100, genius."
            elif guess == true_number:
                st.session_state.message = f"You are right. The number is {true_number}. Pure luck. Don't be dumb."
                st.session_state.game_over = True
            elif guess < true_number:
                st.session_state.message = "You are dumb. Your guess is LOW. Try again."
            else:
                st.session_state.message = "You are dumb. Your guess is HIGH. Try again."
        except ValueError:
            st.session_state.message = "Input a positive whole number between 1 and 100, genius."
        st.rerun()

# Step 3: Game over
else:
    st.success(st.session_state.message)
    if st.button("Play Again"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
