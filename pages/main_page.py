import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    CONSTRUCTOR_BUTTON = (By.CSS_SELECTOR, "a[href='/']")
    ORDER_FEED_BUTTON = (By.CSS_SELECTOR, "a[href='/feed']")
    INGREDIENT = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
    COUNTER = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/ancestor::a//div[contains(@class, 'counter')]//p")
    ADD_BUTTON_IN_MODAL = (By.XPATH, "//button[text()='Добавить']")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__TnseK')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_NUMBER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//h2")
    TARGET_CONSTRUCTOR = (By.CSS_SELECTOR, ".constructor-element_pos_top")

    @allure.step("Кликнуть на кнопку «Конструктор»")
    def click_constructor(self):
        self.click(self.CONSTRUCTOR_BUTTON)
        return self

    @allure.step("Кликнуть на кнопку «Лента заказов»")
    def click_order_feed(self):
        self.click(self.ORDER_FEED_BUTTON)
        return self

    @allure.step("Кликнуть на ингредиент «Флюоресцентная булка R2-D3»")
    def click_ingredient(self):
        element = self.find_element(self.INGREDIENT)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)
        # Ожидание модального окна теперь в тесте
        return self

    @allure.step("Получить значение счётчика ингредиента")
    def get_ingredient_counter(self):
        try:
            return self.get_text(self.COUNTER)
        except:
            return "0"

    @allure.step("Добавить ингредиент перетаскиванием (drag-and-drop)")
    def drag_and_drop_ingredient(self):
        from selenium.webdriver.common.action_chains import ActionChains
        source = self.find_element(self.INGREDIENT)
        target = self.find_element(self.TARGET_CONSTRUCTOR)
        ActionChains(self.driver).drag_and_drop(source, target).perform()
        self.wait.until(lambda d: self.get_ingredient_counter() != "0")
        return self

    @allure.step("Оформить заказ")
    def place_order(self):
        self.click(self.ORDER_BUTTON)
        self.wait_visibility(self.ORDER_NUMBER_MODAL)
        order_number = self.get_text(self.ORDER_NUMBER_MODAL)
        self.click(self.CLOSE_MODAL_BUTTON)
        return order_number