import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class IngredientModal(BasePage):
    MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__TnseK')]")

    @allure.step("Проверить, что модальное окно ингредиента отображается")
    def is_modal_displayed(self):
        try:
            return self.wait_visibility(self.MODAL).is_displayed()
        except:
            return False

    @allure.step("Закрыть модальное окно кликом по крестику")
    def close_modal(self):
        self.click(self.CLOSE_BUTTON)
        self.wait_invisibility(self.MODAL)
        return self
  
   