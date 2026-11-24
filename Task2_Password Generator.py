
import string
import secrets

def generate_password(length):

    if length < 4:
        print("Password length must be at least 4.")
        return

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one character from each category
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    all_characters = lowercase + uppercase + digits + symbols

    # Generate remaining characters
    for i in range(length - 4):
        password.append(secrets.choice(all_characters))

    # Shuffle the password
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


def main():
    print("======= PASSWORD GENERATOR =======")

    try:
        length = int(input("Enter password length: "))

        password = generate_password(length)

        if password:
            print("\nGenerated Password:", password)

    except ValueError:
        print("Please enter a valid integer.")


main()
