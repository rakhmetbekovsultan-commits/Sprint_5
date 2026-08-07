from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HeaderLocators, LoginPageLocators, RegistrationPageLocators


class TestLogin:

    def test_login_from_main_page_login_button(self, driver, registered_user):
        email, password, _ = registered_user
        driver.get("https://stellarburgers.education-services.ru")
        
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(HeaderLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        login_button.click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(email)
    
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
        )

    def test_login_from_personal_account_button(self, driver, registered_user):
        email, password, _ = registered_user
        driver.get("https://stellarburgers.education-services.ru/")
    
        driver.find_element(*HeaderLocators.PERSONAL_ACCOUNT_BUTTON).click()
    
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(email)
    
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
        )

    def test_login_from_registration_form(self, driver):
        driver.get("https://stellarburgers.education-services.ru/register")
    
        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Войти']"))
        )
        login_link.click()
    
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        assert "/login" in driver.current_url

    def test_login_from_forgot_password_form(self, driver):
        driver.get("https://stellarburgers.education-services.ru/forgot-password")
    
        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Войти']"))
        )
        login_link.click()
    
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        assert "/login" in driver.current_url