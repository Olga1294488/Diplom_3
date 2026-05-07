from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from pages.ingredient_modal import IngredientModal
from data import BUN_NAME, SAUCE_NAME

class MainPage(BasePage):
    CONSTRUCTOR_BUTTON = (By.CSS_SELECTOR, "a[href='/']")
    ORDER_FEED_BUTTON = (By.CSS_SELECTOR, "a[href='/feed']")
    INGREDIENT = (By.XPATH, f"//p[text()='{BUN_NAME}']")
    SAUCE = (By.XPATH, f"//p[text()='{SAUCE_NAME}']")
    COUNTER = (By.XPATH, f"//p[text()='{BUN_NAME}']/ancestor::a//div[contains(@class, 'counter')]//p")
    ADD_BUTTON_IN_MODAL = (By.XPATH, "//button[text()='Добавить']")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__TnseK')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_NUMBER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//h2")
    TARGET_CONSTRUCTOR = (By.CSS_SELECTOR, ".constructor-element_pos_top")

    def click_constructor(self):
        self.click(self.CONSTRUCTOR_BUTTON)
        return self

    def click_order_feed(self):
        self.click(self.ORDER_FEED_BUTTON)
        return self

    def click_ingredient(self):
        element = self.find_element(self.INGREDIENT)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)
        IngredientModal(self.driver).wait_visibility(IngredientModal.MODAL)
    # Удалите строку с assert modal.is_modal_displayed()
        return self

    def get_ingredient_counter(self):
        return self.get_text(self.COUNTER)

    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        ActionChains(self.driver).drag_and_drop(source, target).perform()
        return self

    def reset_cart(self):
        self.driver.refresh()
        self.wait.until(lambda d: "Соберите бургер" in d.page_source)
        return self

    def build_full_burger(self):
        self.drag_and_drop(self.INGREDIENT, self.TARGET_CONSTRUCTOR)
        self.drag_and_drop(self.SAUCE, self.TARGET_CONSTRUCTOR)
        return self

    def place_order(self):
        self.click(self.ORDER_BUTTON)
        self.wait_visibility(self.ORDER_NUMBER_MODAL)
        order_number = self.get_text(self.ORDER_NUMBER_MODAL)
        self.click(self.CLOSE_MODAL_BUTTON)
        return order_number