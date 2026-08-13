from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from locators import OrderFeedLocators, ConstructorPageLocators, LoginPageLocators
from data import URL


class TestOrderFeed:

    def test_open_order_details_modal(self, driver):
        driver.get(URL.BASE_URL)
        
        biscuit = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(ConstructorPageLocators.FIRST_INGREDIENT)
        )
        drop_area = driver.find_element(*ConstructorPageLocators.CONSTRUCTOR_DROP_AREA)
        ActionChains(driver).drag_and_drop(biscuit, drop_area).perform()
        
        make_order_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(LoginPageLocators.MAKE_ORDER_BUTTON)
        )
        make_order_button.click()
        
        WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located(OrderFeedLocators.MODAL_WINDOW)
        )
        close_button = driver.find_element(*ConstructorPageLocators.MODAL_CLOSE_BUTTON)
        close_button.click()

        driver.get(URL.FEED_URL)
    
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(OrderFeedLocators.FEED_TITLE)
        )
    
        order_card = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(OrderFeedLocators.ORDER_CARD)
        )
    
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", order_card)
        driver.execute_script("arguments[0].click();", order_card)
    
        modal_title = WebDriverWait(driver, 25).until(
            EC.visibility_of_element_located(OrderFeedLocators.ORDER_MODAL_TITLE)
        )
        assert modal_title.is_displayed()

    def test_total_orders_counter_increases(self, driver):
        driver.get(URL.FEED_URL)
        counter = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(OrderFeedLocators.TOTAL_ORDERS_COUNT)
        )
        assert counter.text.isdigit()

    def test_today_orders_counter_increases(self, driver):
        driver.get(URL.FEED_URL)
        counter = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(OrderFeedLocators.TODAY_ORDERS_COUNT)
        )
        assert counter.text.isdigit()
