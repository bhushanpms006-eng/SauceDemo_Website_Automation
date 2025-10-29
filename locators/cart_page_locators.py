from selenium.webdriver.common.by import By

class CartPageLocators:
    CART_ITEMS = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.NAME, "checkout")
