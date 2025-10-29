from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger
from utils.read_config import config

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, int(config.get("DEFAULT", "explicit_wait", fallback="10")))
        self.logger = get_logger(self.__class__.__name__)

        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_btn = (By.ID, "continue")
        self.finish_btn = (By.XPATH, "//button[contains(text(),'Finish')]")

    def fill_information(self, first, last, postal):
        self.logger.info(f"Filling checkout details: {first} {last}, {postal}")
        self.wait.until(EC.visibility_of_element_located(self.first_name)).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.postal_code).send_keys(postal)
        self.driver.find_element(*self.continue_btn).click()
        self.logger.info("Checkout details submitted successfully.")

    def finish_checkout(self):
        self.logger.info("Clicking Finish to complete checkout.")
        self.wait.until(EC.element_to_be_clickable(self.finish_btn)).click()
