import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Random Password Generator")
    print("===========================")

    num_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter the password length (recommended minimum: 12 characters): "))

    if password_length < 12:
        print("Warning: Passwords shorter than 12 characters may not be secure.")

    passwords = []
    for _ in range(num_passwords):
        password = generate_password(password_length)
        passwords.append(password)

    print("\nGenerated Passwords:")
    for i, password in enumerate(passwords, start=1):
        print(f"Password {i}: {password}")

if __name__ == "__main__":
    main()
