import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import LoginPageLocators, ProfilePageLocators

BASE_URL = "https://stellarburgers.education-services.ru"


class TestProfile:

    def test_open_profile_page(self, driver, registered_user):
        email, password, _ = registered_user
        driver.get(f"{BASE_URL}/login")

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be(f"{BASE_URL}/")
        )

        driver.find_element(*ProfilePageLocators.PROFILE_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be(f"{BASE_URL}/account/profile")
        )
        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.USER_EMAIL_INPUT)
        )
        assert email_input.get_attribute("value") == email

    def test_open_order_history_from_profile(self, driver, registered_user):
        email, password, _ = registered_user
        driver.get(f"{BASE_URL}/login")

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(f"{BASE_URL}/"))
        driver.find_element(*ProfilePageLocators.PROFILE_BUTTON).click()

        history_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ProfilePageLocators.ORDER_HISTORY_LINK)
        )
        history_link.click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be(f"{BASE_URL}/account/order-history")
        )
        assert driver.current_url == f"{BASE_URL}/account/order-history"

    def test_logout_from_profile(self, driver, registered_user):
        email, password, _ = registered_user
        driver.get(f"{BASE_URL}/login")

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(f"{BASE_URL}/"))
        driver.find_element(*ProfilePageLocators.PROFILE_BUTTON).click()

        logout_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)
        )
        logout_btn.click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be(f"{BASE_URL}/login")
        )
        login_btn = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
        assert login_btn.is_displayed()