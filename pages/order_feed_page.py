from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderFeedPage(BasePage):
    TOTAL_COUNTER = (By.XPATH, "//p[text()='Выполнено за всё время']/following-sibling::p")
    TODAY_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня']/following-sibling::p")
    ORDER_IN_WORK = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList')]/li[contains(@class, 'text_type_digits-default')]")

    def get_total_orders_count(self):
        self.wait.until(lambda d: self.driver.find_element(*self.TOTAL_COUNTER).text.isdigit())
        return int(self.get_text(self.TOTAL_COUNTER))

    def get_today_orders_count(self):
        self.wait.until(lambda d: self.driver.find_element(*self.TODAY_COUNTER).text.isdigit())
        return int(self.get_text(self.TODAY_COUNTER))

    def get_order_number_in_work(self):
        self.wait.until(lambda d: len(self.driver.find_elements(*self.ORDER_IN_WORK)) > 0)
        return self.get_text(self.ORDER_IN_WORK)