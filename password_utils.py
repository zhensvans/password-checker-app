import secrets
import string
import math
import requests
import hashlib


def is_password_breached(password):
    hashed_password = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = hashed_password[:5], hashed_password[5:]
    response = requests.get(f'https://api.pwnedpasswords.com/range/{prefix}')
    if response.status_code == 200:
        return suffix in response.text
    else:
        print(f'Failed to check password: {response.status_code}')
        return False


def get_breached_count(password: int) -> str | int:
    hashed_password = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = hashed_password[:5], hashed_password[5:]
    response = requests.get(f'https://api.pwnedpasswords.com/range/{prefix}')
    if response.status_code == 200:
        if suffix in response.text:
            breached_count = response.text.split(suffix + ':')[1].split('\n')[0].strip()
            return breached_count
    return 0


def analyze_password(password):
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)
    has_ten = len(password) >= 10

    return has_uppercase, has_lowercase, has_digit, has_symbol, has_ten


def calculate_entropy(password):
    char_pool = len(string.ascii_letters) + len(string.digits) + len(string.punctuation)
    entropy = math.log2(char_pool) * len(password)
    return entropy


def get_password_strength(entropy):
    if entropy <= 40:
        return "Very weak"
    elif (entropy >= 41) and (entropy <= 60):
        return "Weak"
    elif (entropy >= 61) and (entropy <= 80):
        return "Moderate"
    elif (entropy >= 81) and (entropy <= 100):
        return "Strong"
    else:
        return "Very strong"


def generate_password(length=12):
    length = max(length, 12)

    uppercase_chars = string.ascii_uppercase
    lowercase_chars = string.ascii_lowercase
    digit_chars = string.digits
    special_chars = string.punctuation

    gen_password = (
            secrets.choice(uppercase_chars) +
            secrets.choice(lowercase_chars) +
            secrets.choice(digit_chars) +
            secrets.choice(special_chars)
    )

    remaining_length = length - 4
    gen_password += ''.join(
        secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(remaining_length))

    password_list = list(gen_password)
    secrets.SystemRandom().shuffle(password_list)
    gen_password = ''.join(password_list)

    while is_password_breached(gen_password):
        password_list = list(gen_password)
        secrets.SystemRandom().shuffle(password_list)
        gen_password = ''.join(password_list)

    return gen_password
