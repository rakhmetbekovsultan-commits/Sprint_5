from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HeaderLocators, LoginPageLocators
from data import URL


class TestLogin:

    def test_login_from_main_page_login_button(self, driver, registered_user):
        email, password, _ = registered_user
        driver.get(URL.BASE_URL)
        
        # Кликаем именно по кнопке «Войти в аккаунт» на главной
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.MAIN_PAGE_LOGIN_BUTTON)
        )
        login_button.click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(email)
    
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    
        # Добавлен assert для проверки успешного входа
        make_order_btn = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.MAKE_ORDER_BUTTON)
        )
        assert make_order_btn.is_displayed()

    def test_login_from_personal_account_button(self, driver, registered_user):
        email, password, _ = registered_user
        driver.get(URL.BASE_URL)
    
        driver.find_element(*HeaderLocators.PERSONAL_ACCOUNT_BUTTON).click()
    
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(email)
    
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    
        # Добавлен assert для проверки успешного входа
        make_order_btn = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.MAKE_ORDER_BUTTON)
        )
        assert make_order_btn.is_displayed()

    def test_login_from_registration_form(self, driver):
        driver.get(URL.REGISTER_URL)
    
        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_LINK)
        )
        login_link.click()
    
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        assert "/login" in driver.current_url

    def test_login_from_forgot_password_form(self, driver):
        driver.get(URL.FORGOT_PASSWORD_URL)
    
        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_LINK)
        )
        login_link.click()
    
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        assert "/login" in driver.current_url