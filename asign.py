import streamlit as st
import re

# Set up the page with a friendly title and icon
st.set_page_config(
    page_title="Password Strength Checker", 
    page_icon="🔒",
)

# Main title with emoji
st.title("🔒 Password Strength Checker")
st.markdown("""
    ### Check how strong your password is in real-time!
    ### We'll analyze your password and give you tips to make it stronger.
""")


# Password input field with helpful placeholder
password = st.text_input(
    "Type your password here:",
    type="password",
    placeholder="Enter your password...",
    help="We don't store your password - this checks it in your browser only"
)

# Define what makes a password strong
def check_password_strength(password):
    score = 0
    feedback = []
    
    # Check password length (minimum 8 characters)
    length_ok = len(password) >= 8
    if length_ok:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")
    
    # Check for uppercase letters
    has_upper = re.search(r'[A-Z]', password)
    if has_upper:
        score += 1
    else:
        feedback.append("Add at least one UPPERCASE letter (A-Z)")
    
    # Check for lowercase letters
    has_lower = re.search(r'[a-z]', password)
    if has_lower:
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z)")
    
    # Check for numbers
    has_number = re.search(r'\d', password)
    if has_number:
        score += 1
    else:
        feedback.append("Include at least one number (0-9)")
    
    # Check for special characters
    has_special = re.search(r'[@$!%*?&]', password)
    if has_special:
        score += 1
    else:
        feedback.append("Add a special character (@, $, !, %, *, ?, &)")
    
    return score, feedback

# Only show results if user has entered something
if password:
    # Calculate the strength
    score, feedback = check_password_strength(password)
    
    # Define our strength levels with colors and emojis
    strength_levels = {
        0: ("Very Weak", "🔴", "Extremely easy to crack - very unsafe!"),
        1: ("Weak", "🟥", "Easy to guess - needs improvement"),
        2: ("Fair", "🟧", "Somewhat secure but could be stronger"),
        3: ("Moderate", "🟨", "Decent protection for casual use"),
        4: ("Strong", "🟩", "Good security for most purposes"),
        5: ("Very Strong", "🟩✨", "Excellent! Hard to crack")
    }
    
    # Get the appropriate level based on score
    level, emoji, description = strength_levels.get(score, ("Unknown", "❓", "Cannot determine"))
    
    # Visual progress bar
    st.progress(score / 5)
    
    # Show improvement tips if needed
    if feedback:
        st.markdown("### 🔍 How to improve your password:")
        for tip in feedback:
            st.write(f"- {tip}")
        
        st.markdown("""
            💡 **Pro Tip:** Combine multiple words with numbers and symbols
            (like "Blue42Dragon$Sky") for a strong yet memorable password.
        """)
    else:
        st.success("🎉 Excellent! Your password meets all security requirements!")
        
else:
    # Initial message before user types anything
    st.info("""
        👆 Start typing your password above to check its strength.
        We'll show you how secure it is and ways to make it stronger.
    """)

# Add some extra security tips in an expandable section
with st.expander("🔐 Learn more about password security"):
    st.markdown("""
        **Why strong passwords matter:**
        - Weak passwords are easily guessed or cracked by hackers
        - Many people reuse passwords across sites, multiplying the risk
        - Strong passwords protect your personal and financial information
        
        **Creating strong passwords:**
        1. Use at least 12 characters when possible
        2. Combine letters (upper and lower case), numbers, and symbols
        3. Avoid common words, phrases, or personal information
        4. Consider using a password manager to generate and store passwords
        
        **Example strong passwords:**
        - `Sunset$Over7Mountains!`
        - `Correct42HorseBatteryStaple`
        - `Pizza@8WithExtraCheese!`
    """)