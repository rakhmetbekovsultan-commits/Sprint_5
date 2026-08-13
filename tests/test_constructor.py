from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import ConstructorPageLocators
from data import URL


class TestConstructor:

    def test_transition_to_sauces_tab(self, driver):
        driver.get(URL.BASE_URL)

        sauces_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorPageLocators.TAB_SAUCES)
        )
        sauces_tab.click()

        assert "tab_type_current" in sauces_tab.get_attribute("class")

    def test_transition_to_fillings_tab(self, driver):
        driver.get(URL.BASE_URL)

        fillings_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorPageLocators.TAB_FILLINGS)
        )
        fillings_tab.click()

        assert "tab_type_current" in fillings_tab.get_attribute("class")

    def test_transition_to_buns_tab(self, driver):
        driver.get(URL.BASE_URL)

        driver.find_element(*ConstructorPageLocators.TAB_SAUCES).click()

        buns_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorPageLocators.TAB_BUNS)
        )
        buns_tab.click()

        assert "tab_type_current" in buns_tab.get_attribute("class")

    def test_open_ingredient_modal(self, driver):
        driver.get(URL.BASE_URL)

        first_ingredient = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorPageLocators.FIRST_INGREDIENT)
        )
        first_ingredient.click()

        modal = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorPageLocators.MODAL_WINDOW)
        )
        assert modal.is_displayed()


    def test_close_ingredient_modal(self, driver):
        driver.get(URL.BASE_URL)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorPageLocators.FIRST_INGREDIENT)
        ).click()

        close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorPageLocators.MODAL_CLOSE_BUTTON)
        )
        close_button.click()

        assert WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located(ConstructorPageLocators.MODAL_WINDOW)
        )
