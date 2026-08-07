from selenium.webdriver.common.by import By


class HeaderLocators:
    # Кнопка «Конструктор» в шапке
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    # Кнопка «Личный кабинет» в шапке
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    # Логотип Stellar Burgers
    LOGO = (By.XPATH, "//div[contains(@class, 'Header_logo')]//a")


class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    PASSWORD_ERROR = (By.XPATH, "//p[contains(@class, 'input__error')]")


# Псевдоним, который ищет conftest.py
RegistrationPageLocators = RegisterPageLocators


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")


class ProfilePageLocators:
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    USER_EMAIL_INPUT = (By.XPATH, "//input[@name='name']")


class ConstructorPageLocators:
    TAB_BUNS = (By.XPATH, "//span[text()='Булки']/parent::div")
    TAB_SAUCES = (By.XPATH, "//span[text()='Соусы']/parent::div")
    TAB_FILLINGS = (By.XPATH, "//span[text()='Начинки']/parent::div")
    FIRST_INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]")
    INGREDIENT_COUNTER = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]//p[contains(@class, 'counter__num')]")
    CONSTRUCTOR_DROP_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    MODAL_WINDOW = (By.XPATH, "//section[contains(@class, 'Modal_modal')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal')]//button")
    MODAL_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")


class OrderFeedLocators:
    FEED_HEADER_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    
    # Точный и стабильный селектор для карточки заказа в ленте
    ORDER_CARD = (By.XPATH, "//div[contains(@class, 'OrderHistory_listItem')]//a | //ul[contains(@class, 'OrderFeed_orderList')]//li[1]")
    
    MODAL_WINDOW = (By.XPATH, "//section[contains(@class, 'Modal_modal')]")
    ORDER_MODAL_TITLE = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//h2[contains(@class, 'text_type_digits-default')]")
    
    TOTAL_ORDERS_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")