import random
import string
letters = string.ascii_letters
numbers = string.digits
characters = letters + numbers
while True:
    try:
        length = int(input("Enter password length (e.g. 8): "))
        if length < 1:
            print("Please enter a positive number.")
        else:
            break
    except ValueError:
        print("Invalid input. Enter a number.")
password = ''.join(random.choice(characters) for _ in range(length))
print(f"\nGenerated Password: {password}")