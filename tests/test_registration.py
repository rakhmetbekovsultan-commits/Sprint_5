from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import RegistrationPageLocators, LoginPageLocators
from helpers import generate_email, generate_password
from data import URL


class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get(URL.REGISTER_URL)

        email = generate_email()
        password = generate_password(8)

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Иван")
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)

        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be(URL.LOGIN_URL)
        )

        login_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        assert login_button.is_displayed()

    def test_registration_short_password_shows_error(self, driver):
        driver.get(URL.REGISTER_URL)

        email = generate_email()
        short_password = generate_password(5)

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Иван")
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(short_password)

        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.PASSWORD_ERROR)
        )

        assert error_message.is_displayed()
