from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.NAME, "checkout")
        self.cart_items = (By.CLASS_NAME, "inventory_item_name")

    def verify_product_in_cart(self, expected_product_name):
        """Verify if specific product is displayed in the cart."""
        items = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.cart_items)
        )
        item_names = [i.text for i in items]

        if expected_product_name in item_names:
            print(f" '{expected_product_name}' is visible in the cart.")
            return True
        else:
            print(f" '{expected_product_name}' is NOT found in the cart.")
            print(f"Items found: {item_names}")
            return False

    def proceed_to_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()
