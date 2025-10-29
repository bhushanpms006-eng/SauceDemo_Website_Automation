from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger
from utils.read_config import config

class ConfirmationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, int(config.get("DEFAULT", "explicit_wait", fallback="10")))
        self.logger = get_logger(self.__class__.__name__)

        self.confirmation_msg = (By.XPATH, "//h2[contains(text(),'Thank you for your order!')]")

    def get_confirmation_message(self):
        self.logger.info("Retrieving order confirmation message.")
        msg = self.wait.until(EC.visibility_of_element_located(self.confirmation_msg)).text
        self.logger.info(f"Confirmation message found: {msg}")
        return msg
