from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

logger = get_logger(__name__)


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.XPATH, "//h3[@data-test='error']")

    def login_to_application(self, username, password):
        """Enter username, password, and click login."""
        logger.info(f"Attempting login with user: {username}")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_field)
        ).clear()
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).clear()
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        logger.info("Entered credentials, clicking Login button.")

    def is_login_successful(self):
        """Return True if login succeeded, False if error is displayed."""
        try:
            WebDriverWait(self.driver, 5).until(
                EC.url_contains("inventory.html")
            )
            logger.info("Login successful and inventory page loaded.")
            return True
        except Exception:
            try:
                error_text = WebDriverWait(self.driver, 3).until(
                    EC.visibility_of_element_located(self.error_message)
                ).text
                logger.warning(f"Login failed, error displayed: {error_text}")
            except Exception:
                logger.error("Login failed — no success or error detected.")
            return False
    def get_error_message(self):
        """Return the error message text if displayed, else None."""
        try:
            error_element = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(self.error_message)
            )
            error_text = error_element.text
            logger.info(f"Captured login error message: {error_text}")
            return error_text
        except Exception:
            logger.info("No error message displayed after login attempt.")
            return None
