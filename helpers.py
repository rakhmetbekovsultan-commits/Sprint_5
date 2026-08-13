import random

def generate_email():
    # Пример: testtestov_99_123@yandex.ru
    random_digits = random.randint(100, 999)
    return f"testtestov_99_{random_digits}@yandex.ru"

def generate_password(length=8):
    return "".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=length))