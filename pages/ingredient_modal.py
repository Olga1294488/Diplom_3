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
    
    def test_ingredient_modal_opens(self, main_page):
        main_page.click_ingredient()
        modal = IngredientModal(main_page.driver)
        modal.wait_visibility(modal.MODAL)   
        assert modal.is_modal_displayed()

    def test_close_modal_by_cross(self, main_page):
        main_page.click_ingredient()
        modal = IngredientModal(main_page.driver)
        modal.wait_visibility(modal.MODAL)  
        modal.close_modal()
        assert not modal.is_modal_displayed()