import random
import string

def generate_password(length):
    # Define the set of characters to choose from
    chars = string.ascii_letters + string.digits + string.punctuation

    # Generate a password by randomly choosing characters from the set
    password = ''.join(random.choice(chars) for i in range(length))

    return password

# Example usage: generate a 12-character password
password = generate_password(12)
print(password)

