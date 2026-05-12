import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)
        return self

    @allure.step("Найти элемент {locator}")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Кликнуть на элемент {locator}")
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return self

    @allure.step("Кликнуть на элемент с прокруткой {locator}")
    def click_with_scroll(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        return self

    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Дождаться видимости элемента {locator}")
    def wait_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Дождаться невидимости элемента {locator}")
    def wait_invisibility(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Ожидать, что текст элемента {locator} станет числом")
    def wait_for_text_to_be_digit(self, locator):
        self.wait.until(lambda d: self.find_element(locator).text.isdigit())

    @allure.step("Получить исходный код страницы")
    def get_page_source(self):
        return self.driver.page_source

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url