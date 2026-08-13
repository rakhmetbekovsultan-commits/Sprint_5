import pytest
from selenium import webdriver
from locators import RegisterPageLocators
from helpers import generate_email, generate_password
from data import URL


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def registered_user(driver):
    email = generate_email()
    password = generate_password(8)
    name = "Тест"

    driver.get(URL.REGISTER_URL)
    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    return email, password, name