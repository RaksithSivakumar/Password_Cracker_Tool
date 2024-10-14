import streamlit as st
import time
from attack import brute_force_attack, dictionary_attack

# Streamlit UI
st.title("Password Cracker Tool")

# User input for password and attack type
target_password = st.text_input("Enter the target password:", type="password")
attack_type = st.selectbox("Select Attack Type:", ["Brute Force Attack", "Dictionary Attack"])

# Button to start cracking
if st.button("Start Cracking"):
    if target_password:
        if attack_type == "Brute Force Attack":
            st.write(brute_force_attack(target_password))
        elif attack_type == "Dictionary Attack":
            st.write(dictionary_attack(target_password))
    else:
        st.warning("Please enter a target password.")

st.write("Logs will appear here as the attack progresses.")
