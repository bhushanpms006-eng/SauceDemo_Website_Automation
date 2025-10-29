from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger
from utils.read_config import config

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, int(config.get("DEFAULT", "explicit_wait", fallback="10")))
        self.logger = get_logger(self.__class__.__name__)

        self.products_names = (By.CSS_SELECTOR, "div.inventory_item_name")
        self.sort_dropdown = (By.CLASS_NAME, "product_sort_container")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def get_all_products(self):
        self.logger.info("Fetching list of available products.")
        elements = self.wait.until(EC.visibility_of_all_elements_located(self.products_names))
        product_names = [p.text for p in elements]
        self.logger.info(f"Products found: {product_names}")
        return product_names

    def add_product_to_cart(self, product_id):
        button = (By.ID, f"add-to-cart-{product_id}")
        self.logger.info(f"Adding product to cart: {product_id}")
        self.wait.until(EC.element_to_be_clickable(button)).click()
        badge = self.wait.until(EC.visibility_of_element_located(self.cart_badge))
        self.logger.info(f"Product added. Cart count: {badge.text}")
        return True

    def go_to_cart(self):
        self.logger.info("Navigating to cart page.")
        self.wait.until(EC.element_to_be_clickable(self.cart_link)).click()
