import random
import string

def generate_password(length=12, use_special_chars=True):
    
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

   
    characters = letters + digits
    if use_special_chars:
        characters += special_chars

    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 1:
                raise ValueError("Password length must be at least 1.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive integer.")
    
    
    while True:
        use_special_chars = input("Include special characters? (y/n): ").lower()
        if use_special_chars in ('y', 'n'):
            use_special_chars = (use_special_chars == 'y')
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    
    password = generate_password(length, use_special_chars)
    print(f"Generated Password: {password}")

main()
