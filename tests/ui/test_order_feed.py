from pages.order_feed_page import OrderFeedPage

class TestOrderFeed:
    def test_total_orders_counter_increases(self, main_page, driver):
        main_page.click_order_feed()
        feed = OrderFeedPage(driver)
        initial_total = feed.get_total_orders_count()

        main_page.click_constructor()
        main_page.build_full_burger()
        main_page.place_order()

        main_page.click_order_feed()
        main_page.wait.until(lambda d: feed.get_total_orders_count() > initial_total)
        new_total = feed.get_total_orders_count()
        assert new_total > initial_total

    def test_today_orders_counter_increases(self, main_page, driver):
        main_page.click_order_feed()
        feed = OrderFeedPage(driver)
        initial_today = feed.get_today_orders_count()

        main_page.click_constructor()
        main_page.build_full_burger()
        main_page.place_order()

        main_page.click_order_feed()
        main_page.wait.until(lambda d: feed.get_today_orders_count() > initial_today)
        new_today = feed.get_today_orders_count()
        assert new_today > initial_today

    def test_order_number_appears_in_work(self, main_page, driver):
        main_page.click_constructor()
        main_page.build_full_burger()
        order_number = main_page.place_order()

        main_page.click_order_feed()
        feed = OrderFeedPage(driver)
        main_page.wait.until(lambda d: order_number in feed.get_order_number_in_work())
        order_in_work = feed.get_order_number_in_work()
        assert order_number in order_in_work