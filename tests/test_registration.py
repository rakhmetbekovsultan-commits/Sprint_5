from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import RegistrationPageLocators, LoginPageLocators
from helpers import generate_email, generate_password
from data import URL


class TestRegistration:

    # 1. Успешная регистрация
    def test_successful_registration(self, driver):
        # Открываем напрямую страницу регистрации
        driver.get("https://stellarburgers.education-services.ru/register")

        # Генерируем тестовые данные
        email = generate_email()
        password = generate_password(8)

        # Заполняем форму
        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Иван")
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)

        # Кликаем "Зарегистрироваться"
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        # Ждем редиректа на страницу входа (/login)
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.education-services.ru/login")
        )

        # Проверяем наличие кнопки "Войти" на странице входа
        login_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        assert login_button.is_displayed()

    # 2. Ошибка при пароле меньше 6 символов
    def test_registration_short_password_shows_error(self, driver):
        driver.get("https://stellarburgers.education-services.ru/register")

        email = generate_email()
        short_password = generate_password(5)  # Пароль короче 6 символов

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Иван")
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(short_password)

        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        # Ждем появление ошибки под полем пароля
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.PASSWORD_ERROR)
        )

        assert error_message.is_displayed()