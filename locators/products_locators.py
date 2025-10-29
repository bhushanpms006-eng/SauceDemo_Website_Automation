from selenium.webdriver.common.by import By


class ProductsLocators:
    PRODUCT_NAMES = (By.CSS_SELECTOR, "div.inventory_item_name")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    CART_LINK = (By.XPATH, "//a[@data-test='shopping-cart-link']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    @staticmethod
    def add_to_cart_button(product_id: str):
        """Dynamic locator for add-to-cart button by product id."""
        return By.ID, f"add-to-cart-{product_id}"
