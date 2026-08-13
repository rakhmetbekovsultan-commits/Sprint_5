from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import HeaderLocators, LoginPageLocators, ProfilePageLocators
from data import URL


class TestPersonalAccount:

    def _login(self, driver, email, password):
        driver.get(URL.LOGIN_URL)
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(LoginPageLocators.MAKE_ORDER_BUTTON)
        )

    def test_go_to_personal_account_success(self, driver, registered_user):
        email, password, _ = registered_user
        self._login(driver, email, password)

        personal_account_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(HeaderLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()

        WebDriverWait(driver, 15).until(
            EC.url_contains("/account")
        )

        logout_button = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)
        )
        assert logout_button.is_displayed()

    def test_go_from_account_to_constructor_by_button(self, driver, registered_user):
        email, password, _ = registered_user
        self._login(driver, email, password)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(HeaderLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        WebDriverWait(driver, 15).until(EC.url_contains("/account"))

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(HeaderLocators.CONSTRUCTOR_BUTTON)
        ).click()
        
        WebDriverWait(driver, 15).until(EC.url_to_be(f"{URL.BASE_URL}/"))
        assert driver.current_url == f"{URL.BASE_URL}/"

    def test_go_from_account_to_constructor_by_logo(self, driver, registered_user):
        email, password, _ = registered_user
        self._login(driver, email, password)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(HeaderLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        WebDriverWait(driver, 15).until(EC.url_contains("/account"))

        logo = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(HeaderLocators.LOGO)
        )
        driver.execute_script("arguments[0].click();", logo)
        
        WebDriverWait(driver, 15).until(EC.url_to_be(f"{URL.BASE_URL}/"))
        assert driver.current_url == f"{URL.BASE_URL}/"
        
    def test_logout_success(self, driver, registered_user):
        email, password, _ = registered_user
        self._login(driver, email, password)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(HeaderLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        WebDriverWait(driver, 15).until(EC.url_contains("/account"))

        logout_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)
        )
        logout_button.click()

        WebDriverWait(driver, 15).until(
            EC.url_to_be(URL.LOGIN_URL)
        )
        login_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        assert login_button.is_displayed()
