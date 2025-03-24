import streamlit as st # type: ignore
import random
import string
import re 
# password strength checker

st.set_page_config(page_title="Password Strength Checker and Password Generator", page_icon="🔒")

st.title("Password Strength Checker🔐")
st.markdown(""" 
 welcome to the ultimate Password Strength Checker and Password Generator!
            
 use this simple tool to check the strength of your password and generate a strong password.""")


password = st.text_input("Enter your password", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌Password should be at least 8 characters long")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌Password should contain both uppercase and lowercase characters")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one number")
    if re.search(r"[!@#$&^%*<>]", password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one special character (!@#$&^%*<>)")
    if score == 4:
        feedback.append("✅Password is strong.")
    elif score == 3:
        feedback.append("🟡Password is medium Strength, It could be stronger.")
    else:
        feedback.append("🔴Password is weak, Make it stronger.")
    
    if feedback:
        st.markdown("## Improvement Suggestions")
        for suggestion in feedback:
            st.write(suggestion)

else:
    st.info("Enter a password to check its strength")

st.write("____________________________________________________________________")

# Password Generator
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

