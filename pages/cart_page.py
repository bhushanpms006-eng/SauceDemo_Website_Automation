from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger
from utils.read_config import config

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, int(config.get("DEFAULT", "explicit_wait", fallback="10")))
        self.logger = get_logger(self.__class__.__name__)

        self.checkout_button = (By.NAME, "checkout")
        self.cart_items = (By.CLASS_NAME, "inventory_item_name")

    def verify_product_in_cart(self, expected_product_name):
        self.logger.info(f"Verifying '{expected_product_name}' is present in the cart.")
        items = self.wait.until(EC.visibility_of_all_elements_located(self.cart_items))
        names = [i.text for i in items]
        if expected_product_name in names:
            self.logger.info(f"Product '{expected_product_name}' verified in cart.")
            return True
        self.logger.warning(f"Product '{expected_product_name}' not found in cart. Found items: {names}")
        return False

    def proceed_to_checkout(self):
        self.logger.info("Clicking on checkout button.")
        self.wait.until(EC.element_to_be_clickable(self.checkout_button)).click()
