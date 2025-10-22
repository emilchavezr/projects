import streamlit as st
import random

letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')
symbols = list('!#$%&()*+')

st.title("🔐 PyPassword Generator")

nr_letters = st.number_input("How many letters?", min_value=0, value=4)
nr_symbols = st.number_input("How many symbols?", min_value=0, value=2)
nr_numbers = st.number_input("How many numbers?", min_value=0, value=2)

if st.button("Generate password"):
    password = []
    for _ in range(nr_letters):
        password.append(random.choice(letters))
    for _ in range(nr_symbols):
        password.append(random.choice(symbols))
    for _ in range(nr_numbers):
        password.append(random.choice(numbers))
    random.shuffle(password)
    final_password = "".join(password)
    st.success(f"**Your password:** {final_password}")
    st.code(final_password)
