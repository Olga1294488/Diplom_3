import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

# Кастомное ожидание: текст элемента состоит только из цифр
class text_to_be_digit:
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        return element.text.isdigit()

class OrderFeedPage(BasePage):
    TOTAL_COUNTER = (By.XPATH, "//p[text()='Выполнено за всё время']/following-sibling::p")
    TODAY_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня']/following-sibling::p")
    ORDER_IN_WORK = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList')]/li[contains(@class, 'text_type_digits-default')]")

    @allure.step("Получить значение счётчика «Выполнено за всё время»")
    def get_total_orders_count(self):
        self.wait.until(text_to_be_digit(self.TOTAL_COUNTER))
        return int(self.get_text(self.TOTAL_COUNTER))

    @allure.step("Получить значение счётчика «Выполнено за сегодня»")
    def get_today_orders_count(self):
        self.wait.until(text_to_be_digit(self.TODAY_COUNTER))
        return int(self.get_text(self.TODAY_COUNTER))

    @allure.step("Получить номер заказа в разделе «В работе»")
    def get_order_number_in_work(self):
        return self.get_text(self.ORDER_IN_WORK)