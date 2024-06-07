import re

def check_password_strength(password):
    # Minimum length requirement
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."

    # Check for uppercase and lowercase letters
    if not re.search("[A-Z]", password) or not re.search("[a-z]", password):
        return "Weak: Password must contain both uppercase and lowercase letters."

    # Check for numbers
    if not re.search("[0-9]", password):
        return "Weak: Password must contain at least one number."

    # Check for special characters
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Password must contain at least one special character."

    return "Strong: Password meets complexity requirements."

# Test the function
password = input("Enter your password: ")
strength = check_password_strength(password)
print(strength)
