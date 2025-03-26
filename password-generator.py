import streamlit as st
import random
import string

def generate_password(length, use_digits, use_spesial):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits # Adds numbers (0-9) if use_digits is True

    if use_spesial:
        characters += string.punctuation #Adds spesial characters (!, #, $, %, &, ^, *)

    return "".join(random.choice(characters)for _ in range(length))

st.title("Password Generator")

lengh = st.slider("Select Password Length", min_value=6, max_value=32, value=12)

use_digits = st.checkbox("Include Digits")

use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generate_password(lengh, use_digits, use_special)
    st.write(f"Generated Password: {password}")
st.write("----------------")
st.write("Build With ✅💛 by [Fatima Ali](https://www.linkedin.com/in/fatima-zahra-01a715290/)")