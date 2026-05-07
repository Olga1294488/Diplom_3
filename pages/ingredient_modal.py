from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class IngredientModal(BasePage):
    MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__container__Wo2l_')]")
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__TnseK')]")

    def close_modal(self):
        element = self.find_element(self.CLOSE_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)
        self.wait.until(EC.invisibility_of_element_located(self.MODAL))
        return self