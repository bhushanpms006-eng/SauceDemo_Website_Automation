from selenium.webdriver.common.by import By

class ProductsPageLocators:
    ALL_PRODUCTS = (By.CSS_SELECTOR, ".inventory_item_name")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    # Instead of hardcoding inside method, define a dynamic locator as a method
    @staticmethod
    def add_to_cart_button(product_id):
        return (By.ID, f"add-to-cart-{product_id}")
