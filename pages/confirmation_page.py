from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ConfirmationPage:
    def __init__(self, driver):
        self.driver = driver
        self.confirmation_msg = (By.XPATH, "//h2[contains(text(),'Thank you for your order!')]")

    def get_confirmation_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.confirmation_msg)
        ).text
