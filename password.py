#Password Generator : Create a program that generates secure passwords basedon specified criteria such as length and character types.
import random
import string

def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars):
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if not characters:
        print("Error: No character types selected. Please try again.")
        return

    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        print("\n--- Password Generator ---")
        length = int(input("Enter the password length: "))
        include_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
        include_lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
        include_numbers = input("Include numbers? (y/n): ").lower() == "y"
        include_special_chars = input("Include special characters? (y/n): ").lower() == "y"

        password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars)

        if password:
            print("\nGenerated Password:", password)
        else:
            print("Please try again.")

        choice = input("\nDo you want to generate another password? (y/n): ")
        if choice.lower() != "y":
            break

    print("\n--- Thank you for using the Password Generator! ---")

if __name__ == "__main__":
    main()