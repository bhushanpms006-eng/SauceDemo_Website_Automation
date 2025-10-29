from selenium.webdriver.common.by import By

class CheckoutLocators:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.XPATH, "//button[contains(text(),'Finish')]")
