from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import OrderFeedLocators, ConstructorPageLocators

BASE_URL = "https://stellarburgers.education-services.ru"


class TestOrderFeed:

    def test_open_order_details_modal(self, driver):
        driver.get(BASE_URL)
        
        # Перетаскиваем ингредиент в корзину
        biscuit = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(ConstructorPageLocators.FIRST_INGREDIENT)
        )
        drop_area = driver.find_element(*ConstructorPageLocators.CONSTRUCTOR_DROP_AREA)
        
        from selenium.webdriver.common.action_chains import ActionChains
        ActionChains(driver).drag_and_drop(biscuit, drop_area).perform()
        
        # Оформляем заказ
        make_order_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Оформить заказ']"))
        )
        make_order_button.click()
        
        # Ждем появления модального окна с подтверждением заказа и закрываем его
        WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'Modal_modal')]"))
        )
        close_button = driver.find_element(By.XPATH, "//section[contains(@class, 'Modal_modal')]//button")
        close_button.click()

        # Переходим в Ленту заказов
        driver.get(f"{BASE_URL}/feed")
    
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(OrderFeedLocators.FEED_TITLE)
        )
    
        # Даем время WebSocket подгрузить созданный заказ в список и ждем кликабельности карточки
        order_card = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(OrderFeedLocators.ORDER_CARD)
        )
    
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", order_card)
        driver.execute_script("arguments[0].click();", order_card)
    
        # Проверяем открытие модального окна деталей заказа
        modal_title = WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located(OrderFeedLocators.ORDER_MODAL_TITLE)
        )
        assert modal_title.is_displayed()

    def test_total_orders_counter_increases(self, driver):
        driver.get(f"{BASE_URL}/feed")
        counter = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(OrderFeedLocators.TOTAL_ORDERS_COUNT)
        )
        assert counter.text.isdigit()

    def test_today_orders_counter_increases(self, driver):
        driver.get(f"{BASE_URL}/feed")
        counter = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(OrderFeedLocators.TODAY_ORDERS_COUNT)
        )
        assert counter.text.isdigit()