from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.products_names = (By.CSS_SELECTOR, "div.inventory_item_name")
        self.sort_dropdown = (By.CLASS_NAME, "product_sort_container")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def get_all_products(self):
        elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.products_names)
        )
        return [p.text for p in elements]

    def add_product_to_cart(self, product_id):
        """Add product to cart by product_id and verify it was added."""
        button = (By.ID, f"add-to-cart-{product_id}")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(button)
        ).click()

        #  Verify product added by checking cart badge count
        try:
            badge = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.cart_badge)
            )
            if badge.text.isdigit() and int(badge.text) > 0:
                print(f" Product '{product_id}' successfully added to cart! Cart count: {badge.text}")
                return True
        except:
            print(f" Product '{product_id}' was not added to cart.")
        return False

    def go_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_link)
        ).click()
