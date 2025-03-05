import streamlit as st
import random
import string

def password_generator(length, use_digits, use_special_characters):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_characters:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length)) # the reason of underscore variable is define that loop has no specific length


st.title('Password Generator🔐')

length = st.slider(' Select Password Length', min_value=6, max_value=32, value=12)

use_digits = st.checkbox('Use Digits')

use_special_characters = st.checkbox('Use Special Characters')

if st.button("Generate Password"):
    password = password_generator(length, use_digits, use_special_characters)
    st.write(f'Generated Password: {password}')


st.write("____________________________________________________________________")    
st.write("Build with by ❤️ [Khadija Faisal](https://github.com/khadija-faisal) ")

