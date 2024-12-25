# import
import random
# String
import string


# Generate a random password of length 8

# password
password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))


print("Generated password:", password)