
import string
import secrets

def generate_password(length, use_numbers, use_symbols):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    characters = letters
    password = []

    if use_numbers:
        characters += numbers
        password.append(secrets.choice(numbers))

    if use_symbols:
        characters += symbols
        password.append(secrets.choice(symbols))

    password.append(secrets.choice(letters))

    while len(password) < length:
        password.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password)

    return "".join(password)


print("===== PASSWORD GENERATOR =====")

while True:
    try:
        length = int(input("\nEnter password length (minimum 4): "))

        if length < 4:
            print("Password length must be at least 4.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.")

while True:
    use_numbers = input("\nInclude numbers? (yes/no): ").lower()

    while use_numbers not in ["yes", "no"]:
        use_numbers = input("Please enter yes or no: ").lower()

    use_symbols = input("Include special characters? (yes/no): ").lower()

    while use_symbols not in ["yes", "no"]:
        use_symbols = input("Please enter yes or no: ").lower()

    numbers_choice = use_numbers == "yes"
    symbols_choice = use_symbols == "yes"

    password = generate_password(length, numbers_choice, symbols_choice)

    print("\nGenerated Password:", password)
    print("Password Length:", len(password))

    again = input("\nGenerate another password? (yes/no): ").lower()

    while again not in ["yes", "no"]:
        again = input("Please enter yes or no: ").lower()

    if again == "no":
        print("Thank you for using Password Generator!")
        break
