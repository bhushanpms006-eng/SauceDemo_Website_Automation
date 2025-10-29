from selenium.webdriver.common.by import By


class LoginLocators:
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")
    HEADER_TEXT = (By.XPATH, "//div[contains(text(),'Swag Labs')]")
