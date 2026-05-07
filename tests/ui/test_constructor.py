from pages.ingredient_modal import IngredientModal
from selenium.webdriver.support import expected_conditions as EC
from data import CONSTRUCTOR_HEADER

class TestConstructor:
    def test_constructor_navigation(self, main_page):
        main_page.click_order_feed()
        main_page.click_constructor()
        assert CONSTRUCTOR_HEADER in main_page.driver.page_source

    def test_order_feed_navigation(self, main_page):
        main_page.click_order_feed()
        assert "feed" in main_page.driver.current_url

    def test_ingredient_modal_opens(self, main_page):
        main_page.click_ingredient()
        modal = IngredientModal(main_page.driver)
        modal.wait_visibility(modal.MODAL)
        assert modal.find_element(modal.MODAL).is_displayed()

    def test_close_modal_by_cross(self, main_page):
        main_page.click_ingredient()
        modal = IngredientModal(main_page.driver)
        modal.close_modal()
        modal.wait.until(EC.invisibility_of_element_located(modal.MODAL))

    def test_ingredient_counter_increases(self, main_page):
        main_page.reset_cart()
        initial = int(main_page.get_ingredient_counter())
        main_page.drag_and_drop(main_page.INGREDIENT, main_page.TARGET_CONSTRUCTOR)
        new = int(main_page.get_ingredient_counter())
        assert new == initial + 1