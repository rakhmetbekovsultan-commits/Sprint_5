import pytest
import random
import string
from selenium import webdriver
from locators import RegisterPageLocators


@pytest.fixture
def driver():
    """Фикстура для инициализации и закрытия браузера Chrome."""
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless") # Раскомментируйте при необходимости запуска без GUI
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def generate_email():
    """Генерация случайного email для тестов."""
    domains = ["gmail.com", "yandex.ru", "mail.ru"]
    username = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = random.choice(domains)
    return f"{username}@{domain}"


def generate_password(length=8):
    """Генерация случайного пароля."""
    characters = string.ascii_letters + string.digits
    return "".join(random.choices(characters, k=length))


@pytest.fixture
def registered_user(driver):
    """Фикстура создаёт нового пользователя через интерфейс и возвращает его данные."""
    base_url = "https://stellarburgers.education-services.ru"
    email = generate_email()
    password = generate_password(8)
    name = "Тест"

    driver.get(f"{base_url}/register")
    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    return email, password, name