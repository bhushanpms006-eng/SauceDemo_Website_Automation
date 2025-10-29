from selenium.webdriver.common.by import By


class ConfirmationLocators:
    CONFIRMATION_MSG = (By.XPATH, "//h2[contains(text(),'Thank you for your order!')]")
