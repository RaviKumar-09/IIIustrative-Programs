import random
import string


# Generate a random password of length 8
password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))