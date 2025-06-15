import random
import string

def generate_password(length):
    if length < 4:
        return "Password must be at least 4 characters long."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_input():
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Length must be a positive number.")
            return None
        return length
    except ValueError:
        print(" Please enter a valid number.")
        return None

def main():
    print("=== PASSWORD GENERATOR ===")
    length = get_user_input()

    if length:
        password = generate_password(length)
        print(f"Your generated password is:\n{password}")

if __name__ == "__main__":
    main()
