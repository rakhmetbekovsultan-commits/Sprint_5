from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import ConstructorPageLocators
from data import URL

BASE_URL = "https://stellarburgers.education-services.ru"


class TestConstructor:

    # 1. Проверка перехода к вкладке «Соусы»
    def test_transition_to_sauces_tab(self, driver):
        driver.get(BASE_URL)

        # Кликаем по вкладке «Соусы»
        sauces_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorPageLocators.TAB_SAUCES)
        )
        sauces_tab.click()

        # Проверяем, что вкладка стала активной
        assert "tab_type_current" in sauces_tab.get_attribute("class")

    # 2. Проверка перехода к вкладке «Начинки»
    def test_transition_to_fillings_tab(self, driver):
        driver.get(BASE_URL)

        # Кликаем по вкладке «Начинки»
        fillings_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorPageLocators.TAB_FILLINGS)
        )
        fillings_tab.click()

        # Проверяем, что вкладка стала активной
        assert "tab_type_current" in fillings_tab.get_attribute("class")

    # 3. Проверка перехода к вкладке «Булки»
    def test_transition_to_buns_tab(self, driver):
        driver.get(BASE_URL)

        # Сначала переходим на другую вкладку
        driver.find_element(*ConstructorPageLocators.TAB_SAUCES).click()

        # Возвращаемся к булкам
        buns_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorPageLocators.TAB_BUNS)
        )
        buns_tab.click()

        # Проверяем активность вкладки булок так же, как и остальные вкладки
        assert "tab_type_current" in buns_tab.get_attribute("class")

    # 4. Проверка открытия модального окна ингредиента
    def test_open_ingredient_modal(self, driver):
        driver.get(BASE_URL)

        # Кликаем по первому ингредиенту в конструкторе
        first_ingredient = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorPageLocators.FIRST_INGREDIENT)
        )
        first_ingredient.click()

        # Проверяем, что модальное окно с деталями появилось
        modal = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorPageLocators.MODAL_WINDOW)
        )
        assert modal.is_displayed()

        modal_title = driver.find_element(*ConstructorPageLocators.MODAL_TITLE)
        assert modal_title.is_displayed()

    # 5. Проверка закрытия модального окна кликом на крестик
    def test_close_ingredient_modal(self, driver):
        driver.get(BASE_URL)

        # Открываем модальное окно
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorPageLocators.FIRST_INGREDIENT)
        ).click()

        # Ждем появления крестика и кликаем по нему
        close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ConstructorPageLocators.MODAL_CLOSE_BUTTON)
        )
        close_button.click()

        # Проверяем, что модальное окно закрылось (исчезло)
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located(ConstructorPageLocators.MODAL_WINDOW)
        )
        # assert для финальной проверки отсутствия модального окна в DOM
        modal_elements = driver.find_elements(*ConstructorPageLocators.MODAL_WINDOW)
        assert len(modal_elements) == 0
