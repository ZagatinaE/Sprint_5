import random

NAME = "Ekaterina"
MY_EMAIL = "zig.89@mail.ru"
CORRECT_PASSWORD = "1234S?"
INCORRECT_PASSWORD = "W1234"
DOMAIN = "yandex.ru"

def generate_email():
    random_part = f"{random.randint(100, 999):03d}"
    return f"Ekaterina_Zagatina_20_{random_part}@{DOMAIN}".replace(" ", "")


NEW_EMAIL = generate_email()




def generate_password():
    return f"{random.randint(10000, 99999)}{random.choice('abcdefghijklmnopqrstuvwxyz')}"

NEW_PASSWORD = generate_password()