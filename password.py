import random
import string

def generate_password(length):
    # Define character set: letters (upper & lower), digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Get user input for password length
try:
    length = int(input("Enter the desired password length: "))
    if length < 4:
        print("Password length should be at least 4 characters.")
    else:
        password = generate_password(length)
        print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")
