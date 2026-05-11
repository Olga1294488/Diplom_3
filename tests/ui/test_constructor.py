import allure
import pytest
from pages.ingredient_modal import IngredientModal
from data import CONSTRUCTOR_HEADER   

@allure.epic("Stellar Burgers UI")
@allure.feature("Конструктор")
class TestConstructor:

    @allure.title("Переход по клику на «Конструктор»")
    def test_constructor_navigation(self, main_page):
        main_page.click_order_feed()
        main_page.click_constructor()
        assert CONSTRUCTOR_HEADER in main_page.driver.page_source

    @allure.title("Переход по клику на «Лента заказов»")
    def test_order_feed_navigation(self, main_page):
        main_page.click_order_feed()
        assert "feed" in main_page.driver.current_url

    @allure.title("Клик на ингредиент открывает всплывающее окно с деталями")
    def test_ingredient_modal_opens(self, main_page):
        main_page.click_ingredient()
        modal = IngredientModal(main_page.driver)
        modal.wait_visibility(modal.MODAL)
        assert modal.is_modal_displayed()   

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_close_modal_by_cross(self, main_page):
        main_page.click_ingredient()
        modal = IngredientModal(main_page.driver)
        modal.wait_visibility(modal.MODAL)
        modal.close_modal()
        assert not modal.is_modal_displayed()

    @allure.title("При добавлении ингредиента счётчик увеличивается")
    def test_ingredient_counter_increases(self, main_page):
        initial = int(main_page.get_ingredient_counter())
        main_page.drag_and_drop_ingredient()   
        new = int(main_page.get_ingredient_counter())
        assert new == initial + 1