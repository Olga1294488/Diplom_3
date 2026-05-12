import allure
import pytest
from pages.order_feed_page import OrderFeedPage

@allure.epic("Stellar Burgers UI")
@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("При создании заказа счётчик «Выполнено за всё время» увеличивается")
    def test_total_orders_counter_increases(self, main_page, driver):
        main_page.click_order_feed()
        feed = OrderFeedPage(driver)
        initial = feed.get_total_orders_count()
        main_page.click_constructor()
        main_page.drag_and_drop_ingredient()
        main_page.place_order()
        main_page.click_order_feed()
        new = feed.get_total_orders_count()
        assert new > initial

    @allure.title("При создании заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_today_orders_counter_increases(self, main_page, driver):
        main_page.click_order_feed()
        feed = OrderFeedPage(driver)
        initial = feed.get_today_orders_count()
        main_page.click_constructor()
        main_page.drag_and_drop_ingredient()
        main_page.place_order()
        main_page.click_order_feed()
        new = feed.get_today_orders_count()
        assert new > initial

    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    def test_order_number_appears_in_work(self, main_page, driver):
        main_page.click_constructor()
        main_page.drag_and_drop_ingredient()
        order_number = main_page.place_order()
        main_page.click_order_feed()
        feed = OrderFeedPage(driver)
        order_in_work = feed.get_order_number_in_work()
        assert order_number in order_in_work