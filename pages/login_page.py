from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.header_text = (By.XPATH, "//div[contains(text(),'Swag Labs')]")

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_input)
        ).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def verify_login_success(self):
        """Wait until 'Swag Labs' appears after login and return True/False"""
        try:
            txt = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.header_text)
            ).text
            if "Swag Labs" in txt:
                print("__User logged in successfully!__")
                return True
        except:
            print("__Login failed or page not loaded correctly__.")
            return False
