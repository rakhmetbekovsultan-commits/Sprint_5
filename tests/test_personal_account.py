from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import HeaderLocators, LoginPageLocators, ProfilePageLocators
from data import URL

BASE_URL = "https://stellarburgers.education-services.ru"


class TestPersonalAccount:

    # Вспомогательный метод авторизации
    def _login(self, driver, email, password):
        driver.get(f"{BASE_URL}/login")
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # Ждем появления кнопки "Оформить заказ" на главной (подтверждает успешный вход)
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
        )

    # 1. Переход в Личный Кабинет по клику в шапке
    def test_go_to_personal_account_success(self, driver, registered_user):
        email, password, _ = registered_user
        self._login(driver, email, password)

        # Ожидаем кликабельности кнопки «Личный кабинет» в шапке и кликаем
        personal_account_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(HeaderLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()

        # Ожидаем смены URL на страницу профиля
        WebDriverWait(driver, 15).until(
            EC.url_contains("/account")
        )

        # Проверяем, что кнопка "Выйти" видима
        logout_button = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)
        )
        assert logout_button.is_displayed()

    # 2а. Переход в конструктор по клику на кнопку «Конструктор»
    def test_go_from_account_to_constructor_by_button(self, driver, registered_user):
        email, password, _ = registered_user
        self._login(driver, email, password)

        # Заходим в личный кабинет
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(HeaderLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        WebDriverWait(driver, 15).until(EC.url_contains("/account"))

        # Клик на кнопку «Конструктор»
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(HeaderLocators.CONSTRUCTOR_BUTTON)
        ).click()
        
        # Проверка перехода
        WebDriverWait(driver, 15).until(EC.url_to_be(f"{URL.BASE_URL}/"))
        assert driver.current_url == f"{URL.BASE_URL}/"

    # 2б. Переход в конструктор по клику на логотип
    def test_go_from_account_to_constructor_by_logo(self, driver, registered_user):
        email, password, _ = registered_user
        self._login(driver, email, password)

        # Заходим в личный кабинет
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(HeaderLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        WebDriverWait(driver, 15).until(EC.url_contains("/account"))

        # Клик на логотип
        logo = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(HeaderLocators.LOGO)
        )
        driver.execute_script("arguments[0].click();", logo)
        
        # Проверка перехода
        WebDriverWait(driver, 15).until(EC.url_to_be(f"{URL.BASE_URL}/"))
        assert driver.current_url == f"{URL.BASE_URL}/"
        
    # 3. Выход из аккаунта по кнопке «Выйти» в личном кабинете
    def test_logout_success(self, driver, registered_user):
        email, password, _ = registered_user
        self._login(driver, email, password)

        # Переходим в личный кабинет через шапку
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(HeaderLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        # Ждем загрузки подстраницы профиля
        WebDriverWait(driver, 15).until(EC.url_contains("/account"))

        # Ждем, пока кнопка "Выйти" станет видимой и кликабельной
        logout_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)
        )
        logout_button.click()

        # Проверяем успешный выход (возврат на /login)
        WebDriverWait(driver, 15).until(
            EC.url_to_be(f"{BASE_URL}/login")
        )
        login_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        assert login_button.is_displayed()